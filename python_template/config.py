import structlog
import os

# Logger
logger = structlog.get_logger()

# Global variables
PROJECT_NAME = "python_template"
IMAGE_FILE_EXTENSIONS = ["jpg", "jpeg", "png"]

# Hosting
HOST = os.environ.get("HOST", "localhost")
PORT = os.environ.get("HOST", 8000)

