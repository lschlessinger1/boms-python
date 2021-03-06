from typing import List

from numpy import ndarray

from model_spaces.core.covariance import Covariance
from strategies.boms.active_models import ActiveModels
from strategies.boms.distance_builder import DistanceBuilder


class FrobeniousDistanceBuilder(DistanceBuilder):
    """FrobeniousDistanceBuilder builds distances based on the Frobenious norm between the model's Gram matrices."""
    def __init__(self,
                 noise_prior,
                 num_samples: int,
                 max_num_hyperparameters: int,
                 max_num_kernels: int,
                 active_models: ActiveModels,
                 initial_model_indices,
                 data_X: ndarray):
        super().__init__(noise_prior, num_samples, max_num_hyperparameters, max_num_kernels, active_models,
                         initial_model_indices, data_X)

    def compute_distance(self,
                         active_models: ActiveModels,
                         indices_i: List[int],
                         indices_j: List[int]) -> None:
        pass

    def create_precomputed_info(self,
                                covariance: Covariance,
                                data_X: ndarray) -> ndarray:
        pass


def frobenious_distance(a: ndarray,
                        b: ndarray,
                        num_points: int) -> float:
    """Average squared Frobenius distance between A vs B.

    :param a:
    :param b:
    :param num_points:
    :return:
    """
    pass
