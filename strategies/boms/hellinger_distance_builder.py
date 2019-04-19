from typing import Tuple, List

from numpy import ndarray

from model_spaces.core.covariance import Covariance
from strategies.boms.active_models import ActiveModels
from strategies.boms.distance_builder import DistanceBuilder

PrecomputedInfo = Tuple[ndarray, ndarray]


class HellingerDistanceBuilder(DistanceBuilder):
    """HellingerDistanceBuilder builds distances based on the Hellinger distance between the model's Gram matrices."""

    def __init__(self,
                 noise_prior,
                 num_samples: int,
                 max_num_hyperparameters: int,
                 max_num_kernels: int,
                 active_models: ActiveModels,
                 initial_model_indices: List[int],
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
                                data_X: ndarray) -> PrecomputedInfo:
        pass


def hellinger_distance(data_i: PrecomputedInfo,
                       data_j: PrecomputedInfo) -> float:
    """Squared Hellinger distance for two multivariate Gaussian distributions with means zero.

    https://en.wikipedia.org/wiki/Hellinger_distance

    :param data_i:
    :param data_j:
    :return:
    """
    pass


def fix_numerical_problem(k: ndarray) -> ndarray:
    pass
