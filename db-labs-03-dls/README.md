# azure-databricks-labs
This lab gives the hands-on experience with reading the data from Data Lake Storage Gen2 as RDD into Spark job.

# Create a Data Lake Storage Gen2 Account

1. Login to Azure portal
2. Click **Create a resource**
3. Select "Storage" and select "Storage Account - blob, data lake gen 2 (preview), file, table, queue"
4. Select a valid subscription, Give resource group name, Give valid storage account name, Select nearest location and leave the rest as default
5. Click Next
6. Select all default settings and click next and then select next again and then create the storage account
7. Add a new container and create a folder in it
8. Copy the cars auctions file (kansas_city_monthly_car_auction.csv) into the Container (You can find the cars auction file in this repo)

# Create a notebook

1. Open the Azure databricks workspace
2. Create a new notebook
3. Add the below code snippet in the cell
`
spark.conf.set(
  "fs.azure.account.key.<YOUR_STORAGE>.blob.core.windows.net",
  "<YOUR_TOKEN_KEY>")

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('wasbs://<YOUR_CONTAINER>@<YOUR_STORAGE_ACCOUNT>.blob.core.windows.net/<YOUR_INPUT_DIR>')

print("Count of auction cars: ", df.count())
df.printSchema()
`
NOTE: replace the container, strorage account and input directory
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
from pyspark.sql.functions import *

df2 = df.select(col("Lot #").alias("lot_num"), col("Vehicle ID").alias("vehicle_id"), col("Tow Reference ").alias("tow_reference"), col("Year").alias("year"), col("Make").alias("make"),col("Model").alias("model"),col("VIN").alias("vin"),col("Mileage").alias("mileage"),col("Reason").alias("reason"),col("K").alias("k"),col("Comments").alias("comments"),)
df2.printSchema()
print(df2.count())
df2.write.parquet("wasbs://<YOUR_CONTAINER>@<YOUR_STORAGE_ACCOUNT>.blob.core.windows.net/<YOUR_OUTPUT_DIR>")
`
NOTE: replace the container, storage account name, output dir

10. Execute the code snippet by pressing CTRL+ENTER
11. Enter the below code snippet
`
modelDF = df2.groupBy("model").count().collect()
display(modelDF)
`

