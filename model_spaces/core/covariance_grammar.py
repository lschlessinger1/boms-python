from typing import List, Optional

from model_spaces.core.covariance import Covariance
from model_spaces.core.hyperpriors import Hyperpriors


class CovarianceGrammar:

    def __init__(self,
                 base_kernels_names: List[str],
                 dimension: int,
                 hyperprior: Optional[Hyperpriors] = None):
        if hyperprior is None:
            hyperprior = Hyperpriors()

        assert isinstance(hyperprior, Hyperpriors)

        n = len(base_kernels_names)
        base_kernels = []
        for name in base_kernels_names:
            base_kernels.append(Covariance.str2covariance(name, hyperprior))

        if dimension > 1:
            new_base_kernels = []
            new_base_kernels_names = []
            c = 0
            for i in range(n):
                for j in range(dimension):
                    new_base_kernels.append(base_kernels[i].mask(j))
                    new_base_kernels_names.append(new_base_kernels[c].name)
                    c += 1
            base_kernels = new_base_kernels
            base_kernels_names = new_base_kernels_names

        self.dimension = dimension
        self.hyperpriors = hyperprior
        self.base_kernels_names = base_kernels_names
        self.base_kernels = base_kernels

    def expand(self, kernel: Covariance) -> List[Covariance]:
        number_of_base_kernels = len(self.base_kernels)
        new_kernels = []

        for i in range(number_of_base_kernels):
            new_kernels.append(kernel + self.base_kernels[i])
            new_kernels.append(kernel * self.base_kernels[i])
        return new_kernels

    def full_expand(self, level: int,
                    max_number_of_models: int) -> List[Covariance]:
        pass
