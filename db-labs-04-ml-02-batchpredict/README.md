# azure-databricks-labs
This lab gives the hands-on experience in how to save a model to Blob Storage and use it for batch predictions in Azure Databricks.

## pre-requisites
Please follow the complete instructions in **anomalydetection** labs

## Save the model to Blob Storage

1. Login to Azure portal
2. Launch the Azure databricks workspace
3. Click on **Workspace** icon from the left navigation pane 
4. Open the previously imported notebook **anomaly_detection_v1** from the workspace 
5. Before you run the notebook, you need to follow below steps
    1. Goto Azure Databricks workspace
    2. Open the **clusters**
    3. Select your cluster which you want to use to run this notebook on
    4. Click on Edit (if started, **terminte** the cluster)
    5. Under the Spark Config box -> add the below settings **spark.hadoop.fs.azure.account.key.<STORAGE_ACCOUNT_NAME>.blob.core.windows.net <YOUR_BLOB_STORAGE_ACCOUNT_TOKEN_KEY>**
    Note: 
        * Replace <STORAGE_ACCOUNT_NAME> => You can find the Storage Account Name from, Azure Portal -> ALL Resources -> Your Storage Account -> Overview page
        * Replace <YOUR_BLOB_STORAGE_ACCOUNT_TOKEN_KEY> => You can find the TOKEN KEY from, Azure Portal -> ALL Resources -> Your Storage Account -> Access Keys -> **Primary Key (or) Secondary key**
    6. Click **Confirm and Restart** button 
6. Run all the commands in your notebook by clicking **Run All** command from the top of the notebook
7. Once all the commands are successfully executed, goto the last command in the notebook and press **ctrl+alt+n** command
8. This will create a new command below, go to the newly created cell/command 
9. Copy below code snippet into the cell   
`
pipelineModel.save("wasbs://<BLOB_CONTAINER>@<STORAGE_ACCOUNT_NAME>.blob.core.windows.net/anomaly-detection-model-pipeline/")
`  
Replace <BLOB_CONTAINER> and <STORAGE_ACCOUNT_NAME> as per instructions in step 5
10. Go to your Azure Storage Explorer within your desktop and refresh the container, you will find the newly created folder called **anomaly-detection-model-pipeline** and the actual model persisted in this directory

*Congrats! you have learnt how to persist the ML model into Azure Blob Storage* 

## Do the Batch Predictions for the test data

1. Download the test data **kddcup.newtestdata_10_percent_unlabeled.gz** from below link  
http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html 
 
2. Extract the gzip file
3. Review the file contents **kddcup.newtestdata_10_percent_unlabeled** 
4. Create a new folder in your Storage account as **network-logs-production-data**
5. Upload the file into the newly created directory using **Azure Storage Explorer**
6. In the **anomaly_detection_v1** press **ctrl+alt+n** to add new cell/command in the end
7. Add below code snippet in the new cell     
`  
val networkProductionLogFieldsTuple = networkLogSchema.splitAt(networkLogSchema.fieldIndex("label"))
var networkProductionLogSchema: StructType = StructType(networkProductionLogFieldsTuple._1)
println(networkProductionLogSchema)
val networkProductionLogsDF = spark.read.format("csv") 
  .schema(networkProductionLogSchema)
  .load("wasbs://<BLOB_CONTAINER>@<STORAGE_ACCOUNT_NAME>.blob.core.windows.net/<YOUR_FOLDER>")
networkProductionLogsDF.describe()
println(networkProductionLogsDF.count())
val networkProductionLogs = networkProductionLogsDF.rdd.map(transformRowIntoLabelledPoint).toDF
display(networkProductionLogs)
val featureIndexer2 = new VectorIndexer()
  .setInputCol("features")
  .setOutputCol("indexedFeatures")
  .setMaxCategories(10)
  .fit(networkLogsTrainDF)
`  

NOTE: Replace <YOUR_BLOB_CONTAINER> and <YOUR_STORAGE_ACCOUNT_NAME> as per instructions in step 5
      Replace <YOUR_FOLDER> as the newly created folder name where you copied production data in my case it is **network-logs-production-data**
8. Press **ctrl+enter** to run the above command and press **ctrl+alt+n** to go to new command, add below code snippet,  
`
import org.apache.spark.ml.PipelineModel
val networkLogAnomalyDetectionModelPipeline = PipelineModel.load("wasbs://<BLOB_CONTAINER>@<STORAGE_ACCOUNT_NAME>.blob.core.windows.net/<YOUR_FOLDER>/")
`  
Replace above place holders accordingly specially YOUR_FOLDER here is for Model folder (i.e., where you persisted model) not the data folder

9. Press **ctrl+enter** to run the above command and press **ctrl+alt+n** to go to new command, add below code snippet,  

`
val finalPredictions = networkLogAnomalyDetectionModelPipeline.transform(networkProductionLogs)
finalPredictions.select("prediction", "label", "features", "indexedFeatures").show(5)
`

*Congrats! you now have load the pipeline model from Azure Blob Storage and do the batch predictions on the production unlabeled data* 