from unittest import TestCase

from math import log


class TestHyperpriors(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.length_scale_mean_value = log(0.1)
        cls.length_scale_var_value = 1
        cls.output_scale_mean_value = log(0.4)
        cls.output_scale_var_value = 1
        cls.p_length_scale_mean_value = log(2)
        cls.p_length_scale_var_value = 0.5
        cls.p_mean_value = log(0.1)
        cls.p_var_value = 0.5
        cls.alpha_mean_value = log(0.05)
        cls.alpha_var_value = 0.5
        cls.lik_noise_std_mean_value = log(0.01)
        cls.lik_noise_std_var_value = 1
        cls.mean_offset_value = 0
        cls.mean_offset_var_value = 1

    def test_constructor_default_parameters(self):
        pass

    def test_constructor_default_parameters_data_noise(self):
        pass

    def test_gaussian_prior_method(self):
        pass
