from cnnClassifier.entity.config_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path


class Trainer:
    def __init__(self, config: TrainingConfig):
        self.validation_steps = None
        self.step_per_epochs = None
        self.train_generator = None
        self.valid_data_generator = None
        self.model = None
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

    def train_valid_generator(self):
        data_generator_kwargs = dict(
            rescale=1. / 255,
            validation_split=0.2
        )
        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation='bilinear'
        )
        valid_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )
        self.valid_data_generator = valid_data_generator.flow_from_directory(
            directory=self.config.training_data_path,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )
        if self.config.params_is_augmented:
            train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **data_generator_kwargs
            )
        else:
            train_datagen = valid_data_generator

        self.train_generator = train_datagen.flow_from_directory(
            directory=self.config.training_data_path,
            subset='training',
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train(self, callbacks_list: list):
        self.step_per_epochs = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_data_generator.samples // self.valid_data_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            callbacks=callbacks_list,
            steps_per_epoch=self.step_per_epochs,
            validation_steps=self.validation_steps,
            validation_data=self.valid_data_generator
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )
