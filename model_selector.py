from collections import defaultdict
from typing import Callable, Tuple, List, DefaultDict

from model_spaces.core.covariance_grammar import CovarianceGrammar
from model_spaces.core.gp_model import GPModel
from strategies.bayesian_optimization_strategy import BayesianOptimizationStrategy


class ModelSelector:

    def __init__(self,
                 problem,
                 model_space: CovarianceGrammar,
                 fitness_function: Callable[..., float],
                 strategy: BayesianOptimizationStrategy,
                 callback: Callable):
        self.problem = problem
        self.model_space = model_space
        self.fitness_function = fitness_function
        self.strategy = strategy
        self.callback = callback
        self.time = defaultdict(float)

    def run(self) -> Tuple[List[GPModel], List[float], DefaultDict[float]]:
        pass

    def initialization(self) -> Tuple[List[GPModel], List[float]]:
        raise NotImplementedError
