from unittest import TestCase


class ActiveModelsTest(TestCase):

    def __init__(self):
        super().__init__()
        self.candidates = None
        self.expected_candidate = None
        self.expected_status = None
        self.candidate_options = {'small', 'repeated', 'multi'}
        self.active_set_options = {'empty', 'collision'}

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
