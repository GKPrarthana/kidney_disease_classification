import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config):
        self.config = config
        
    def download_file(self) -> str:
        """Download file from the given URL"""
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)

            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            # Extract file ID correctly
            file_id = dataset_url.split("/")[-2]
            download_url = f"https://drive.google.com/uc?id={file_id}"

            # Download file using gdown
            gdown.download(download_url, zip_download_dir, quiet=False)

            logger.info(f"File downloaded successfully: {zip_download_dir}")
        except Exception as e:
            logger.error(f"Error downloading file: {e}")
            return str(e)

    def extract_zip_file(self):
        """Extracts the zip file into the data directory"""
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            if not os.path.exists(self.config.local_data_file):
                raise FileNotFoundError(f"Zip file not found: {self.config.local_data_file}")

            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)

            logger.info(f"File extracted successfully to {unzip_path}")

        except Exception as e:
            logger.error(f"Error extracting file: {e}")
            raise e