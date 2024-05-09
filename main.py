import os
import boto3
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO


AWS_REGION = os.getenv('AWS_DEFAULT_REGION')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)
bucket_name = 'statics.helmcode.com'
object_key = 'spain-turism-data/api/dev/tourists/10_2015_to_03_2024.csv'

response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")


if status == 200:
    print("Successful S3 get_object response. Status - {}".format(status))
    data = response['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(data), delimiter=';')

    # Filtra los datos por Comunidad Autónoma, ejemplo: Canarias
    canarias_data = df[df['Comunidades autónomas'].str.contains('Canarias')].copy()
    canarias_data.loc[:, 'Periodo'] = pd.to_datetime(canarias_data['Periodo'], format='%YM%m')
    canarias_data = canarias_data.sort_values('Periodo')
    canarias_data['Total'] = canarias_data['Total'].str.replace('.', '').str.replace(',', '.')
    canarias_data['Total'] = canarias_data['Total'].apply(pd.to_numeric, errors='coerce')
    canarias_data['Total'] = canarias_data['Total'].fillna(0)

    # Crear un gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(canarias_data['Periodo'], canarias_data['Total'], color='blue')
    plt.xlabel('Periodo')
    plt.ylabel('Total de Turistas')
    plt.title('Total de Turistas Visitando Canarias por Año')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Unsuccessful S3 get_object response. Status - {}".format(status))
