from google.cloud import storage, bigquery

bucket_name = 'predictit_data_dezoomcamp'
project_name = 'predict-it-dezoomcamp'
dataset_name = 'PredictIt'
path_to_keys = '../keys/keys.json'



# Define schemas for contracts and markets tables
contracts_schema = [
    bigquery.SchemaField("id", "INTEGER", mode="NULLABLE"),
    bigquery.SchemaField("dateEnd", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("image", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("name", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("shortName", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("status", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("lastTradePrice", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField("bestBuyYesCost", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField("bestBuyNoCost", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField("bestSellYesCost", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField("bestSellNoCost", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField("lastClosePrice", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField("displayOrder", "INTEGER", mode="NULLABLE"),
    bigquery.SchemaField("market_id", "INTEGER", mode="NULLABLE"),
]

markets_schema = [
    bigquery.SchemaField("id", "INTEGER", mode="NULLABLE"),
    bigquery.SchemaField("name", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("shortName", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("image", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("url", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("timeStamp", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("status", "STRING", mode="NULLABLE"),
]


query = """

CREATE OR REPLACE TABLE `predict-it-dezoomcamp.PredictIt.markets_contracts`
AS
SELECT
    market_id,
    market,
    market_name,
    market_image,
    url,
    currentdate,
    timestamp,
    market_status,
    contract_id,
    contract_image,
    contract_name,
    contract_short,
    contract_status,
    lasttradeprice,
    bestbuyyescost,
    bestbuynocost,
    bestsellyescost,
    bestsellnocost,
    lastcloseprice
FROM `predict-it-dezoomcamp.dbt_epeterson.fact_markets_contracts`;


"""