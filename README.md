# Problem Statement 
End to End Data Engr Project.
1. Design Architecture for Data Ingestion Pipeline: Firstly we want to create a reporting solution for data that can be found in this site here (All the data points can be seen when you click on the view button under the details column). This would involve extracting, transforming and loading the data. 
#### a.
The first task is to design a data ingestion pipeline architecture showing the different tools and framework you would propose to the business in achieving the final result. Things your architecture or pipeline should answer includes scheduling and automation, final data warehouse or database, tools for extraction and loading and finally the flow showing how you intend to move data from source to destination.

## Solution 
B. The second task here is to design the ERD(Entity Relationship Diagram) of the system and schema of your final data mart that would be used for reporting. Apply normalization from 1NF, 2NF and 3NF where applicable.

2. Data Extraction, Transformation and Loading: 
A.Here, you are expected to extract data of 60 health institutions which is loading the details from the first 3 pages of the website, perform adequate transformation on it to have it as a dataframe or flat file that can be loaded into the final destination.
On extracting the data, load it into any coding environment of your choice and read this data with Pyspark, then filter out the data to a health institution that has at least one doctor and save it as a parquet file named doctors.parquet.
	B. Secondly with reference to the ERD and Schema you have proposed above, perform data loading into the final destination of your choice and answer the following questions and the screenshots of the results should be attached in your final submission.
Select Top 10 sample results
Health Institution with highest number of beds
Health Institution with highest number of Doctors
Average number of beds across the ingested data
Health Institutions with Doctors and Pharmacists
Health Institutions without Nurses
Health Institutions with Doctors, Nurses and Pharmacist
Health Institutions with No doctors
Finally, the Health institution with the highest number of personnel across the board.
Bonus Tip: You can use any web scraping tool or RPA framework like tagui python rpa, or robocorp python rpa framework for the extraction.

3. Automation and Scheduling: Using the workflow management or orchestration tool of your choice, automate if possible the whole process or any part of the pipeline process and attach any schedule of your choice to this. Kindly share screenshots of this too.
Bonus Tip: You can use Airflow and share pictures of your DAG and schedule on airflow UI

Submission:
Submit by creating a folder named Data_Engr_Assessment, Inside that folder, create subfolders for each question and put in all necessary files like data files,code files and images of results that pertains to each subfolder. Upload the Parent Folder Data_Engr_Assessment to any drive or cloud storage and share the public link to access or download the folder.
Kindly name each file correctly.
