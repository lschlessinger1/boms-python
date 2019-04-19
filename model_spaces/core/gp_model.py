from model_spaces.core.covariance import Covariance
from model_spaces.core.hyperpriors import Hyperpriors


class GPModel:

    def __init__(self, covariance: Covariance, hyperpriors: Hyperpriors):
        pass

    def predict(self, x_train, y_train, x_star) -> tuple:
        pass

    def update(self, x_train, y_train) -> None:
        pass

    def train(self, x_train, y_train) -> None:
        pass

    def log_evidence(self) -> float:
        pass
