# azure-databricks-labs
This lab gives the hands-on experience with creating a temporary table and querying the table.

# Create the dataset

1. Login to Azure databricks
2. Launch the Azure databricks workspace
3. Click on the **Data** icon
4. Click **add data**
5. Select **Other datasources** and select **Azure Blob Storage**
6. In command 3 populate the Azure Storage account name and the Token key in the Azure storage access key
7. Execute the shell by pressing CTRL+ENTER
8. In command 4 Update the file location to the file you have created in the previous labs (for e.g., wasbs://<YOUR_CONTAINER>@<YOUR_STORAGE_ACCOUNT>.blob.core.windows.net/<YOUR_OUTPUT_DIR>) and populate the values appropriately
9. Update the file type as **"parquet"**
10. Execute the commands 4, 5 and 6 by pressing CTRL+ENTER
11. In command 9 change the column name as **model**
12. Execute command 9, 11
13. Replace the select query as below
`code`
SELECT model, Max(Year) FROM YOUR_TEMP_VIEW_NAME GROUP BY model
`code`
14. Review %sql command on the top, this is the magic command which can turn the python notebook to run sql queries
