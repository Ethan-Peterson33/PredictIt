from variables import bucket_name,project_name,dataset_name,path_to_keys,markets_schema,contracts_schema,query
import logging
import requests
import json
import pandas as pd
import datetime
from functions import upload_blob, get_data,upload_csv_to_bigquery,execute_query

log = "info.log"
logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('Log Entry Here.')


current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y%m%d%H")
current_date = datetime.date.today()
formatted_date = current_date.strftime(("%Y%m%d"))


# Get the current date and time


def main():
 # get_data()
 # upload_blob(bucket_name,'contracts.csv','contracts')
 # upload_blob(bucket_name,'markets.csv','markets')
 # upload_blob('contracts.csv',bucket_name,  'contracts',path_to_keys)
 # upload_blob('markets.csv',bucket_name,  'markets',path_to_keys)
 # upload_csv_to_bigquery(formatted_date, f'contracts-{formatted_datetime}.csv',project_name, dataset_name, 'contracts', bucket_name, path_to_keys,contracts_schema)
 # upload_csv_to_bigquery(formatted_date, f'markets-{formatted_datetime}.csv',project_name, dataset_name, 'markets', bucket_name, path_to_keys,markets_schema)
  execute_query(query, project_name,path_to_keys)
if __name__ == '__main__':
  main()