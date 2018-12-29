# azure-databricks and Cosmos DB integration labs
This lab gives the hands-on experience with reading and writing the data from Azure Cosmos DB as dataframe into Spark job.

# pre-requisites
Please follow the complete instructions from **dlsgen2** labs

# Create a Cosmos DB Database and Collection

1. Login to Azure portal
2. Click **Create a resource**
3. Select **databases** and select **Azure Cosmos DB**
4. Select a valid subscription, Give resource group name, Give valid account name, Select api as **Core (SQL)**, Select nearest location and leave the rest as default
5. Click **Review + Create**
6. Once the Cosmos DB account is created successfully, goto resource
7. Under **Overview** section, click **+ Add Collection**
8. Click **New Collection** and select **Create New** for **Database ID** give any valid Database ID Name
NOTE: You can select the **Provision Database Throughput** this will allocate the troughput under database level and can be equally allocated for all the collections created under this database. 
Alternatively you can also allocate throughput at Collection level
9. Give a valid **Collection ID** as **cars**
10. Give the partition key as **/vehicleID**
11. Click **OK** 
NOTE: This will create both the database and the collections in Cosmos DB.

# Upload the jar file to the Azure Databricks Cluster

1. Launch Azure Databricks workspace
2. Select **Clusters** icon from the left navigation pane and select **+ Create Cluster**
3. Create a **Standard** cluster with all the default settings
4. Once the cluster is created and started (or Running)
5. Select the **Azure Databricks** icon from the left navigation pane in Databricks workspace
6. Under **Common Tasks** click on **Import Library**
7. Select **Source** as **Upload Java/Scala Jar** 
8. Give Library name as **azure-cosmosdb-spark-lib**
9. Upload the library jar file **azure-cosmosdb-spark_2.3.0_2.11-1.2.2-uber.jar** from this repo to the workspace by click on **Drop Library Jar here to Upload** button
10. Hit **Create Library** 
11. You can now click on the checkbox under **Attach** for the newly created cluster 

NOTE: These steps will load the Comos DB - Spark connector jar file to the cluster and make it available for your use within your jobs/notebooks. 

# Create a notebook in Azure Databricks to Write and Read data into Cosmos DB Collections

1. Open the Azure databricks workspace
2. Create a new notebook
3. Add the below code snippet in the cell
`
spark.conf.set("fs.azure.account.key.maadlsgen2.dfs.core.windows.net", dbutils.secrets.get(scope = "<ADLS_SCOPE>", key = "<ADLS_KEY_NAME>"))
spark.conf.set("fs.azure.createRemoteFileSystemDuringInitialization", "false")

df = spark.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('abfss://<BLOB_CONTAINER>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/<YOUR_FOLDER>/Kansas_City_Monthly_Car_Auction.csv')

print("Count of auction cars: ", df.count())

from pyspark.sql.functions import *

df2 = df.select(col("Vehicle ID").alias("vehicleID"), col("Lot #").alias("lot_num"), col("Tow Reference ").alias("tow_reference"), col("Year").alias("year"), col("Make").alias("make"),col("Model").alias("model"),col("VIN").alias("vin"),col("Mileage").alias("mileage"),col("Reason").alias("reason"),col("K").alias("k"),col("Comments").alias("comments"),)
df2.printSchema()
print(df2.count())
`
NOTE: replace the container, strorage account and input directory

4. Run the cell by pressing CTRL+ENTER

5. Add a new cell by pressing CTRL+ALT+N
6. Add below code snippet in newly added cell

`
# Cosmos DB Write configuration
writeConfig = {
 "Endpoint" : "<COSMOSDB_URI>",
 "Masterkey" : "<COSMOSDB_KEY>",
 "Database" : "<DATABASE_ID>",
 "Collection" : "<COLLECTION_ID>",
 "Upsert" : "true"
}

# Write to Cosmos DB from the cars DataFrame
df2.write.format("com.microsoft.azure.cosmosdb.spark").options(**writeConfig).save(mode="append")
`
NOTE: Replace below
  * COSMOSDB_URI -> This can be found in the Azure Portal -> COSMOS DB Resource page -> Overview section -> **URI** 
  * COSMOSDB_KEY -> Under **Keys** section of Cosmos Resource page -> Copy **PRIMARY** (or) **SECONDARY key**
  * DATABASE_ID & COLLECTION_ID -> Under the Overview section -> Collections -> copy **Database** ID and **Collection** ID

7. Execute the shell and reveiw the output

8. Add a new cell by pressing CTRL+ALT+N
9. Add below code snippet

`
# Cosmos DB - Read Configuration
readConfig = {
  "Endpoint" : "<COSMOSDB_URI>",
  "Masterkey" : "<COSMOSDB_KEY>",
  "Database" : "<DATABASE_ID>",
  "preferredRegions" : "West Europe",
  "Collection" : "<COLLECTION_ID>",
  "SamplingRatio" : "1.0",
  "schema_samplesize" : "1000",
  "query_pagesize" : "2147483647",
  "query_custom" : "SELECT * FROM cars"
}

# Connect via azure-cosmosdb-spark to create Spark DataFrame
cars = spark.read.format("com.microsoft.azure.cosmosdb.spark").options(**readConfig).load()
cars.count()
`
NOTE: Replace below
  * COSMOSDB_URI -> This can be found in the Azure Portal -> COSMOS DB Resource page -> Overview section -> **URI** 
  * COSMOSDB_KEY -> Under **Keys** section of Cosmos Resource page -> Copy **PRIMARY** (or) **SECONDARY key**
  * DATABASE_ID & COLLECTION_ID -> Under the Overview section -> Collections -> copy **Database** ID and **Collection** ID

10. Execute the code snippet by pressing CTRL+ENTER
11. Add a new cell by pressing CTRL+ALT+N
12. Add below code snippet  
`
display(cars.orderBy(col("vehicleID")))
`
13. Execute the code snippet by pressing CTRL+ENTER
14. This should display the list of documents ordered by vehicleID

*Congratulations! you now have successfully able to Write and Read data from CosmosDB within Databricks using Cosmos DB connector*
