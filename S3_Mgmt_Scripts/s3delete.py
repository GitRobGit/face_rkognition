import boto3    

s3 = boto3.resource('s3')
bucket = s3.Bucket('checkingbuckgh')
bucket.delete()
