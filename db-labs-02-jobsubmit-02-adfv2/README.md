# Azure-Databricks & DataFactory-V2-Pipeline Labs

Orchestrating the jobs i.e., defining the workflows and managing and monitoring the workflows in Azure Databricks can be done within  the DataFactory-V2.
In this labs we will create a Python job to calculate the value of PI and configure this job in a DataFactory V2 pipeline to execute and monitor the job from within DFV2. 

## Pre-Requisites
This lab expects you to have a valid Azure subscription and that you have privileges to create the Azure services like Azure Data Factory V2 and Azure Databricks. 
This lab depends on two other labs in this repository
1. DBCLI labs
2. JOBSUBMIT-CLI-UI labs
You can either complete those labs or need to refer to intsructions partially from the above mentioned labs

## Create the DataFactory V2 from Azure Portal

1. Log into your Azure Portal 
2. Select **+ Create a Resource** button from left side menu and select **Analytics** and click on **Data Factory** 
3. Give a Datafactory name say **ADFV2Workflows** (NOTE: this name needs to be globally unique so feel free to append your company name or your name in the datafactory name)
4. Select a valid subscription
5. For **Resource Group** select **Use exisiting** and select the same resource group name as you used to create Databricks workspace or alternatively you can use **Create New** and give the resource group name something like **az_df_labs_rg** 
6. Select Version as **v2**
7. Select location the same as your Databricks, if the datafactory does not exist within the same region please feel free to select the closest region  
NOTE: Even though DataFactory exists in a different region the actual data will not move out of your region instead only the pipeline configurations will live in the same region as DataFactory. (So your data do not move out of your region, since DFV2 is only scheduling the jobs)
8. Click **create**
NOTE: Once the DataFactory V2 is created successfully then it will create a notification in the top right corner under bell icon 

## Create the DataFactory Pipeline to create, execute, schedule, monitor the Azure Databricks jobs

1. Log into your Azure Portal 
2. Once the DFV2 is created, go to the resource through the notification bell (or) select **all resources** and select your **DataFactory instance** in my case it is **ADFV2Workflows**  
3. Click on **Author and Monitor**, this will launch the authoring portal
4. In the left side menu click on **Author** icon (This will be small pen like icon on the left navigation pane)  
### Steps to create a Compute Linked Service
5. Select **Connections** at the bottom of the window, under **Linked Services** select **+ New**
6. Under **New Linked Service** pane to the right, select **Compute** tab and select **Azure Databricks** 
7. Give a name to the linked service as **AzureDatabricks_LinkedService**, Optionally give some **Description**
8. For **Connect via integration runtime** select **AutoResolveIntegrationRuntime**
9. Under **Account Selected Method** select **From Azure Subscription**
10. For **Azure Subsciption** select the right Azure Subscription where your databricks instace is created
11. In **Databricks workspace** from the drop down list select appropriate databricks resource
12. Under **Select Cluster** select **New Job Cluster**
13. Use the token you have already created from the **dbcli** labs or generate a new token as per the instructions in **dbcli** labs (Refer to **Generate a token section in DBCLI labs in this repository**) 
14. For **Cluster Version** select **4.3 (Includes Apache Spark 2.3.1, Scala 2.11)** 
NOTE: there are two cluster types for 4.3, one have GPU capability. This is not required for our labs so please select the plain cluster type, unless you are happy to spend more money for GPUs :( 
15. Under **Cluster node type** select **Standard_DS3_V2 (14GB Memory, 4 Cores, 0.75 DBU)** 
NOTE: DBU stand for Databricks Unit, you will be charged based on the VM size, number of VMs and the amount of DBUs
16. Select **Python Version** as **3**
17. For **Worker Options** Select **Auto Scaling** and give **Min Workers** as **2** and **Max Workers** as **8**
18. Review the **Additional Cluster Settings** section, Leave the Additional Cluster Settings as default 
19. Click **Finish**
### Steps to create an Activity
20. Under **Factory Resources** click on **+** icon, followed by **pipeline**  
21. Under **Activities** drag and drop **Python** into the **Pipeline editor pane**
22. Below the **Pipeline editor pane** select **Azure Databricks** and in the **Databricks Linked Service** select your Azure databricks linked service. In my case it is **AzureDatabricks_LinkedService**
23. Change to **Settings** tab for **Python file** give the value as **dbfs:/docs/pi.py** (NOTE: this pi.py file is copied into DBFS in the **pyjobcli** lab or follow the instructions under the section **Upload your python script to DBFS**)
NOTE: If you want to send any input parameters to the job (like input path, output path, or other values you can use the **parameters** section and configure the new parameters for the job)
24. Click on **Publish ALL** button on the top left corner of the page
25. Click on **Trigger** followed by **Trigger now** button followed by **finish** button on the trigger now pane
26. Click on the **Monitor** icon on the left side naviation pane (NOTE: you will find a red circle button underneath the editor icon (pen icon))
27. You can find the job is **in progress** state. This may take 7 to 8 mins to complete
28. You can also login to your azure databricks workspace and then click on clusters and monitor the progress of the newly submitted job from Datafactory v2  

***Congrats, you now have created and submitted DFV2 Databricks pipline successfully***