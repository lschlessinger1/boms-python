from typing import List, Tuple

from model_spaces.core.covariance import Covariance
from strategies.boms.covariance_node import CovarianceNode


class ActiveModels:
    """ActiveModels manages the active set of models."""

    def __init__(self, max_number_of_models: int):
        pass

    def update(self, candidates: List[Covariance]):
        pass

    def add_model(self, covariance: Covariance) -> tuple:
        pass

    def get_index_to_insert(self) -> int:
        pass

    def add_to_map(self, key: str, id_: int) -> None:
        pass

    def remove_from_map(self, id_: int, **kwargs) -> CovarianceNode:
        pass

    def get_model_by_covariance(self,
                                covariance: Covariance,
                                **kwargs) -> Tuple[CovarianceNode, str, int]:
        pass
