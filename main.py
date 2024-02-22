from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info('Starting stage {}'.format(STAGE_NAME))
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'stage {STAGE_NAME} has completed')

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"

try:
    logger.info(f"Starting stage {STAGE_NAME}")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e
