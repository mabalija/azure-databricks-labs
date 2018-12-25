# azure-databricks-labs
This lab gives the hands-on experience with Databricks Utilities within Azure Databricks Notebooks.
The syntax of the Databricks utils looks like below,
`DBUtils.fs.ls(<path>)`
`DBUtils.notebook.help()`

## Create an interactive cluster in Azure Databricks workspace

1. Launch **Azure databricks workspace** from your Azure Portal 
2. Select **Clusters** icon from the left side pane
3. Click on **+ Create Cluster** button
4. Give the cluster name as **azure-databricks-test-cluster**
5. Select Cluster Mode as **Standard**  
**NOTE: You will find two modes High Concurrency and Standard modes, select standard mode for now**
6. Leave the **Databricks runtime version** as default
**NOTE: Please review the runtime versions, you will find bunch of Databricks images to select from each with a specific spark and scala versions and some versions are suitable for ML workloads with GPU**
7. Select the **Python version** as **3**
8. Select **Driver Type** as **Same as worker**
**NOTE: Please review VM types like General Purpose, Memory Optimized, Storage Optimized, Compute Optimized; each of these types are uniquely sized for supporting variety of workloads. Notice DBUs along with each VM Size i.e., Databricks Units**
9. Select **Worker Type** as *Standard_DS3_V2*, *Min Workers as 2* and *Max workers as 8* and Enable *auto-scaling*
10. Enable **Auto Termination** and set the minutes of inactivity to say *120*  
This will automatically terminate the inactive cluster i.e., without any jobs or commands executed, after the specified amount of time is elapsed
11. Leave the **Spark Config** and **Environment Variables** as default or empty

## Create a new notebook in Azure Databricks Workspace

1. Launch **Azure databricks workspace** from your Azure Portal
2. Click on the **workspace** folder and under the username you can create a new notebook and select language as **python**
3. Call the notebook as **dbutils**
4. Add the below command to your notebook cell (i.e., Cmd 1) and click on the **Run Cell** icon and click **Run Cell**  
`dbutils.fs.help()`  
NOTE: a) You might get error **No cluster is attached** (You can click Attached: and select the newly created cluster - This will attach your notebook to the selected cluster)
      b) Review the help content to get familierity with the *dbutils.fs*
6. Click the **Keyboard** icon on the top right of the notebook to find the keyboard shortcuts for the Azure Databricks notebooks
7. Press **Ctrl + Alt + n** to add a new cell below
8. Add the command `dbutils.notebook.help()` and press Alt + Enter
NOTE: Review the notebook dbutil command
10. Add the command `dbutils.widgets.help()` in the new cell and press Alt + Enter
NOTE: Review the widgets dbutil command 
11. Add the command `dbutils.widgets.combobox("region", "UK", ["UK", "USA", "EU", "IN"], "Region")` in the new cell and press Alt + Enter
NOTE: This will create a new widget on the top of the notebook and by default selects the UK as the region
12. Select *EU* as the region from the widget
13. Add below commands in the new cell,  
`region = dbutils.widgets.get("region")  
print("User Selected Region as : " + region)`
and run the cell.
NOTE: You will find the output as your selected region.
14. You can change the behavior of the widget panel  
    i. click on the settings button on the widget panel  
    ii. **On Widget Change** setting select **Run Accessed Commands** - this will rerun the cells upon the change in the widget
    NOTE: If you select **Run Notebook** this will re-run entire notebook if any of the wigets is changed
15. **This applies only to Databricks runtime 5.1 and above, so do not run this if you are on lower versions, but you can still read this :(**  
Add the command `dbutils.library.help()` in the new cell and press Alt + Enter
NOTE: Review the library dbutil command 
16. **This applies only to Databricks runtime 5.1 and above, so do not run this if you are on lower versions, but you can still read this :(**  
Add the command 
`dbutils.library.installPyPI("tensorflow")
dbutils.library.restartPython()` in the new cell and press Alt + Enter
NOTE: This will install the tensorflow in your cluster. RestartPython should loose all the variables, state etc. So better to run these sort of commands in the beginning of the notebooks.
