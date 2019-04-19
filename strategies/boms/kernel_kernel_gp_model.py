from model_spaces.core.gp_model import GPModel


class KernelKernelGPModel(GPModel):

    def __init__(self, kernel_kernel_hyperpriors):
        covariance = None
        super().__init__(covariance, kernel_kernel_hyperpriors)

    def set_kernel_kernel(self, k):
        pass
