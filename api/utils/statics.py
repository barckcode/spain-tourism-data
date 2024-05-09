import os
import boto3
import pandas as pd
from io import StringIO


AWS_REGION = os.getenv('AWS_DEFAULT_REGION')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')


def load_data_from_s3():
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )
    bucket_name = 'statics.helmcode.com'
    object_key = 'spain-turism-data/api/dev/tourists/10_2015_to_03_2024.csv'
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    data = response['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(data), delimiter=';')
    return df
