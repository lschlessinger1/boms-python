from strategies.boms.active_models import ActiveModels


class DistanceBuilder:

    def __init__(self,
                 noise_prior,
                 num_samples: int,
                 max_num_hyperparameters: int,
                 max_num_kernels: int,
                 active_models: ActiveModels,
                 initial_model_indices,
                 data_X):
        pass

    def precompute_information(self,
                               active_models: ActiveModels,
                               new_candidates_indices,
                               data_X) -> None:
        pass

    def update(self,
               active_models: ActiveModels,
               new_candidates_indices,
               all_candidates_indices,
               selected_indices,
               data_X) -> None:
        pass

    def compute_distance(self,
                         active_models: ActiveModels,
                         indices_i,
                         indices_j) -> None:
        raise NotImplementedError

    def create_precomputed_info(self, covariance, data_X):
        raise NotImplementedError

    def get_kernel(self, index: int):
        pass
