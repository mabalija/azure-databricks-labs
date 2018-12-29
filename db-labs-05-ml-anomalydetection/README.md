# azure-databricks-labs
This lab gives the hands-on experience with Azure Databricks ML module.

## Create an Azure Blob Storage account and upload the Network logs - Synthetic data

1. Login to the Azure portal
2. Click **+ Create a Resource** button
3. Select **Storage** and click **Storage account - blob, file, table, queue**
4. Select a valid subscription, resource group, account name, nearest location, select standard
5. For **Account Kind** select **Blob Storage**
6. Leave **Replication** as **RA-GRS** and **Access Tier** as **Hot**
7. Hit **Review + Create** and **Create**
8. Once the deployment is successful, goto the storage account through the notification bell and clicking **Go to resource** button
9. Under **Settings** select **Access Keys** and make a note of **Key1** (or) **Key2**
10. Download the file **kddcup.data_10_percent.gz** from below link  
http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html 
NOTE: Only use the 10 percent dataset from this link for the scope of this labs. You can use the whole dataset for your learning in your personal time :)
11. Extract the gzip file, you will get **kddcup.data_10_percent_corrected**
12. Open **Microsoft Azure Storage Explorer** from your desktop and connect to your Azure subscription  
NOTE: Follow the instructions in the **dls-gen2-abfs** labs to download and install the storage explorer in your desktop, if it is not availble in your desktop or VM
13. Under the **Storage accounts**, open the newly created blob storage account
14. Expand **Blob Containers**, right click and select **create blob container** and give a valid name, in my case I gave **root** as the container name 
15. Click on **+ New Folder** and give a folder name as say **network-logs**
16. Upload the file **kddcup.data_10_percent_corrected** from where you have extracted into the newly created folder **network-logs** in the blob container **root**
17. Wait until the file is uploaded successfully!
 
## Import the Anomaly Detection notebook .dbc file into your workspace, execute the ML Model and review the output

1. Login to Azure portal
2. Launch the Azure databricks workspace
3. Click on **Workspace** icon from the left navigation pane 
4. Click on the **down arrow icon** next to workspace
5. Hit **Import**
6. Upload the **anomaly_detection_v1.dbc** file from this repo to this workspace
7. Click on **Home** icon from the left navigation pane
8. Goto to the **anomaly_detection_v1** notebook under the **Recents** section
9. In the **Cmd 1** replace all of the following,
    * Replace **<Azure Storage KEY - You can copy this from your Azure Portal>** with your Blob Storage Key which you have copied from above instructions
    * Replace **<STORAGE_ACCOUNT_NAME>** with your Storage Account name, this can be found from the overview page of the Storage resource in Azure portal
    * Replace **<BLOB_CONTAINER>** with the newly created contianer name above (in my case **root**)
    * Replace **<STORAGE_ACCOUNT_NAME>** with your Storage Account name, this can be found from the overview page of the Storage resource in Azure portal
    * Repace **<YOUR_FOLDER>** with the folder name created above (in my case **network-logs**)
10. Review each command and run one by one and monitor the results of each command

*Congrats! you are now been able to learn how easy-it-is to create an ML model using Azure Databricks Notebooks* 