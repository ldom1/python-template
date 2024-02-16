import os

from loguru import logger

# Logger
logger = logger.opt(colors=True)
logger.add(
    "logs/{time:YYYY-MM-DD}.log",
    level="INFO",
)

# Global variables
PROJECT_NAME = "python_template"
IMAGE_FILE_EXTENSIONS = ["jpg", "jpeg", "png"]

# Hosting
PYTHON_TEMPLATE_HOST = os.environ.get("PYTHON_TEMPLATE_HOST", "localhost")
PYTHON_TEMPLATE_PORT = os.environ.get("PYTHON_TEMPLATE_PORT", 8000)
