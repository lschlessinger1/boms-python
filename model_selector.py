from typing import Callable

from model_spaces.core.covariance_grammar import CovarianceGrammar
from strategies.bayesian_optimization_strategy import BayesianOptimizationStrategy


class ModelSelector:

    def __init__(self,
                 problem,
                 model_space: CovarianceGrammar,
                 fitness_function: Callable,
                 strategy: BayesianOptimizationStrategy,
                 callback: Callable):
        self.problem = problem
        self.model_space = model_space
        self.fitness_function = fitness_function
        self.strategy = strategy
        self.callback = callback
        self.time = None

    def run(self):
        pass

    def initialization(self):
        raise NotImplementedError
