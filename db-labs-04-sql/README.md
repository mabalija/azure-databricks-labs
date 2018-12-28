# azure-databricks-labs
This lab gives the hands-on experience with creating a temporary table and querying the table.

## Create a local table in Azure Databricks through UI dataset 

1. Login to Azure portal
2. Launch the Azure databricks workspace
3. Click on the **Data** icon from the left navigation pane, under **Databases** select **Default** 
4. Click **Add Data**
5. Under **Data Source** Select **Upload File** and click **Browse** link from **File** section  
NOTE: You can create tables from wide variety of data sources you can review the **Other datasources** drop down on the top like Azure Blob Storage, Data Lake Storage etc
6. Upload the file from this repository **Kansas_City_Monthly_Car_Auction.csv**
7. Once uploaded successfully, you can click on **Create Table With UI**
8. Under **Select the cluster to preview the table** select one of the running clusters and hit **Preview Table**
9. Give the name of the table as **city_cars**
10. Create in database, select **default**
11. File Type as **CSV**
12. Select **First Row is Header** check-box and **Infer Schema** check-box
13. Modify the column names to not to have the spaces in the names and also remove special characters
14. Review the datatypes infered by the table creation UI
15. Hit **Create Table**

## Create a table programatically through notebook

1. Login to Azure portal
2. Launch the Azure databricks workspace
3. Click on the **Data** icon from the left navigation pane, under **Databases** select **Default** 
4. Click **Add Data**
5. Under **Data Source** Select **Upload File** and click **Browse** link from **File** section  
NOTE: You can create tables from wide variety of data sources you can review the **Other datasources** drop down on the top like Azure Blob Storage, Data Lake Storage etc
6. Upload the file from this repository **Kansas_City_Monthly_Car_Auction.csv**
7. Once uploaded successfully, you can click on **Create Table in Notebook**
8. In the **Command 2** modify **infer_schema** flag to **true** and **first_row_is_header** flag to **true**
9. Run **Commands** 2, 3, 4 in the notebook
10. Replace the code in **Command 5** as below,
`
permanent_table_name = "Kansas_City_Cars"

renamedDF = df.withColumnRenamed("Lot #", "lot_no").withColumnRenamed("Vehicle ID", "vehicle_id").withColumnRenamed("Tow Reference ", "tow_reference")
renamedDF.write.format("parquet").saveAsTable(permanent_table_name)
`
11. Execute the command
12. You might see the command executed successfully with out any errors

*Congratulations! you now have created the tables in Azure Databricks successfully!*


