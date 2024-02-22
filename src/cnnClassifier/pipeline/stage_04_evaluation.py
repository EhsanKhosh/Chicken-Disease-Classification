from cnnClassifier import logger
from cnnClassifier.components.evaluator import Evaluation
from cnnClassifier.config.configuration import ConfigurationManager

STAGE_NAME = "Evaluation"


class EvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluator = Evaluation(eval_config)
        evaluator.evaluation()
        evaluator.save_score()


if __name__ == "__main__":
    try:
        logger.info("*" * 20)
        logger.info(f"Starting {STAGE_NAME} stage of pipeline")
        evaluation_training_pipeline = EvaluationTrainingPipeline()
        evaluation_training_pipeline.main()
        logger.info(f"{STAGE_NAME} finished successfully")

    except Exception as e:
        logger.exception(e)
        raise e
