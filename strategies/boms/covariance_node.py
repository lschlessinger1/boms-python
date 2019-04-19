class CovarianceNode:
    def __init__(self, id_, covariance):
        self.id_ = id_
        self.covariance = covariance
        self.info = None

    def set_precomputed_info(self, info):
        self.info = info
