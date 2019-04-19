from strategies.bayesian_optimization_strategy import BayesianOptimizationStrategy


class SimpleTracker:

    def callback(self,
                 boms_strategy: BayesianOptimizationStrategy,
                 problem,
                 candidate_models,
                 selected_models,
                 fitness_scores,
                 new_candidates_indices,
                 k,
                 all_candidate_indices,
                 x_train,
                 y_train,
                 acquisition_function_values,
                 next_model_index: int) -> None:
        pass
