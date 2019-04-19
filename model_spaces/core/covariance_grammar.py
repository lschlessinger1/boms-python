from typing import List


class CovarianceGrammar:

    def __init__(self,
                 base_kernels_names: List[str],
                 dimension: int,
                 hyperprior):
        pass

    def expand(self, kernel):
        pass

    def full_expand(self, level: int,
                    max_number_of_models: int):
        pass
