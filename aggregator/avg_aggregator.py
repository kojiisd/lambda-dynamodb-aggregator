import sys
from lambda_aggregator import LambdaAggregator

class AvgAggregator(LambdaAggregator):
    def __init__(self):
        pass

    def aggregate(self, data, params):
        self.check_params(params)

        return_response = sum(map(lambda x: x['score'], data)) / len(map(lambda x: x['score'], data))
        return return_response

    
    def check_params(self, params):
        if 'score' not in params:
            sys.stderr.write("score key is necessary for avg aggregator.")
            sys.exit()