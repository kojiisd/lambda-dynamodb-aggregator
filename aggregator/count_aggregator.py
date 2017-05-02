import sys
from lambda_aggregator import LambdaAggregator

class CountAggregator(LambdaAggregator):
    def __init__(self):
        pass

    def aggregate(self, data, params):
        self.check_params(params)

        return_response = len(map(lambda x: x['score'], data))
        return return_response

    
    def check_params(self, params):
        if 'score' not in params:
            sys.stderr.write("score key is necessary for count aggregator.")
            sys.exit()