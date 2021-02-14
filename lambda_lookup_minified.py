C='TTL'
B='Uses'
import boto3
F=boto3.resource('dynamodb')
def A(event,context):
	M='Plaintext';L='Item';K='Hash';I=event[K];C=F.Table('hash_lookup');D={}
	for E in I:
		A=C.get_item(Key={K:E})
		if not L in A:continue
		A=A[L]
		if not A['Verified']:J=G(A);C.put_item(Item=J)
		if B in A:A[B]=A[B]+1
		else:A[B]=1
		A[M]=A[M].strip();C.put_item(Item=A);A=H(A);D[E]=A
	return{'statusCode':200,'body':D}
def G(row):
	A=row
	if A[B]>=5:
		if C in A:del A[C]
	return A
def H(row):
	A=row
	if C in A:del A[C]
	if B in A:del A[B]
	return A