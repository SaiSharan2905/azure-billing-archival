from azure.storage.blob import BlobServiceClient
import json, os

BLOB_CONN_STR = os.environ['BLOB_CONN_STR']
BLOB_CONTAINER = 'archived-billing-records'

blob_service = BlobServiceClient.from_connection_string(BLOB_CONN_STR)
blob_client = blob_service.get_container_client(BLOB_CONTAINER)

def search_archived_record(record_id):
    for blob in blob_client.list_blobs():
        data = json.loads(blob_client.download_blob(blob.name).readall())
        for record in data:
            if record['id'] == record_id:
                return record
    return None
