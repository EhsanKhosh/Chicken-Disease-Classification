from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationTrainingPipeline

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

STAGE_NAME = "Training stage"

try:
    logger.info("*" * 20)
    logger.info(f"Starting stage {STAGE_NAME}")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f"stage {STAGE_NAME} completed\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation stage"

try:
    logger.info("*" * 20)
    logger.info(f"Starting stage {STAGE_NAME}")
    evaluation = EvaluationTrainingPipeline()
    evaluation.main()
    logger.info(f"stage {STAGE_NAME} completed\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e
