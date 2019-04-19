from typing import List

from numpy import ndarray

from model_spaces.core.covariance import Covariance
from model_spaces.core.gp_model import GPModel
from strategies.bayesian_optimization_strategy import BayesianOptimizationStrategy


class SimpleTracker:

    def callback(self,
                 boms_strategy: BayesianOptimizationStrategy,
                 problem,
                 candidate_models: List[Covariance],
                 selected_models: List[GPModel],
                 fitness_scores: List[float],
                 new_candidates_indices: List[int],
                 k: ndarray,
                 all_candidate_indices: List[int],
                 x_train: ndarray,
                 y_train: ndarray,
                 acquisition_function_values: List[float],
                 next_model_index: int) -> None:
        pass
