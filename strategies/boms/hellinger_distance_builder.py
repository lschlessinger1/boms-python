from strategies.boms.distance_builder import DistanceBuilder


class HellingerDistanceBuilder(DistanceBuilder):

    def __init__(self, noise_prior, num_samples, max_num_hyperparameters, max_num_kernels, active_models,
                 initial_model_indices, data_X):
        super().__init__(noise_prior, num_samples, max_num_hyperparameters, max_num_kernels, active_models,
                         initial_model_indices, data_X)

    @staticmethod
    def hellinger_distance(data_i, data_j):
        pass

    def compute_distance(self, active_models, indices_i, indices_j):
        pass

    def create_precomputed_info(self, covariance, data_X):
        pass
