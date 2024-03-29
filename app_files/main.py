from variables import bucket_name,project_name,dataset_name,path_to_keys,markets_schema,contracts_schema,query
import logging
import requests
import json
import pandas as pd
import datetime
from functions import upload_blob, get_data,upload_csv_to_bigquery,execute_query
import datetime
import time

log = "info.log"
logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('New Session.')


current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y%m%d%H")
current_date = datetime.date.today()
formatted_date = current_date.strftime(("%Y%m%d"))


def pipeline():
  print("Pipeline executed at:", datetime.datetime.utcnow())
  get_data()
  upload_blob('contracts.csv',bucket_name,  'contracts',path_to_keys)
  upload_blob('markets.csv',bucket_name,  'markets',path_to_keys)
  print(f"files uploaded to {bucket_name}")
  upload_csv_to_bigquery(formatted_date, f'contracts-{formatted_datetime}.csv',project_name, dataset_name, 'contracts', bucket_name, path_to_keys,contracts_schema)
  upload_csv_to_bigquery(formatted_date, f'markets-{formatted_datetime}.csv',project_name, dataset_name, 'markets', bucket_name, path_to_keys,markets_schema)
  print(f"data uploaded into big query dataset {dataset_name}")
  execute_query(query, project_name,path_to_keys)
  print('inserted new data into main table')

# Define your scheduled execution times
scheduled_time1 = datetime.time(8, 00)  # 8:00 UTC
scheduled_time2 = datetime.time(19, 00)  # 16:00 UTC

def main():
    while True:
        # Get current UTC datetime
        current_datetime = datetime.datetime.utcnow()
        
        # Calculate the datetime for the next scheduled executions
        next_execution1 = datetime.datetime.combine(current_datetime.date(), scheduled_time1)
        next_execution2 = datetime.datetime.combine(current_datetime.date(), scheduled_time2)
        
        # Determine the time until each scheduled execution
        time_until_next_execution1 = (next_execution1 - current_datetime).total_seconds()
        time_until_next_execution2 = (next_execution2 - current_datetime).total_seconds()
        
        # Determine the closest execution time
        if time_until_next_execution1 > 0 and time_until_next_execution1 < time_until_next_execution2:
            next_execution = next_execution1
            time_until_next_execution = time_until_next_execution1
        elif time_until_next_execution2 > 0:
            next_execution = next_execution2
            time_until_next_execution = time_until_next_execution2
        else:
            # Calculate the datetime for the first scheduled execution on the next day
            next_execution = datetime.datetime.combine(current_datetime.date() + datetime.timedelta(days=1), scheduled_time1)
            time_until_next_execution = (next_execution - current_datetime).total_seconds()
        
        # Check if it's time to execute the function
        if time_until_next_execution <= 0:
            pipeline()
        else:
            print("Next execution in:", time_until_next_execution / 3600, "hours")
            # Sleep until the next scheduled time
            time.sleep(max(0, time_until_next_execution))
            pipeline()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
