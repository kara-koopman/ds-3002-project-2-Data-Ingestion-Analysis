# ds-3002-project-2-Data-Ingestion-Analysis

## How it Works

The code which calls the API and writes the data into a database is contained in tool.py. The analysis code is contained in the analysis.py file. Tool.py works by connecting to a dynamoDB database called project2. It then uses the scheduler module to time the execution of the fetch() function. The fetch() function makes an API call to the provided link, parses the JSON file, and then extracts the required fields 'factor', 'time' and 'pi'. It then calls the insert() function which inserts the desired information into the dynamoDB table. The scheduler only runs for an hour because the for loop controls the minute delay between calls (e.g. it runs at the 0 min mark from when the program is executed and then again at the 1 minute mark and so on until 60 mins have passed).

## Execution Timing

Screen shot of the first database insertion (in the consistentExecution.txt file)
![image](https://user-images.githubusercontent.com/88460223/144949276-ebd72e59-7b8d-4f8a-84be-8a61e65c3cb3.png)

Screen shot of the last database insertion 
![image](https://user-images.githubusercontent.com/88460223/144949482-398225ec-e5b8-4b8f-a5b2-6ceae08fb1d7.png)

These screen shots show that data was inserted between minute 00 and minute 59. The text file contains all insertions and can verify the 1 minute spacing.

## Analysis
