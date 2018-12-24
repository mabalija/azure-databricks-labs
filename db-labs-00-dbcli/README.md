![Alt text](../images/az-db-logo.jpg "Azure Databricks Labs")

# Azure-Databricks-Labs

Databricks Developer Tools are used to build Spark applications from outside of Databricks environment. These include,
* Databricks CLI
* Databricks Utilities (These utilities are run from within the Databricks notebooks)
    * File System Utilities
    * Notebook Workflow Utilities
    * Widget Utilities
    * Secrets Utilities
    * Library Utilities
* Data Pipelines
    * Azure DataFactory
    * Apache Airflow

In this lab you will install the Databricks CLI and run few commands to get hands-on experience using the Databricks CLI.
You can create groups, ACLs (Access Control Lists) and configure ACLs based on users (i.e., principals).

## Pre-Requisites
This lab expects you to have a working Python 3 (i.e., Python 3.6 and above) installation either on your Desktop, or alternatively you can simply use the Data Science Virtual Machine (DSVM) or any tier in Azure.

## Install Databricks CLI

1. Open command prompt in your VM
2. Run below command
    `pip install databricks-cli`

## Generate the token to interact with Databricks cluster using Databricks-CLI

1. Log into your Azure Portal 
2. Select your Databricks resource 
3. Click the **Launch Workspace**
4. Once you login to the workspace you will find the **person icon** on the top-right side of the page
5. Click the  **Person Icon** and select **User Settings**
6. Click **Generate New Token** and key in the **Comment** and **Lifetime**, ensure that you **copy the token key in a secure place** and store it for future use

## Connect to Databricks from CLI

1. Run below command
    ` databricks configure --token `
2. Log into your Azure Portal 
3. Select your Databricks resource
4. Under the overview section copy the URL ( for e.g., https://******.azuredatabricks.net )
5. When it will prompt to enter **Databricks Host (should begin with https://):**, Please enter the URL you copied previously
6. It will prompt for token
7. Paste the token created previously
8. Run the command **databricks workspace ls** and you must see atleast two folders like Users and Shared

**Note: You can use multiple profiles to connect to various Databricks workspaces from the same Databricks CLI**

## Get familiarity with commands

1. Run the help command, `databricks -h` 
    This command will display various sub-commands like clusters, jobs, fs etc

2. Run the help command on a sub-group, `databricks clusters -h`
    This command returns the operations available on **clusters** sub-command

3. List the files under your workspace - replace the exmaple below with your username and your company with your company name for Databricks workspace
    **databricks workspace ls /Users/example@yourcompany.com**

4. List the databricks clusters
    **databricks clusters list**

5. List the runtime versions of the spark clusters    
    **databricks clusters spark-versions**

6. DBFS commands: List the files in DBFS
    **databricks fs ls**

7. DBFS Commands: Copy the local files into DBFS
    **dbfs cp <Path to Local file>/test.txt dbfs:/test.txt**

8. Run the groups command, `databricks groups list`
This command lists all the available groups in the current databricks workspace

9. Run the command, `databricks groups list-members --group-name admins` 
This command will display the user names under the group **admins**

10. Run the command `databricks groups create --group-name dev-group`
This command will create a new group called dev-group

11. Run the jobs command, `databricks jobs -h`

12. Run the command, `databricks jobs list`