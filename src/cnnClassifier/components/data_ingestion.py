import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, data_config: DataIngestionConfig):
        self.config = data_config

    def download_data(self):
        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(url=self.config.source_URL,
                                                    filename=self.config.local_data_file)
            logger.info(f'Downloading {filename} to {self.config.local_data_file} with headers: {headers}'
                        )

        else:
            logger.info(
                f'File already downloaded: {self.config.local_data_file} with {get_size(Path(self.config.local_data_file))}KB size')

    def extract_data(self):

        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_file:
            zip_file.extractall(unzip_dir)

