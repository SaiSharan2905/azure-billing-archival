def get_billing_record(record_id, customer_id):
    try:
        return cosmos_container.read_item(item=record_id, partition_key=customer_id)
    except:
        for blob in blob_client.list_blobs():
            data = json.loads(blob_client.download_blob(blob.name).readall())
            for record in data:
                if record['id'] == record_id and record['customerId'] == customer_id:
                    return record
        raise Exception('Record not found')
