from typing import Optional, Callable

from model_spaces.core.hyperpriors import Hyperpriors


class Covariance:
    rnd_code_max_digit = 10
    rnd_code_maximum_length = 16
    rnd_code_truncation = 1e6

    def __init__(self,
                 name: str,
                 is_base: bool,
                 rnd_code,
                 function_handle: Callable,
                 priors):
        self.name = name  # string to represent the model
        self.is_base = is_base  # boolean to define if it is a base covariance
        self.rnd_code = rnd_code  # random numbers to figure out if two models are the same
        self.function_handle = function_handle  # covariance function handle
        self.priors = priors  # covariance prior function handle

    @classmethod
    def mask(cls, o1, dimension: int):
        pass

    def __add__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __eq__(self, other):
        pass

    def get_hyperparameters_sample(self):
        pass

    def is_base_kernel(self):
        pass

    @staticmethod
    def str2covariance(covariance_name: str,
                       hyperpriors: Optional[Hyperpriors] = None,
                       **kwargs):
        pass
