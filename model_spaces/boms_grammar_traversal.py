from typing import List

import numpy as np

from model_spaces.core.covariance import Covariance
from model_spaces.core.covariance_grammar import CovarianceGrammar
from model_spaces.core.gp_model import GPModel
from model_spaces.core.hyperpriors import Hyperpriors


class BomsGrammarTraversal(CovarianceGrammar):
    random_walk_geometric_dist_parameter: float
    number_of_top_k_best: int
    number_of_random_walks: int

    def __init__(self,
                 base_kernels_names: List[str],
                 dimension: int,
                 hyperprior: Hyperpriors):
        super().__init__(base_kernels_names, dimension, hyperprior)
        self.random_walk_geometric_dist_parameter = 1 / 3
        self.number_of_top_k_best = 3
        self.number_of_random_walks = 15

    def get_candidates(self, selected_models: List[GPModel], fitness_score: List[float]) -> List[Covariance]:
        # exploration
        total_num_walks = self.number_of_random_walks
        candidates_random = self.expand_random(total_num_walks)

        # exploitation
        candidates_best = self.expand_best(selected_models, fitness_score)

        # concatenate
        candidates = candidates_best + candidates_random
        return candidates

    def expand_random(self, total_num_walks: int) -> List[Covariance]:
        parameter = self.random_walk_geometric_dist_parameter
        new_kernels = []
        for i in range(total_num_walks):
            frontier = self.base_kernels
            depth = np.random.geometric(parameter)
            new_kernel = None
            while depth >= 0:
                new_kernel = np.random.choice(frontier)
                frontier = self.expand(new_kernel)
                depth -= 1
            new_kernels.append(new_kernel)

        return new_kernels

    def expand_best(self, selected_models: List[GPModel], fitness_score: List[float]) -> List[Covariance]:
        new_kernels = []
        num_exploit_top = self.number_of_top_k_best
        if len(fitness_score) < 2:
            return new_kernels

        indices = np.argsort(fitness_score)[::-1]
        last_index = min(num_exploit_top, len(fitness_score))
        indices = indices[:last_index]

        models_with_highest_score = [selected_models[i] for i in indices]
        for model in models_with_highest_score:
            kernel_to_expand = model.covariance
            new_kernel_list = self.expand(kernel_to_expand)
            new_kernels += new_kernel_list

        return new_kernels
