from tests.test_distance_builder import DistanceBuilderTest


class HellingerDistanceBuilderTest(DistanceBuilderTest):

    def __init__(self, active_models, candidates, model_space, noise_prior, initial_model_indices, data_X,
                 distance_builder):
        super().__init__(active_models, candidates, model_space, noise_prior, initial_model_indices, data_X)
        self.distance_builder = distance_builder

    def setUp(self) -> None:
        pass

    def test_update(self):
        pass

    def test_test_create_precomputed_info(self):
        pass

    def test_distance_builder(self):
        pass

    def test_test_compute_distance(self):
        pass
