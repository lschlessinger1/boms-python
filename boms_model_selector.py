from typing import Callable

from model_selector import ModelSelector
from model_spaces.boms_grammar_traversal import BomsGrammarTraversal
from strategies.bayesian_optimization_strategy import BayesianOptimizationStrategy


class BomsModelSelector(ModelSelector):

    def __init__(self,
                 problem,
                 fitness_function: Callable,
                 callback: Callable):
        BomsModelSelector.default_parameters(problem)
        model_space = BomsGrammarTraversal()
        strategy = BayesianOptimizationStrategy()
        super().__init__(problem, model_space, fitness_function, strategy, callback)

    def initialization(self):
        pass

    @staticmethod
    def default_parameters(problem):
        pass
