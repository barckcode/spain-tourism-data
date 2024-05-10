import os
import boto3
import pandas as pd
from pandas.errors import EmptyDataError
from io import StringIO
from fastapi import HTTPException, status


AWS_REGION = os.getenv('AWS_DEFAULT_REGION')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_s3_bucket = os.getenv('AWS_S3_BUCKET')


def load_data_from_s3(object_key: str):
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION
        )
        bucket_name = aws_s3_bucket
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error getting file from S3")

    data = response['Body'].read().decode('utf-8')
    first_line = data.split('\n')[0]
    if ';' not in first_line:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The downloaded file has incorrect format")
    try:
        df = pd.read_csv(StringIO(data), delimiter=';')
        return df
    except EmptyDataError:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="The downloaded file is empty")
