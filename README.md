# rsf-data-visualizer

A Django web app for tracking optimal visit times in UC Berkeley's Recreational Sports Facility. It utilizes a script to scrape publicly available data that is used to build a Plotly graph representing the daily trend.

I am currently migrating the data collection pipeline to the cloud, using AWS Lambda functions to collect and process data in DynamoDB tables, using an S3 bucket for long term data storage. Another feature is exploring time-series forecasting methods to make predictions about optimal visit times.

Below is an example of a graph displayed and used for analysis. It could use more data.

<img width="1425" alt="Screenshot 2024-01-08 at 5 56 51 PM" src="https://github.com/jerliang/rsf-data-visualizer/assets/37273788/6765c89d-2926-4765-b9b7-d8e422d3a31c">
