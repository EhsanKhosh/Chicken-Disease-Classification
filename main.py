from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info('Starting stage {}'.format(STAGE_NAME))
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'stage {STAGE_NAME} has completed')

except Exception as e:
    logger.exception(e)
    raise e


