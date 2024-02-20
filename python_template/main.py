from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

import python_template
import python_template.config as cfg
from python_template.api.health.main import router as health_app_router

app = FastAPI(
    title=cfg.PROJECT_NAME,
    description=f"Base API for {cfg.PROJECT_NAME}.",
    version=python_template.__version__,
)

app.include_router(health_app_router, tags=["healthcheck"])


# Base route
@app.get(
    "/",
    description=f"Base route of the {cfg.PROJECT_NAME} API.",
    tags=["base"],
)
async def main_route() -> JSONResponse:
    """
    Base route
    """
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": f"Welcome to {cfg.PROJECT_NAME}!",
            "version": python_template.__version__,
        },
    )

@app.get(
    "/version",
    description=f"Version route of the {cfg.PROJECT_NAME} API.",
    tags=["base"],
)
async def version_route() -> JSONResponse:
    """
    Version route
    """
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "version": python_template.__version__,
        },
    )