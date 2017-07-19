import sys
import boto3
import json
import decimal
import os
from boto3.dynamodb.conditions import Key

from aggregator.lambda_aggregator import LambdaAggregator
from aggregator.latest_aggregator import LatestAggregator
from aggregator.max_aggregator import MaxAggregator
from aggregator.min_aggregator import MinAggregator
from aggregator.sum_aggregator import SumAggregator
from aggregator.avg_aggregator import AvgAggregator
from aggregator.count_aggregator import CountAggregator

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table(os.environ['TABLE'])

aggregator_map = {}
aggregator_map['latest'] = LatestAggregator()
aggregator_map['max'] = MaxAggregator()
aggregator_map['min'] = MinAggregator()
aggregator_map['sum'] = SumAggregator()
aggregator_map['avg'] = AvgAggregator()
aggregator_map['count'] = CountAggregator()

def run(event, context):
    check_params(event)
    result = []
    
    for id in event['id']:
        res = table.query(
                KeyConditionExpression=Key(event['label_id']).eq(id) & Key(event['label_range']).between(event['time_from'], event['time_to']),
                ScanIndexForward=False
            )

        return_response = aggregator_map[event['aggregator']].aggregate(res['Items'], event['params'])
        result.append(return_response)

    return json.dumps(result, default=decimal_default)

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

def check_params(params):
    if 'label_id' not in params or 'label_range' not in params or 'id' not in params or 'aggregator' not in params or 'time_from' not in params or 'time_to' not in params or 'params' not in params:
        sys.stderr.write("Parameters for label_id, label_range, id, aggregator, time_from, time_to and params are needed.")
        sys.exit()