import os
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_dirs
from cnnClassifier.entity.config_entity import (DataIngestionConfig,
                                                PrepareBaseModelConfig,
                                                CallbacksConfig,
                                                TrainingConfig,
                                                EvaluationConfig)


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

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_dirs([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            update_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config

    def get_callbacks_config(self) -> CallbacksConfig:
        config1 = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config1.checkpoint_model_file)
        create_dirs([
            model_ckpt_dir,
            config1.tensorboard_log_dir
        ])
        callbacks_config1 = CallbacksConfig(
            root_dir=Path(config1.root_dir),
            tensorboard_log_dir=Path(config1.tensorboard_log_dir),
            checkpoint_dir=Path(config1.checkpoint_model_file)
        )
        return callbacks_config1

    def get_training_config(self) -> TrainingConfig:
        training_config = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_file, "Chicken-fecal-images")
        create_dirs([training_config.root_dir])

        training_config = TrainingConfig(
            root_dir=training_config.root_dir,
            trained_model_path=Path(training_config.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data_path=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmented=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )
        return training_config

    def get_evaluation_config(self):
        eval_config = EvaluationConfig(
            model_path=Path(self.config.training.trained_model_path),
            training_data=Path('artifacts/data_ingestion/Chicken-fecal-images'),
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config
