from google.cloud import bigquery

def upload_to_bigquery(df, table_id, write_disposition="WRITE_TRUNCATE"):
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(write_disposition=write_disposition)
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()
    print(f"Loaded to BigQuery: {table_id}")
