from typing import Callable

from model_spaces.core.gp_model import GPModel
from strategies.boms.active_models import ActiveModels
from strategies.boms.distance_builder import DistanceBuilder
from strategies.boms.kernel_kernel_gp_model import KernelKernelGPModel
from strategies.boms.simple_tracker import SimpleTracker


class BayesianOptimizationStrategy:
    model: GPModel

    def __init__(self,
                 active_models: ActiveModels,
                 acquisition_function: Callable,
                 kernel_builder: DistanceBuilder,
                 kernel_kernel_hyperpriors,
                 tracker: SimpleTracker):
        self.active_models = active_models
        self.acquisition_function = acquisition_function
        self.kernel_builder = kernel_builder
        self.model = KernelKernelGPModel(kernel_kernel_hyperpriors)
        self.tracker = tracker

    def query(self, problem, selected_models, fitness_scores, candidate_models):
        pass
