from typing import Optional, List, Callable

from numpy import ndarray

from model_spaces.core.hyperpriors import Hyperpriors


class Problem:

    def __init__(self,
                 budget: int,
                 verbose: Optional[bool] = None):
        self.budget = budget
        self.verbose = verbose


class BomsProblem(Problem):

    def __init__(self,
                 budget: int,
                 base_kernel_names: List[str],
                 num_dimensions: int,
                 data_X: ndarray,
                 hyperpriors_lowlevel: Optional[Hyperpriors],
                 initial_level_depth: Optional[int],
                 max_number_of_initial_models: Optional[int],
                 max_num_kernels: Optional[int],
                 acquisition_function: Optional[Callable],
                 hyperpriors_kernel_kernel: Optional[Hyperpriors],
                 num_samples: Optional[int],
                 max_num_hyperparameters: Optional[int],
                 verbose: Optional[bool] = None):
        super().__init__(budget, verbose)
        self.base_kernel_names = base_kernel_names
        self.num_dimensions = num_dimensions
        self.data_X = data_X
        self.hyperpriors_lowlevel = hyperpriors_lowlevel
        self.initial_level_depth = initial_level_depth
        self.max_number_of_initial_models = max_number_of_initial_models
        self.max_num_kernels = max_num_kernels
        self.acquisition_function = acquisition_function
        self.hyperpriors_kernel_kernel = hyperpriors_kernel_kernel
        self.num_samples = num_samples
        self.max_num_hyperparameters = max_num_hyperparameters
