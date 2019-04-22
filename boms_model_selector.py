from typing import Callable, Optional, List, Tuple

from model_selector import ModelSelector
from model_spaces.boms_grammar_traversal import BomsGrammarTraversal
from model_spaces.core.gp_model import GPModel
from model_spaces.core.hyperpriors import Hyperpriors
from problem import BomsProblem
from score_functions.expected_improvement import expected_improvement
from strategies.bayesian_optimization_strategy import BayesianOptimizationStrategy
from strategies.boms.active_models import ActiveModels
from strategies.boms.hellinger_distance_builder import HellingerDistanceBuilder
from strategies.boms.simple_tracker import SimpleTracker


class BomsModelSelector(ModelSelector):

    def __init__(self,
                 problem: BomsProblem,
                 fitness_function: Callable[..., float],
                 callback: Optional[Callable] = None):
        problem = BomsModelSelector.default_parameters(problem)

        model_space = BomsGrammarTraversal(problem.base_kernel_names, problem.num_dimensions,
                                           problem.hyperpriors_lowlevel)

        initial_candidates = model_space.full_expand(problem.initial_level_depth, problem.max_number_of_initial_models)

        active_models = ActiveModels(problem.max_num_kernels)
        initial_candidate_indices = active_models.update(initial_candidates)

        no_duplicates = len(initial_candidate_indices) == len(initial_candidates)
        assert no_duplicates

        acquisition_function = problem.acquisition_function

        kernel_builder = HellingerDistanceBuilder([problem.hyperpriors_kernel_kernel.gaussian_prior('lik_noise_std')],
                                                  problem.num_samples, problem.max_num_hyperparameters,
                                                  problem.max_num_kernels, active_models, initial_candidate_indices,
                                                  problem.data_X)

        tracker = SimpleTracker()

        strategy = BayesianOptimizationStrategy(active_models, acquisition_function, kernel_builder,
                                                problem.hyperpriors_kernel_kernel, tracker)

        super().__init__(problem, model_space, fitness_function, strategy, callback)

    def initialization(self) -> Tuple[List[GPModel], List[float]]:
        selected_index = 0
        selected_node = self.strategy.active_models.models[selected_index]
        self.strategy.active_models.selected_indices = [selected_index]

        selected_model = GPModel(selected_node.covariance, self.problem.hyperpriors_lowlevel)

        fitness_score = self.fitness_function(self.problem, selected_model)

        selected_models = [selected_model]
        fitness_scores = [fitness_score]
        return selected_models, fitness_scores

    @staticmethod
    def default_parameters(problem: BomsProblem) -> BomsProblem:
        problem.hyperpriors_lowlevel = Hyperpriors()
        problem.hyperpriors_kernel_kernel = Hyperpriors(0.01)

        problem.num_samples = 20
        problem.max_num_hyperparameters = 100
        problem.max_num_kernels = 1000

        problem.acquisition_function = expected_improvement

        problem.initial_level_depth = 2
        problem.max_number_of_initial_models = 500
        problem.random_walk_geometric_dist_parameter = 1 / 3
        problem.number_of_top_k_best = 3
        problem.number_of_random_walks = 15
        return problem
