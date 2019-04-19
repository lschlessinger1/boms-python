from math import log


class Hyperpriors:

    def __init__(self, data_noise: float = 0.01):
        self.length_scale_mean = log(0.1)
        self.length_scale_var = 1

        self.output_scale_mean = log(0.4)
        self.output_scale_var = 1

        self.p_length_scale_mean = log(2)
        self.p_length_scale_var = 0.5

        self.p_mean = log(0.1)
        self.p_var = 0.5

        self.alpha_mean = log(0.05)
        self.alpha_var = 0.5

        self.lik_noise_std_mean = log(data_noise)
        self.lik_noise_std_var = 1

        self.mean_offset_mean = 0
        self.mean_offset_var = 1

    def gaussian_prior(self, hyperparameter_name):
        pass
