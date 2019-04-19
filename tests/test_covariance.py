from unittest import TestCase


class TestCovariance(TestCase):

    def __init__(self, se, rq):
        super().__init__()
        self.se = se
        self.rq = rq

    def test_create_covariances(self):
        pass

    def test_mask(self):
        pass

    def testCovariance(self):
        pass

    def test_str2covariance(self):
        pass

    @staticmethod
    def test_covariance(test_case, expected_covariance_name, expected_number_of_parameters, is_base_kernel,
                        expected_covariance_function_handle, expected_mean, covariance):
        pass
