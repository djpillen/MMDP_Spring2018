import csv
import requests
import time


# Function to iterate through all results returned by the webdata API
def get_webdata(webdata_url, username, password, webdata=[]):
    results = requests.get(webdata_url, auth=(username, password)).json()
    webdata.extend(parse_results(results))
    # webdata results are paginated; default pagination is 100 results per page
    if results["next"]:
        time.sleep(5)
        get_webdata(results["next"], username, password, webdata=webdata)
    return webdata


# Function to parse out metadata for each WARC file
# Used to flatten results and create unique keys for fields that return multiple values, e.g. locations
def parse_results(results):
    warcs = results["files"]
    result_data = []
    for warc in warcs:
        warc_metadata = {}
        for key, value in warc.items():
            if type(value) == dict:
                for subkey, subvalue in value.items():
                    warc_metadata[subkey] = subvalue
            elif type(value) == list:
                for index, item in enumerate(value):
                    warc_metadata["{}_{}".format(key, index)] = item
            else:
                warc_metadata[key] = value
        result_data.append(warc_metadata)
    return result_data


webdata_base_url = "https://partner.archive-it.org/wasapi/v1/webdata"
username = "ARCHIVE-IT_USERNAME"
password = "ARCHIVE-IT_PASSWORD"

# BASIC REQUEST. RETURNS 100 RESULTS.
results = requests.get(webdata_base_url, auth=(username, password)).json()

# COLLECTION-SPECIFIC REQUEST
collection_number = "ARCHIVE-IT_COLLECTION_NUMBER"  # e.g., 5871
# https://partner.archive-it.org/wasapi/v1/webdata?collection=5871
collection_url = webdata_base_url + "?collection={}".format(collection_number)
results = requests.get(collection_url, auth=(username, password)).json()

# TIME-SPECIFIC REQUEST
begin_date = "2017-01-01"
end_date = "2017-12-31"
# https://partner.archive-it.org/wasapi/v1/webdata?crawl-start-after=2017-01-01&crawl-start-before=2017-12-31
time_specific_url = webdata_base_url + "?crawl-start-after={}&crawl-start-before={}".format(begin_date, end_date)
results = requests.get(time_specific_url, auth=(username, password)).json()

# GET THE DOWNLOAD LOCATION OF THE FIRST WARC
download_location = results["files"][0]["locations"][0]

# EXTRACT METADATA FOR ALL WARCS AND EXPORT TO CSV
all_webdata = get_webdata(webdata_base_url, username, password)
with open("warc_metadata.csv", "w", newline="", encoding="utf-8") as f:
    headers = all_webdata[0].keys()
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(all_webdata)
