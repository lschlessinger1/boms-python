from typing import List

from model_spaces.core.covariance_grammar import CovarianceGrammar
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

    def get_candidates(self, selected_models, fitness_score):
        pass

    def expand_random(self, total_num_walks: int):
        pass

    def expand_best(self, selected_models, fitness_score):
        pass
