import os
import pickle
from src.exception import MyException
from src.logger import logging
import sys

class Proj1Estimator:
    def __init__(self, bucket_name: str, model_path: str):
        """
        Handles model loading and inference, supporting both S3 and local folder storage.
        """
        try:
            self.bucket_name = bucket_name
            self.model_path = model_path
            self.local_s3_path = "s3"  # Local "S3" folder replication

            # If bucket_name is 'local_s3_storage', assume local storage
            if bucket_name == "":
                self.model_full_path = os.path.join(self.local_s3_path, self.model_path)
                if not os.path.exists(self.model_full_path):
                    raise FileNotFoundError(f"Model file not found at {self.model_full_path}")
            else:
                raise NotImplementedError("S3 support not implemented in this local version")

            logging.info(f"Loading model from {self.model_full_path}")
            with open(self.model_full_path, "rb") as model_file:
                self.model = pickle.load(model_file)

        except Exception as e:
            raise MyException(e, sys) from e

    def predict(self, dataframe):
        """
        Predict using the loaded model.
        """
        try:
            if not hasattr(self, "model"):
                raise ValueError("Model is not loaded properly.")
            
            predictions = self.model.predict(dataframe)
            return predictions

        except Exception as e:
            raise MyException(e, sys) from e
