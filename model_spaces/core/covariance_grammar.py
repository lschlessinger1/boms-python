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

    def full_expand(self,
                    level: int,
                    max_number_of_models: int) -> List[Covariance]:
        # this is a brute-force implementation, use it for level < 4
        current_kernels = self.base_kernels
        if level == 0:
            return current_kernels

        def remove_duplicates(new_kerns, all_kerns):
            unique_kernels = []
            for new_kernel in new_kerns:
                repeated = False
                for kern in all_kerns:
                    if new_kernel == kern:
                        repeated = True
                        break
                if not repeated:
                    unique_kernels.append(new_kernel)
            return unique_kernels

        all_kernels = []

        while level > 0:
            this_level = []
            number_of_models = len(all_kernels)
            for current_kernel in current_kernels:
                new_kernels = self.expand(current_kernel)
                unique_new_kernels = remove_duplicates(new_kernels, this_level)
                this_level += unique_new_kernels
                number_of_models = number_of_models + len(unique_new_kernels)
                if number_of_models > max_number_of_models:
                    all_kernels += this_level
                    all_kernels = all_kernels[:max_number_of_models]
                    return all_kernels
            current_kernels = this_level
            all_kernels += this_level
            level -= 1
        return all_kernels
