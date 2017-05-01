import sys
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key

from aggregator.lambda_aggregator import LambdaAggregator
from aggregator.latest_aggregator import LatestAggregator


dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('test')

aggregator_map = {}
aggregator_map['latest'] = LatestAggregator()

def run(event, context):
    check_params(event)

    res = table.query(
            KeyConditionExpression=Key(event['label_id']).eq(event['id'])
        )

    return_response = aggregator_map[event['aggregator']].aggregate(res['Items'], event['params'])

    return json.dumps(return_response, default=decimal_default)

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

def check_params(params):
    if 'label_id' not in params or 'id' not in params or 'aggregator' not in params or 'params' not in params:
        sys.stderr.write("Parameters for label_id, id, aggregator and params are needed.")
        sys.exit()