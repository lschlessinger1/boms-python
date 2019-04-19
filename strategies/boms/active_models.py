from model_spaces.core.gp_model import GPModel


class ActiveModels:
    """ActiveModels manages the active set of models."""

    def __init__(self, max_number_of_models: int):
        pass

    def update(self, candidates):
        pass

    def add_model(self, covariance) -> tuple:
        pass

    def get_index_to_insert(self) -> int:
        pass

    def add_to_map(self, key, id_) -> None:
        pass

    def remove_from_map(self, id_, **kwargs) -> GPModel:
        pass

    def get_model_by_covariance(self, covariance, **kwargs) -> tuple:
        pass
