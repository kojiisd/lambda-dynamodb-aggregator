import sys
from lambda_aggregator import LambdaAggregator

class MinAggregator(LambdaAggregator):
    def __init__(self):
        pass

    def aggregate(self, data, params):
        self.check_params(params)

        return_response = min(data, key=lambda x: x[params['score']])
        return return_response

    
    def check_params(self, params):
        if 'score' not in params:
            sys.stderr.write("score key is necessary for min aggregator.")
            sys.exit()