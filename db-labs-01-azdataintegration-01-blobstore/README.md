# azure-databricks-labs
This lab gives the hands-on experience with reading the data from Blob Storage as RDD into Spark job.

## Load the data into Azure Storage (Blob Storage)

**Note: You need to have a Blob Storage account to complete these steps**

1. Open the Azure Storage Explorer from your machine
     i. Goto the start button and search for "Azure Storage Explorer"
    ii. Open the Storage explorer
2. login to your storage account 
3. Create a container under the Blob Containers **sourcecontainer**
4. Create a new directory under the Blob container **"azdb-input-datasets"**
5. Upload the **wordcount-testset.txt** file into the directory (you can find this txt file in this repository)

## Create a new notebook in Azure Databricks Workspace

1. Open the Azure databricks workspace
2. Click on the **workspace** folder and under the username you can create a new notebook and select language as **python**
3. Call the notebook as **wordcount**
4. Copy the code from the wordcount.py into the newly created notebook (Note: you can find wordcount.py in this repository)  
    i. Review the code snippet - it calculates the count of words in the input documents  
    ii. review the the below line of code  
    ` spark = SparkSession.builder.appName("AzureDatabricksWordCount").getOrCreate()`  
    Notice that you are invoking the getOrCreate() method to create the spark session object instead of instantiating new object. Ensure that you always use getOrCreate() method to create the spark session.  
    iii. Data from the Blob Storage is read as RDD  
    ` lines = spark.read.text(inpath).rdd.map(lambda r: r[0]) `  
    ii. Notice that #spark.stop() this command in the end of the job is commented, in Databricks you should not manually stop the spark session object as this will have unexpected behaviour on your job  
5. Replace the CONTAINER_NAME, STORAGE_ACCOUNT and the DIRECTORY_NAME according to your settings
6. Press CTRL+ENTER to run the notebook, it may respond to attach the cluster so please attach the cluster you have created previously or create a new cluster and attach this notebook to that cluster
7. You may get below error message
shaded.databricks.org.apache.hadoop.fs.azure.AzureException: shaded.databricks.org.apache.hadoop.fs.azure.AzureException: **Container images in account yourstorage.blob.core.windows.net not found,** and we can a post create it using anoynomous credentials, and no credentials found for them in the configuration.
Note: Your Azure Databricks cluster is not able to read the files as it does not have access to the Blob Storage

## Configure the Blob Storage in your cluster settings

1. Open your Azure Databricks workspace
2. Open the **clusters**
3. Select your cluster under **Interactive Clusters**
4. Click on Edit
5. Under the Spark Config box -> add the below settings
**spark.hadoop.fs.azure.account.key.aimastorage.blob.core.windows.net <YOUR_BLOB_STORAGE_ACCOUNT_TOKEN_KEY>**
Note: You can find the TOKEN KEY Azure Portal -> ALL Resources -> Your Storage Account -> Access Keys -> **Primary Key (or) Secondary key**
6. Click **Confirm and Restart** button 
7. Go back to your notebook and press CTRL+ENTER
8. Once the notebook runs successfully it will produce below output
`
 :20 
 out: 3 
 Cosmos: 3 
 share: 6 
 how: 3 
 for: 18 
 Get: 3
 `

