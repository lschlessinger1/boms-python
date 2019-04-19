from model_spaces.core.covariance_grammar import CovarianceGrammar


class BomsGrammarTraversal(CovarianceGrammar):

    def __init__(self, base_kernels_names, dimension, hyperprior):
        super().__init__(base_kernels_names, dimension, hyperprior)
        self.random_walk_geometric_dist_parameter = 1 / 3
        self.number_of_top_k_best = 3
        self.number_of_random_walks = 15

    def get_candidates(self, selected_models, fitness_score):
        pass

    def expand_random(self, total_num_walks):
        pass

    def expand_best(self, selected_models, fitness_score):
        pass
