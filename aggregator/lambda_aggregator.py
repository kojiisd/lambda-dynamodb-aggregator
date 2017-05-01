class LambdaAggregator(object):
    def __init__(self):
        raise NotImplementedError

    def aggregate(self, data, params):
        raise NotImplementedError

    def check_params(self, params):
        raise NotImplementedError