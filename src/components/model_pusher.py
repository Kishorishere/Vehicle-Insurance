import shutil
import os
from src.entity.artifact_entity import ModelEvaluationArtifact, ModelPusherArtifact
from src.entity.config_entity import ModelPusherConfig
from src.logger import logging
from src.exception import MyException
import sys

class ModelPusher:
    def __init__(self, model_evaluation_artifact: ModelEvaluationArtifact, model_pusher_config: ModelPusherConfig):
        try:
            self.model_evaluation_artifact = model_evaluation_artifact
            self.model_pusher_config = model_pusher_config
            self.model_store_path = self.model_pusher_config.model_store_path
            os.makedirs(os.path.dirname(self.model_store_path), exist_ok=True)
        except Exception as e:
            raise MyException(e, sys)

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        try:
            if not self.model_evaluation_artifact.is_model_accepted:
                logging.info("New model is not better. Keeping the existing model.")
                return ModelPusherArtifact(model_pushed=False, model_path=None)

            trained_model_path = self.model_evaluation_artifact.trained_model_path
            
            if os.path.exists(self.model_store_path):
                logging.info(f"Replacing existing model at {self.model_store_path} with new model.")
            else:
                logging.info("No existing model found. Saving the new model.")
            
            shutil.copy(trained_model_path, self.model_store_path)
            logging.info(f"Model pushed to {self.model_store_path}")
            return ModelPusherArtifact(model_pushed=True, model_path=self.model_store_path)
        
        except Exception as e:
            raise MyException(e, sys)
