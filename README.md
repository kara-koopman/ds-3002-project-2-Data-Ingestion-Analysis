# ds-3002-project-2-Data-Ingestion-Analysis

## How it Works

The code which calls the API and writes the data into a database is contained in tool.py. The analysis code is contained in the analysis.py file. Tool.py works by connecting to a dynamoDB database called project2. I then ran the code using the Windows Task scheduler. Everytime the code is run it will call the fetch() function. The fetch() function makes an API call to the provided link, parses the JSON file, and then extracts the required fields 'factor', 'time' and 'pi'. It then calls the insert() function which inserts the desired information into the dynamoDB table. I also included the time in which the code was called to show that it runs precisely at the minute.

Task scheduler information:
![image](https://user-images.githubusercontent.com/88460223/144961097-091bcddd-b0fa-4cde-b6a9-1ec7907e94fa.png)

## Execution Timing

Screen shot of the first database insertion (in the consistentExecution.txt file)


Screen shot of the last database insertion 


These screen shots show that data was inserted between minute 00 and minute 59.

## Analysis
In the analysis.py file I first load the data in from the CSV I downloaded from DynamoDB and make it into a pandas dataframe. At first the data seemed like non-sense as it was sorted based on the insertion time and not the 'time' pulled from the API. Because the API time was provided in datetime format I converted this first into a string and then into epoch time to get a continuous time variable which I could use to plot. I then plotted the three variables against eachother:

### Relationship between Pi and Time

### Relationship between Factor and Time

### Relationship between Pi and Factor 


## Sources
