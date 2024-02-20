import datetime
import io
import os
import uuid
from typing import Dict, List

import boto3
from dotenv import find_dotenv, load_dotenv
from PIL import Image

import python_template.config as cfg

load_dotenv(find_dotenv())


class S3Storage:
    def __init__(
        self,
        bucket_name: str = None,
        aws_access_key_id: str = None,
        aws_secret_access_key: str = None,
        aws_region: str = None,
    ):
        """
        Initializes the S3Storage class

        :param bucket_name: Name of the bucket to use
        :param aws_access_key_id: AWS access key (optional)
        :param aws_secret_access_key: AWS secret key (optional)
        :param aws_region: AWS region (optional)
        """
        self.bucket_name = (
            bucket_name if bucket_name else os.environ.get("AWS_BUCKET_NAME")
        )
        self.aws_access_key_id = (
            aws_access_key_id
            if aws_access_key_id
            else os.environ.get("AWS_ACCESS_KEY_ID")
        )
        self.aws_secret_access_key = (
            aws_secret_access_key
            if aws_secret_access_key
            else os.environ.get("AWS_SECRET_ACCESS_KEY")
        )
        self.aws_region = (
            aws_region if aws_region else os.environ.get("AWS_DEFAULT_REGION")
        )

        self.check_credentials()

        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_KEY"),
            region_name=os.environ.get("AWS_REGION"),
        )

    def check_credentials(self):
        """
        Checks if the credentials are valid

        :return: None if the credentials are valid or raises an exception if they are not
        """
        if (
            self.bucket_name is None
            and self.aws_access_key_id is None
            and self.aws_secret_access_key is None
        ):
            raise Exception(
                "Bucket name, AWS access key and AWS secret key are not set."
            )
        if self.aws_access_key_id is None and self.aws_secret_access_key is None:
            raise Exception("AWS access key and AWS secret key are not set.")
        if self.bucket_name is None:
            raise Exception("Bucket name is not set.")
        if self.aws_access_key_id is None:
            raise Exception("AWS access key is not set.")
        if self.aws_secret_access_key is None:
            raise Exception("AWS secret key is not set.")

    def list_files_in_prefix(self, prefix: str) -> List[Dict[str, str]]:
        """
        Lists all files in a prefix

        :param prefix: Prefix to list the files from (e.g. file_uploaded/date=2020-01-01)
        :return: List of files in the prefix
        """
        cfg.logger.info(
            f"Listing files in prefix {prefix} from S3 bucket {self.bucket_name}, in region {self.aws_region}"
        )

        # List all files in a prefix
        response = self.s3_client.list_objects_v2(
            Bucket=self.bucket_name, Prefix=prefix
        )
        return response.get("Contents", [])

    def list_prefix_filename_in_prefix(self, prefix: str) -> List[Dict[str, str]]:
        """
        Lists all files in a prefix

        :param prefix: Prefix to list the files from (e.g. file_uploaded/date=2020-01-01)
        :return: List of dictionaries with the prefix and filename
        """
        cfg.logger.info(
            f"Listing files in prefix {prefix} from S3 bucket {self.bucket_name}, in region {self.aws_region}"
        )

        # List all files in a prefix
        files = self.list_files_in_prefix(prefix=prefix)
        files = [
            {
                "prefix": os.path.dirname(y["Key"]),
                "filename": os.path.basename(y["Key"]),
            }
            for y in files
        ]
        return files

    def upload_file_to_s3(
        self,
        file: io.BytesIO,
        file_extension: str,
        prefix: str,
        filename: str = None,
    ) -> Dict[str, str]:
        """
        Uploads a file to S3

        :param file: File to upload to S3.
        :param file_extension: File extension (e.g. png, jpg, txt, etc.)
        :param prefix: Prefix to upload the file to
        :param filename: Filename to upload the file to (optional)

        :return: Dictionary with the prefix, key, filename and upload_at
        """
        datetime_today = datetime.date.today()

        if not filename:
            try:
                filename = file.name
            except AttributeError:
                filename = f"{uuid.uuid4()}.{file_extension}"

        if not prefix:
            prefix = f'file_uploaded/date={datetime_today.strftime("%Y-%m-%d")}'

        key = f"{prefix}/{filename}"

        cfg.logger.info(
            f"Uploading file {filename} to S3 bucket {self.bucket_name}, in region {self.aws_region}"
        )

        # Upload the file to S3
        self.s3_client.upload_fileobj(file, self.bucket_name, key)
        return {
            "prefix": prefix,
            "key": key,
            "filename": filename,
            "upload_at": datetime_today.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def read_image_from_s3(self, prefix: str, filename: str, file_extension: str):
        """
        Reads an image from S3

        :param prefix: Prefix to read the file from
        :param filename: Filename to read the file from
        :param file_extension: File extension (allowed extensions are in cfg.IMAGE_FILE_EXTENSIONS)

        :return: PIL Image object
        """
        cfg.logger.info(
            f"Getting file {filename} from S3 bucket {self.bucket_name}, in region {self.aws_region}"
        )

        if file_extension not in cfg.IMAGE_FILE_EXTENSIONS:
            raise Exception(
                f"File extension {file_extension} is not supported. Supported file extensions are {cfg.IMAGE_FILE_EXTENSIONS}"
            )

        # Get the file from S3
        s3_response_object = self.s3_client.get_object(
            Bucket=self.bucket_name, Key=f"{prefix}/{filename}.{file_extension}"
        )
        object_body = s3_response_object["Body"]

        # Expose an image
        image = Image.open(object_body)
        return image
