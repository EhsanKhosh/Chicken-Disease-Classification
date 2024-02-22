from cnnClassifier.components.callbacks import Callbacks
from cnnClassifier.components.trainer import Trainer
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger

STAGE_NAME = 'Training'


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        callbacks_config = config.get_callbacks_config()
        callbacks_list = Callbacks(callbacks_config)
        callbacks_list = callbacks_list.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        trainer = Trainer(training_config)
        trainer.get_base_model()
        trainer.train_valid_generator()
        trainer.train(callbacks_list)


if __name__ == '__main__':
    try:
        logger.info(f'Starting {STAGE_NAME} stage of pipeline')
        trainer_pipeline_obj = ModelTrainingPipeline()
        trainer_pipeline_obj.main()
        logger.info(f'{STAGE_NAME} finished successfully')
    except Exception as e:
        logger.exception(e)
        raise e
