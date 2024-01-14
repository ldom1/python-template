import os

import structlog
from dotenv import find_dotenv, load_dotenv
from mongodb_python_manager import MongoDBManager

load_dotenv(find_dotenv())

# Initialize logger
logger = structlog.get_logger()


def get_mongodb_manager():
    """
    Function to connect to MongoDB and return the MongoDB manager
    :return: MongoDB manager

    For more information on how to use the MongoDB manager, see: https://pypi.org/project/mongodb-python-manager/
    """
    structlog.contextvars.bind_contextvars(function_name="get_mongodb_manager")

    mongodb_manager = MongoDBManager(
        mongo_db_user=os.environ.get("MONGO_DB_USER"),
        mongo_db_password=os.environ.get("MONGO_DB_PASSWORD"),
        mongo_db_cluster=os.environ.get("MONGO_DB_CLUSTER"),
        mongodb_db_name=os.environ.get("MONGO_DB_DBNAME"),
    )
    return mongodb_manager
