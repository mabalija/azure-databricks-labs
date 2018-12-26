# azure-databricks labs to access data from Data Lake Storage Gen2 with ABFS driver (Azure Blob FileSystem driver)  
In this lab we will understand on how to use ABFSS driver ABFS stands for Azure Blob FileSystem Driver to connect and retrieve the data from the Azure Data Lake Storage Gen2. 

In this labs we will also use Azure Key Vault to securely store and retrieve the Storage Keys in Azure Key Vault from Databricks jobs/notebooks using DBUtils.secrets apis. Also learn about the Scopes in Azure Databricks.

This lab is very handy for the developers when they want to retrieve their data from Azure Data Lake Storage Gen2 from within Azure Databricks using ABFS driver.

## Create a Data Lake Storage Gen2 Account

1. Login to Azure portal
2. Click **+ Create a resource**
3. Select **Storage** and select **Storage Account - blob, file, table, queue**
4. Select a valid subscription, Give resource group name, Give valid storage account name, Select nearest location and leave the rest as default
5. Click Next
6. For **Data Lake Storage Gen2 (preview) -> Hierarchical Namespace** select **Enabled** rest all default settings and click next and then select next again and then **create** the storage account
7. Open **Azure Storage Explorer** from your Desktop ( If not installed, you can download the latest version from here, https://azure.microsoft.com/en-us/features/storage-explorer/ ) 
8. Once you Login to your Azure Storage Explorer with the right Azure credentials, you can add a new container within your newly created storage account and create a folder in it
    * Expand your storage account in the Azure Storage Explorer
    * In the **Blob Containers** right click and click **Create Blob Container**
9. Copy the cars auctions file (Kansas_City_Monthly_Car_Auction.csv) into the Container (You can find the cars auction file in this repo)
10. Go back to Azure Portal, select **All Resources**, Open your Storage account, Under **Settings** select **Access Keys** and make a note of either the **Key1** or **Key2**  

## Create the Azure KeyVault account

1. Login to Azure portal
2. Click **+ Create a Resource** 
3. Search for **Key Vault**
4. Hit Create on the **Key Vault page**
5. Enter vaild name, Subscription, Resource Group, Location, Pricing Tier as **Standard**, Select 1 Principal for Access Policies and For **Virtual Network access** you can either configure vnet through **Selected Networks** or for now leave it as default i.e., **All Networks** 
6. Once the KeyVault is created goto the resource
7. Click **Secrets** and **Generate/Import**
8. Under the **Create a Secret** pane, leave **Upload Options** as **Manual**, **name** as **adlsgen2-secret-key**
9. Under value section, You need to copy the keys of your ADLS Gen2 into this box
    * Paste the access **Key** you noted from the Azure Data Lake Storage Gen2 account previously     
10. Leave rest of the fields as default or empty and hit **Create**

## Import the Azure Key Vault into Azure Databricks

1. Access https://<your_azure_databricks_url>#secrets/createScope 
  * Replace your_azure_databricks_url with your Azure Databricks URL (for e.g., https://westus.azuredatabricks.net#secrets/createScope)
2. Enter the name of the secret scope, like databricks-key-vault-secret-scopes
3. For **Manage Principal** use **All Users**
4. Under **DNS Name** enter the URI for the Azure key Vault (You can find this in Azure Portal -> All Resources -> Open your Key Vault REsource -> Under overview section you will find the DNS Name).
  * Copy the DNS Name into the this field (for e.g., https://<YOUR KEY VAULT NAME>.vault.azure.net/)
5. For **Resource ID** enter **/subscriptions/<SUBSCIPTION_ID>/resourcegroups/<YOUR_KEYVAULT_RESOURCE_GROUP>/providers/Microsoft.KeyVault/vaults/<YOUR_KEYVAULT_NAME>**
  * SUBSCRIPTION_ID can be found in Azure Portal -> All Resources -> Open your Key Vault Resource -> Overview page you will find subscription ID
  * YOUR_KEYVAULT_RESOURCE_GROUP can also be found in the overview page
  * YOUR_KEYVAULT_NAME is the name of your keyvault
6. Click **Create**
7. Use the Databricks CLI, **databricks secrets list-scopes** command to verify that the scope was created successfully! 

## Create a notebook to read and perform operations on the data from Azure Data Lake Store Gen2

1. Open the Azure databricks workspace
2. Create a new notebook
3. Add the below code snippet in the cell
`
spark.conf.set("fs.azure.account.key.maadlsgen2.dfs.core.windows.net", dbutils.secrets.get(scope = "<YOUR_SCOPE>", key = "<SECRET_KEY_NAME"))
spark.conf.set("fs.azure.createRemoteFileSystemDuringInitialization", "true")
spark.conf.set("fs.azure.createRemoteFileSystemDuringInitialization", "false")

df = spark.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('abfss://<STORAGE_CONTAINER>@<STORAGE_ACCOUNT>.dfs.core.windows.net/<YOUR_FOLDER>/Kansas_City_Monthly_Car_Auction.csv')

print("Count of auction cars: ", df.count())

from pyspark.sql.functions import *

df2 = df.select(col("Lot #").alias("lot_num"), col("Vehicle ID").alias("vehicle_id"), col("Tow Reference ").alias("tow_reference"), col("Year").alias("year"), col("Make").alias("make"),col("Model").alias("model"),col("VIN").alias("vin"),col("Mileage").alias("mileage"),col("Reason").alias("reason"),col("K").alias("k"),col("Comments").alias("comments"),)
df2.printSchema()
print(df2.count())

modelDF = df2.groupBy("model").count().collect()
display(modelDF)
`
NOTE: 
  * Replace YOUR_SCOPE and the SECRET_KEY_NAME above with the newly created scope in Azure Databricks
  * Replace the STORAGE_CONTAINER, STORAGE_ACCOUNT and YOUR_FOLDER with the newly created container in Azure Data Lake Store Gen2 -> Blob Storage

4. Run the cell by pressing CTRL+ENTER

5. Add a new cell by pressing CTRL+ALT+N
6. Add below code snippet in newly added cell

`
df.show()
`

7. Execute the shell and reveiw the output

8. Add a new cell by pressing CTRL+ALT+N
9. Add below code snippet

`
df2.write.parquet("abfss://<YOUR_CONTAINER>@<YOUR_STORAGE_ACCOUNT>.dfs.core.windows.net/<YOUR_OUTPUT_DIR>")
`
NOTE: replace the container, storage account name, output dir

10. Execute the code snippet by pressing CTRL+ENTER
11. Enter the below code snippet
`
modelDF = df2.groupBy("model").count().collect()
display(modelDF)
`

***Congratulations!, you are able to create connection to Azure Data Lake Storage Gen2 and able to read and write data from it***
