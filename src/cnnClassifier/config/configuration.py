from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_dirs
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
            self,
            config_dir=CONFIG_FILE_PATH,
            params_file=PARAMS_FILE_PATH):
        self.config = read_yaml(config_dir)
        self.params = read_yaml(params_file)

        create_dirs([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_file
        )
        return data_ingestion_config
