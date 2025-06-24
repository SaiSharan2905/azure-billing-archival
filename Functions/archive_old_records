from azure.cosmos import CosmosClient
from azure.storage.blob import BlobServiceClient
from datetime import datetime, timedelta
import json, os

COSMOS_URI = os.environ['COSMOS_URI']
COSMOS_KEY = os.environ['COSMOS_KEY']
COSMOS_DB = 'BillingDB'
COSMOS_CONTAINER = 'BillingRecords'

BLOB_CONN_STR = os.environ['BLOB_CONN_STR']
BLOB_CONTAINER = 'archived-billing-records'

client = CosmosClient(COSMOS_URI, credential=COSMOS_KEY)
container = client.get_database_client(COSMOS_DB).get_container_client(COSMOS_CONTAINER)

blob_service = BlobServiceClient.from_connection_string(BLOB_CONN_STR)
blob_client = blob_service.get_container_client(BLOB_CONTAINER)

def archive_old_records():
    cutoff = (datetime.utcnow() - timedelta(days=90)).isoformat()
    query = f"SELECT * FROM c WHERE c.billingDate < '{cutoff}'"
    records = list(container.query_items(query=query, enable_cross_partition_query=True))

    if not records:
        return

    file_name = f"archive_{datetime.utcnow().isoformat()}.json"
    blob_client.upload_blob(name=file_name, data=json.dumps(records), overwrite=True)

    for record in records:
        container.delete_item(item=record['id'], partition_key=record['customerId'])
