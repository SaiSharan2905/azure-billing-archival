resource storage 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: 'billingstorageacct'
  location: resourceGroup().location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {}
}

resource functionApp 'Microsoft.Web/sites@2022-03-01' = {
  name: 'billing-archival-func'
  location: resourceGroup().location
  kind: 'functionapp'
  properties: {
    serverFarmId: '/subscriptions/.../serverfarms/YOUR_PLAN'
  }
}
