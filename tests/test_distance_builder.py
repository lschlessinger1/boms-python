from unittest import TestCase


class DistanceBuilderTest(TestCase):

    def __init__(self):
        super().__init__()
        self.active_models = None
        self.candidates = None
        self.model_space = None
        self.noise_prior = None
        self.initial_model_indices = None
        self.data_X = None
        self.max_num_kernels = 20
        self.max_num_hyperparameters = 10
        self.num_samples = 10
        self.num_dimensions = 1

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def update_test(self, builder):
        pass

    def distance_builder_test(self, builder, class_name):
        pass

    def compute_distance_test(self, builder, distance_function):
        pass
