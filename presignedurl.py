import boto3
import requests




s3_con = boto3.client(
    's3',aws_access_key_id='AKIAYDLWHHPEULLVNYPP', aws_secret_access_key='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',
)
url = s3_con.generate_presigned_url(
    'put_object', Params={
        'Bucket':'vvdnbucket1', 
        'Key':"application/pdf",'ContentType':'application/pdf'
    },
    ExpiresIn=3600,
    HttpMethod='PUT'
)
print(url)
print s3_con.meta.endpoint_url

url = '{}/{}/{}'.format(s3_con.meta.endpoint_url, 'vvdnbucket1', "contrctsdata.txt")
print url




