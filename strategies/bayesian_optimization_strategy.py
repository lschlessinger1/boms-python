from strategies.boms.kernel_kernel_gp_model import KernelKernelGPModel


class BayesianOptimizationStrategy:

    def __init__(self, active_models, acquisition_function, kernel_builder, kernel_kernel_hyperpriors, tracker):
        self.active_models = active_models
        self.acquisition_function = acquisition_function
        self.kernel_builder = kernel_builder
        self.model = KernelKernelGPModel(kernel_kernel_hyperpriors)
        self.tracker = tracker

    def query(self, problem, selected_models, fitness_scores, candidate_models):
        pass
