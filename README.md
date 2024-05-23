# lighthouse-performance-metrics-fetcher
Use this script to fetch Lighthouse performance metrics for a list of URLs specified as slugs in a CSV file. 

## Getting started
It utilizes the Google PageSpeed Insights API to gather data such as Performance Score, First Contentful Paint, Speed Index, Time to Interactive, Total Blocking Time, Largest Contentful Paint & Cumulative Layout Shift.
Script includes error handling to manage cases where no data is returned for a URL, ensuring robustness in data retrieval. 
The extracted metrics are then saved into an output CSV file.

## Usage
Install dependencies: (Python Packages)
- pip install requests
- pip install python-csv
- pip install jsonlib

**Configuration:**
To properly configure and run the Lighthouse Performance Metrics Fetcher script, follow these steps:

- Google PageSpeed Insights API Key:
Obtain your API key from the Google Cloud Console. Ensure that the PageSpeed Insights API is enabled for your project.
Replace the placeholder 'API key' in fetch_metrics.py with your actual API key.

- Base URL:
Define the base URL for your website. This is the root URL to which the slugs from your CSV file will be appended.
Replace the placeholder 'https://example.com' in fetch_metrics.py with your actual base URL.

- CSV Input File:
Prepare a CSV file (slug.csv) with the list of slugs. Each row should contain one slug.
Ensure the file is in the same directory as fetch_metrics.py or provide the correct path to the file.

**Output**
The script generates performance_report.csv with the following columns:

- Slug
- Performance Score
- First Contentful Paint
- Speed Index
- Time to Interactive
- Total Blocking Time
- Largest Contentful Paint
- Cumulative Layout Shift
