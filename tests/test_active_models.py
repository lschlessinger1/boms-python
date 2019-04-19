from unittest import TestCase


class ActiveModelsTest(TestCase):

    def __init__(self, candidates, expected_candidate, expected_status):
        super().__init__()
        self.candidates = candidates
        self.expected_candidate = expected_candidate
        self.expected_status = expected_status

    def setUpClass(cls) -> None:
        cls.candidate_options = {'small', 'repeated', 'multi'}
        cls.active_set_options = {'empty', 'collision'}

    def setUp(self) -> None:
        pass

    def test_create_active_models(self):
        pass

    def test_update(self, candidate_options):
        pass

    def test_add_model(self, candidate_options):
        pass

    def test_remove_from_map(self, candidate_options):
        pass

    def test_get_model_by_covariance(self, candidate_options):
        pass

    def test_collision(self, candidate_options):
        pass
