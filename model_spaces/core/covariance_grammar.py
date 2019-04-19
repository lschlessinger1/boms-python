from typing import List

from model_spaces.core.covariance import Covariance
from model_spaces.core.hyperpriors import Hyperpriors


class CovarianceGrammar:

    def __init__(self,
                 base_kernels_names: List[str],
                 dimension: int,
                 hyperprior: Hyperpriors):
        pass

    def expand(self, kernel: Covariance) -> List[Covariance]:
        pass

    def full_expand(self, level: int,
                    max_number_of_models: int) -> List[Covariance]:
        pass
