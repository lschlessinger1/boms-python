from collections import defaultdict
from time import time
from typing import Callable, Tuple, List, DefaultDict, Optional

from model_spaces.core.covariance_grammar import CovarianceGrammar
from model_spaces.core.gp_model import GPModel
from strategies.bayesian_optimization_strategy import BayesianOptimizationStrategy


class ModelSelector:

    def __init__(self,
                 problem: dict,
                 model_space: CovarianceGrammar,
                 fitness_function: Callable[..., float],
                 strategy: BayesianOptimizationStrategy,
                 callback: Optional[Callable] = None):
        self.problem = problem
        self.model_space = model_space
        self.fitness_function = fitness_function
        self.strategy = strategy
        self.callback = callback

    def run(self) -> Tuple[List[GPModel], List[float], DefaultDict[list]]:
        verbose = 'verbose' in self.problem and self.problem['verbose']
        self.problem['verbose'] = verbose

        # Save the wall-clock time of each operation.
        total_time_model_space = []
        total_time_strategy = []
        total_time_fitness = []

        selected_models, fitness_scores = self.initialization()

        for i in range(self.problem['budget']):
            # Get list of candidate models.
            t_start_model_space = time()
            candidate_models = self.model_space.get_candidates(selected_models, fitness_scores)
            time_model_space = time() - t_start_model_space
            total_time_model_space.append(time_model_space)

            # Select next model to evaluate.
            t_start_strategy = time()
            chosen_model = self.strategy.query(self.problem, selected_models, fitness_scores, candidate_models)
            time_strategy = time() - t_start_strategy
            total_time_strategy.append(time_strategy)

            # Observe the fitness score of the chosen model.
            t_start_fitness = time()
            chosen_model_fitness = self.fitness_function(self.problem, chosen_model)
            time_fitness = time() - t_start_fitness
            total_time_fitness.append(time_fitness)

            # Update data.
            selected_models = selected_models, chosen_model
            fitness_scores = fitness_scores, chosen_model_fitness

            if self.callback is not None:
                self.callback(self, selected_models, fitness_scores, i)

        times = defaultdict(list)
        times['total_time_model_space'] = total_time_model_space
        times['total_time_strategy'] = total_time_strategy
        times['total_time_oracle'] = total_time_fitness

        return selected_models, fitness_scores, times

    def initialization(self) -> Tuple[List[GPModel], List[float]]:
        raise NotImplementedError
