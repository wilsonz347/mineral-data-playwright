from google.cloud import storage
import json

def upload_to_gcs(bucket_name, destination_blob, data):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    blob.upload_from_string(
        json.dumps(data, indent=2),
        content_type="application/json"
    )