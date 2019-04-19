class DistanceBuilder:

    def __init__(self, noise_prior, num_samples, max_num_hyperparameters, max_num_kernels, active_models,
                 initial_model_indices, data_X):
        pass

    def precompute_information(self, active_models, new_candidates_indices, data_X):
        pass

    def update(self, active_models, new_candidates_indices, all_candidates_indices, selected_indices, data_X):
        pass

    def compute_distance(self, active_models, indices_i, indices_j):
        raise NotImplementedError

    def create_precomputed_info(self, covariance, data_X):
        raise NotImplementedError
