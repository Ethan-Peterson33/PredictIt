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

CREATE TABLE IF NOT EXISTS `predict-it-dezoomcamp.PredictIt.markets_contracts` (
    market_id INTEGER,
    market STRING,
    market_name STRING,
    market_image STRING,
    url STRING,
    currentdate DATE,
    timestamp DATETIME,
    market_status STRING,
    contract_id INTEGER,
    contract_image STRING,
    contract_name STRING,
    contract_short STRING,
    contract_status STRING,
    lasttradeprice FLOAT64,
    bestbuyyescost FLOAT64,
    bestbuynocost FLOAT64,
    bestsellyescost FLOAT64,
    bestsellnocost FLOAT64,
    lastcloseprice FLOAT64
);

INSERT INTO `predict-it-dezoomcamp.PredictIt.markets_contracts` (
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
)
SELECT
    c.market_id,
    m.name AS market,
    m.name AS market_name,
    m.image AS market_image,
    m.url,
    CURRENT_DATE() AS currentdate,
    CAST(PARSE_TIMESTAMP("%Y-%m-%dT%H:%M:%E*S", m.timestamp) AS DATETIME) AS timestamp,
    m.status AS market_status,
    c.id AS contract_id,
    c.image AS contract_image,
    c.name AS contract_name,
    c.shortname AS contract_short,
    c.status AS contract_status,
    c.lasttradeprice,
    c.bestbuyyescost,
    c.bestbuynocost,
    c.bestsellyescost,
    c.bestsellnocost,
    c.lastcloseprice
FROM 
    `predict-it-dezoomcamp.PredictIt.markets` m 
INNER JOIN 
    `predict-it-dezoomcamp.PredictIt.contracts` c ON c.market_id = m.id;

        

"""
