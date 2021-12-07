# ds-3002-project-2-Data-Ingestion-Analysis

## How it Works

The code which calls the API and writes the data into a database is contained in tool.py. The analysis code is contained in the analysis.py file. Tool.py works by connecting to a dynamoDB database called project2. I then ran the code using the Windows Task scheduler. Everytime the code is run it will call the fetch() function. The fetch() function makes an API call to the provided link, parses the JSON file, and then extracts the required fields 'factor', 'time' and 'pi'. It then calls the insert() function which inserts the desired information into the dynamoDB table. I also included the time in which the code was called within the dynamoDB table to show that it runs precisely at the minute.

## Execution and timing

Screen shot of the first database insertion (in the consistentExecution.txt file)
![image](https://user-images.githubusercontent.com/88460223/144968812-7eb7532c-7cb1-48d3-bc21-36757ed4898e.png)

Screen shot of the last database insertion 
![image](https://user-images.githubusercontent.com/88460223/144968951-d1a961d9-ae2f-46c6-badb-1f436b3c9cf2.png)

These screen shots show that data was inserted between minute 00 and minute 59.

## Analysis
In the analysis.py file I first load the data in from the CSV I downloaded from DynamoDB and make it into a pandas dataframe. At first the data seemed like non-sense as it was sorted based on the insertion time and not the 'time' pulled from the API. Because the API time was provided in datetime format I converted this into minutes past the hour by parsing the string and isolating the minute number. I then plotted the data values against eachother:

### Relationship between Factor and Time
![image](https://user-images.githubusercontent.com/88460223/144967849-3a285c17-aedb-4ec9-bc6b-fc5fdc321f2b.png)

We can see that the factor seems to be exponentially increasing with time. 

### Relationship between Pi and Time
![image](https://user-images.githubusercontent.com/88460223/144968046-e313834e-220a-421b-8227-62526f344582.png)

Additionally, we can see that as time progresses the value of 'Pi' oscillates around and then converges to the actual value of pi (found using np.pi) 

### Relationship between Pi and Factor 
![image](https://user-images.githubusercontent.com/88460223/144968170-5e41d22c-e02d-4abc-b08e-3300af1a3aac.png)

Finally, we see a similar convergence when increasing the factor value.

Because of the initial oscillatory behavior and the eventual convergence, this lead me to believe that this data was representative of an infinite series. Infinite series slowly approach a certain value through the addition of terms. Throughout the hour, the API generates the next factor in the series, plugs it into the series formula, and then returns the series summation: a slowly, more and more accurate value of pi.

## Sources
https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
https://en.wikipedia.org/wiki/Series_(mathematics)

