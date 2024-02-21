from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = 'Data Ingestion stage'


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_data()


if __name__ == '__main__':
    try:
        logger.info('Starting stage {}'.format(STAGE_NAME))
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'stage {STAGE_NAME} has completed')

    except Exception as e:
        logger.exception(e)
        raise e
