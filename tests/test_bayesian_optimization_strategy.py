from unittest import TestCase


class BayesianOptimizationStrategyTest(TestCase):

    def __init__(self):
        super().__init__()
        self.problems = None
        self.options = {'small_oneD', 'larger_oneD', 'small_multiD', 'larger_multiD'}

    def setUp(self) -> None:
        pass

    def test_create(self, options):
        pass

    def test_query_empty_candidates(self, options):
        pass

    def test_query_duplicate_candidates(self, options):
        pass

    @staticmethod
    def create_boms(num_points, num_dimensions, base_kernels_names, max_num_kernels, max_num_hyperparameters,
                    num_samples):
        pass
