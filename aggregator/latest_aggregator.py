import sys
import dateutil.parser as dp
import time

from lambda_aggregator import LambdaAggregator

class LatestAggregator(LambdaAggregator):
    def __init__(self):
        pass

    def aggregate(self, data, params):
        self.check_params(params)

        return_response = max(data, key=(lambda x:(time.mktime(dp.parse(x[params['range']]).timetuple()) * 1000 + dp.parse(x[params['range']]).microsecond)))
        return return_response
    
    def check_params(self, params):
        if 'range' not in params:
            sys.stderr.write("range key is necessary for latest aggregator.")
            sys.exit()
