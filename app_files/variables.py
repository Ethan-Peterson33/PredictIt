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

insert into predict-it-dezoomcamp.PredictIt.markets_contracts
SELECT
    c.market_id,
    m.name as market,
    m.name as market_name,
    m.image as market_image,
    m.url,
    CURRENT_DATE() AS currentdate,
    cast(PARSE_TIMESTAMP("%Y-%m-%dT%H:%M:%E*S",m.timestamp) AS DATETIME) AS timestamp,  -- Convert TIMESTAMP to DATETIME
    m.status as market_status,
    c.id as contract_id,
    c.image as contract_image,
    c.name as contract_name,
    c.shortname as contract_short,
    c.status as contract_status,
    c.lasttradeprice,
    c.bestbuyyescost,
    c.bestbuynocost,
    c.bestsellyescost,
    c.bestsellnocost,
    c.lastcloseprice
FROM 
    `predict-it-dezoomcamp.PredictIt.markets` m 
INNER JOIN 
    `predict-it-dezoomcamp.PredictIt.contracts` c ON c.market_id = m.id
        

"""
