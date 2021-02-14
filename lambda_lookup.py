import boto3

dynamo_client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    body = event["Hash"]

    table = dynamo_client.Table("hash_lookup")
    
    # For every hash given to us
    # Calculate the plaintext and reutrn it
    response = {}
    for i in body:
        data = (table.get_item(Key={"Hash": i}))
        if not "Item" in data:
            continue
        data = data["Item"]
        if not data["Verified"]:
            # Updates it if it's not verifie
            non_verified = update_non_verified(data)
            table.put_item(Item=non_verified)
            # Remove TTL and Uses from data
        if "Uses" in data:
            data["Uses"] = data["Uses"] + 1
        else:
            data["Uses"] = 1
        data["Plaintext"] = data["Plaintext"].strip()
        table.put_item(Item=data)
        data = remove_info(data)
            
        response[i] = data
    
    return {
        'statusCode': 200,
        'body': response
    }

def update_non_verified(row):
    # If used 5 times
    if row["Uses"] >= 5:
        # Don't delete from DB
        if "TTL" in row:
            del row["TTL"]
    return row
    
def remove_info(row):
    if "TTL" in row:
        del row["TTL"]
    if "Uses" in row:
        del row["Uses"]
    return row