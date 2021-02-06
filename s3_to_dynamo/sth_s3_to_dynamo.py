import boto3
import ujson

s3_client = boto3.client('s3')
dynamo_client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    json_file_name = event["Records"][0]["s3"]["object"]["key"]
    print(bucket_name)
    print(json_file_name)
    
    json_object = s3_client.get_object(Bucket=bucket_name, Key=json_file_name)
    json_file = json_object["Body"].read()
    read_json = ujson.loads(json_file)
    print(read_json)
    
    table = dynamo_client.Table("hash_lookup")
    
    for i in read_json:
        table.put_item(Item=i)
    
    return {
        'statusCode': 200,
        'body': ujson.dumps(event)
    }
