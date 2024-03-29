import logging
from google.cloud import storage, bigquery
import requests
import json
import pandas as pd
import datetime

log = "info.log"
logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y%m%d%H")
current_date = datetime.date.today()
formatted_date = current_date.strftime(("%Y%m%d"))


def upload_blob(source_file_name,bucket_name,  destination_blob_name,path_to_keys):
    """Uploads a file to the bucket."""
    storage_client = storage.Client.from_service_account_json(path_to_keys)
    bucket = storage_client.get_bucket(bucket_name)
    
    # Include the folder in the destination_blob_name
    blob = bucket.blob(formatted_date+'/'+ destination_blob_name + '-' + formatted_datetime + '.csv')

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

def get_data():
  url = 'https://www.predictit.org/api/marketdata/all/'
  r = requests.get(url)
  data = json.loads(r.content)

  contracts = pd.DataFrame()
  markets  = pd.DataFrame()

  for l in data.values():
    for i in l:
      for contract in i['contracts']:
        contract['market_id'] = i['id']
        contract_dict = pd.DataFrame([contract])
        contracts = pd.concat([contracts, contract_dict], ignore_index=True)
        #need to add currentdate to contract
      i.pop('contracts', None)
      market  =  pd.DataFrame([i])
      markets = pd.concat([markets, market], ignore_index=True)

  contracts.to_csv('contracts.csv', encoding='utf-8', index=False)
  logging.info('Contracts.csv downloaded.')
  markets.to_csv('markets.csv', encoding='utf-8', index=False)
  logging.info('Markets.csv downloaded')
from google.cloud import bigquery

def upload_csv_to_bigquery(folder_name, file_name, project_name, dataset_name, table_name, bucket_name, path_to_keys, schema):
    # Initialize BigQuery client
    client = bigquery.Client.from_service_account_json(path_to_keys)
    
    # Construct Cloud Storage URI
    uri = f'gs://{bucket_name}/{folder_name}/{file_name}'
    
    # Construct a reference to the destination table
    table_ref = client.dataset(dataset_name, project=project_name).table(table_name)

    # Configure the job to append to the table
    job_config = bigquery.LoadJobConfig(
        schema=schema,  # Specify schema here
        source_format=bigquery.SourceFormat.CSV,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        skip_leading_rows=1,  # If CSV has headers
        autodetect=False       # Disable autodetect to use provided schema
    )

    # Load data from Cloud Storage into BigQuery
    job = client.load_table_from_uri(uri, table_ref, job_config=job_config)

    # Wait for the job to complete
    job.result()

    return f'Successfully uploaded {file_name} to BigQuery table {table_name} in dataset {dataset_name}.'

from google.cloud import bigquery

def execute_query(query, project_name, path_to_keys):
    # Initialize BigQuery client with service account credentials and project
    client = bigquery.Client.from_service_account_json(path_to_keys, project=project_name)
    
    # Execute the query
    query_job = client.query(query)
    
    # Wait for the query to complete
    query_job.result()
    
    # Return the results (optional)
    return query_job.to_dataframe()  # Convert query results to a DataFrame
