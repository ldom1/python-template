from uuid import uuid4

from fastapi import APIRouter, status

from python_template.storage.mongodb import get_mongodb_manager

router = APIRouter()


@router.post(
    "/test_mongodb_post",
    tags=["test"],
    summary="Perform a POST test to write data in MongoDB",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
)
def test_post_mongodb() -> dict:
    """
    ## Perform a POST test to write data in MongoDB
    Endpoint to perform a POST test to write data in MongoDB.
    Returns:
        dict: Returns a JSON response with the health status
    """
    # Get MongoDB session
    mongodb_manager = get_mongodb_manager()
    mongodb_manager.set_collection_name("test")
    mongodb_manager.insert_document_in_collection(item={"test": f"test_{str(uuid4())}"})

    return {
        "message": "POST test to write data in MongoDB",
        "status_code": status.HTTP_200_OK,
        "status": "OK",
    }


@router.post(
    "/test_mongodb_empty_db",
    tags=["test"],
    summary="Empty test collection in MongoDB",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
)
def test_empty_mongodb() -> dict:
    """
    ## Empty test collection in MongoDB
    Endpoint to empty test collection in MongoDB.
    Returns:
        dict: Returns a JSON response with the health status
    """
    # Get MongoDB session
    mongodb_manager = get_mongodb_manager()
    mongodb_manager.set_collection_name("test")
    mongodb_manager.delete_all_documents_from_collection()

    return {
        "message": "Empty test collection in MongoDB",
        "status_code": status.HTTP_200_OK,
        "status": "OK",
    }
