B='TTL'
A='Uses'
import boto3
C=boto3.resource('dynamodb')
def F(event,context):
	F='Item';B='Hash';body=event[B];table=C.Table('hash_lookup');response={}
	for i in body:
		data=table.get_item(Key={B:i})
		if not F in data:continue
		data=data[F]
		if not data['Verified']:non_verified=D(data);table.put_item(Item=non_verified)
		if A in data:data[A]=data[A]+1
		else:data[A]=1
		table.put_item(Item=data);data=E(data);response[i]=data
	return{'statusCode':200,'body':response}
def D(row):
	if row[A]>=5:
		if B in row:del row[B]
	return row
def E(row):
	if B in row:del row[B]
	if A in row:del row[A]
	return row