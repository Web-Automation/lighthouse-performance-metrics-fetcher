import requests
import json
import csv

# Replace with your actual API key
API_KEY = 'API key'

# Replace with your base URL
BASE_URL = 'https://example.com' 

# Fetches Lighthouse data for a given URL using the Google PageSpeed Insights API
def fetch_lighthouse_data(url, api_key):
    # Construct the API endpoint URL
    endpoint = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}"
    response = requests.get(endpoint) # Make the API reques
    if response.status_code == 200: # Check if the response status is 200 (OK)
        return response.json() # Return the JSON data
    else:
        print(f"Failed to fetch data for {url}, Status code: {response.status_code}")  # Print an error message if the request fails
        return None # Return None if the request fails

# Parses relevant performance metrics from the Lighthouse data
def parse_lighthouse_data(data):
    if not data:  # Check if data is None
        print("No data received from API.")
        return None # Return None if data is None

    lighthouse_result = data.get("lighthouseResult", {}) # Extract the Lighthouse result section
    categories = lighthouse_result.get("categories", {}) # Extract the categories section
    performance_score = categories.get("performance", {}).get("score", None) # Extract the performance score

    audits = lighthouse_result.get("audits", {}) # Extract the audits section
    fcp = audits.get("first-contentful-paint", {}).get("displayValue", None) # Extract First Contentful Paint
    si = audits.get("speed-index", {}).get("displayValue", None)  # Extract Speed Index
    tti = audits.get("interactive", {}).get("displayValue", None) # Extract Time to Interactive
    tbt = audits.get("total-blocking-time", {}).get("displayValue", None) # Extract Total Blocking Time
    lcp = audits.get("largest-contentful-paint", {}).get("displayValue", None)  # Extract Largest Contentful Paint
    cls = audits.get("cumulative-layout-shift", {}).get("displayValue", None) # Extract Cumulative Layout Shift

    # Return a dictionary of the extracted metrics
    return { 
        "performance_score": performance_score,
        "first_contentful_paint": fcp,
        "speed_index": si,
        "time_to_interactive": tti,
        "total_blocking_time": tbt,
        "largest_contentful_paint": lcp,
        "cumulative_layout_shift": cls
    }


# Main function to fetch slugs from csv file and print Lighthouse performance metrics inside a CSV file
def main():
    # Read slugs from CSV file: Replace the filename (and path if not in same folder) with your csv file having slugs 
    with open('slug.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        with open('performance_report.csv', mode='w', newline='') as output_file:
            fieldnames = ['Slug', 'Performance Score', 'First Contentful Paint', 'Speed Index',
                          'Time to Interactive', 'Total Blocking Time', 'Largest Contentful Paint',
                          'Cumulative Layout Shift']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            # Iterate through each row in the CSV file
            for row in reader:
                slug = row[0]  # Assuming slug is in the first column
                url = f"{BASE_URL}/{slug}"  # Combine base URL and slug to form complete URL
                data = fetch_lighthouse_data(url, API_KEY)
                metrics = parse_lighthouse_data(data) # Parse relevant performance metrics from the data
                if metrics: # If metrics are successfully parsed
                   # Write the metrics to the output CSV file
                    writer.writerow({
                        'Slug': slug,
                        'Performance Score': metrics['performance_score'],
                        'First Contentful Paint': metrics['first_contentful_paint'],
                        'Speed Index': metrics['speed_index'],
                        'Time to Interactive': metrics['time_to_interactive'],
                        'Total Blocking Time': metrics['total_blocking_time'],
                        'Largest Contentful Paint': metrics['largest_contentful_paint'],
                        'Cumulative Layout Shift': metrics['cumulative_layout_shift']
                    })
                else:
                    print(f"No data returned for URL: {url}")  # Print a message if no data was returned for the URL

    print("The Page Speed Insight process has finished, and the report has been generated.")

if __name__ == "__main__":
    main()
