from unittest import TestCase


class DistanceBuilderTest(TestCase):

    def __init__(self, active_models, candidates, model_space, noise_prior, initial_model_indices, data_X):
        super().__init__()
        self.active_models = active_models
        self.candidates = candidates
        self.model_space = model_space
        self.noise_prior = noise_prior
        self.initial_model_indices = initial_model_indices
        self.data_X = data_X

    @classmethod
    def setUpClass(cls) -> None:
        cls.max_num_kernels = 20
        cls.max_num_hyperparameters = 10
        cls.num_samples = 10
        cls.num_dimensions = 1

    def update_test(self, builder):
        pass

    def distance_builder_test(self, builder, class_name):
        pass

    def compute_distance_test(self, builder, distance_function):
        pass
