from typing import List

from numpy import ndarray

from model_spaces.core.covariance import Covariance
from strategies.boms.active_models import ActiveModels


class DistanceBuilder:
    """DistanceBuilder Build distance matrix between models."""

    def __init__(self,
                 noise_prior,
                 num_samples: int,
                 max_num_hyperparameters: int,
                 max_num_kernels: int,
                 active_models: ActiveModels,
                 initial_model_indices: List[int],
                 data_X: ndarray):
        pass

    def precompute_information(self,
                               active_models: ActiveModels,
                               new_candidates_indices: List[int],
                               data_X) -> None:
        pass

    def update(self,
               active_models: ActiveModels,
               new_candidates_indices: List[int],
               all_candidates_indices: List[int],
               selected_indices: List[int],
               data_X: ndarray) -> None:
        """Update average distance between models.

        :param active_models:
        :param new_candidates_indices:
        :param all_candidates_indices:
        :param selected_indices:
        :param data_X:
        :return:
        """
        pass

    def compute_distance(self,
                         active_models: ActiveModels,
                         indices_i: List[int],
                         indices_j: List[int]) -> None:
        raise NotImplementedError

    def create_precomputed_info(self,
                                covariance: Covariance,
                                data_X: ndarray):
        raise NotImplementedError

    def get_kernel(self, index: int) -> ndarray:
        pass
