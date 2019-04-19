from model_spaces.core.covariance import Covariance


class CovarianceNode:
    def __init__(self, id_: int, covariance: Covariance):
        self.id_ = id_
        self.covariance = covariance
        self.info = None  # precomputed information for this node

    def set_precomputed_info(self, info):
        self.info = info
