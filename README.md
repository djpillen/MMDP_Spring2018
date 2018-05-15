# Managing, Preserving, and Describing Web Archives Using Archive-It, DPN, and ArchivesSpace - MMDP Spring 2018

This repository contains some example Python scripts and JSON responses for working with the Archive-It WASAPI data transfer and partner metadata APIs to support a presentation at the Mid-Michigan Digital Practitioners Spring 2018 meeting.

The full presentation can be viewed here: https://goo.gl/RJxi4r

## WASAPI Data Transfer API

The Archive-It webdata API implements a WASAPI data transfer API for Archive-I that "supports working with both web archive files (WARCs) as well as with derivate files" and provides access to all WARC files in the Archive-It repository to "relevant, authenticated Archive-It partners."

The script `wasapi_webdata_api.py` shows how to authenticate against the webdata API and includes a few example queries, including querying for collection-specific WARCs and for crawls started during a specific time period, and an example of how to use the API to get all WARC metadata for a given Archive-It account and to save that metadata to a CSV.

The file `example_webdata.json` includes the JSON returned by the webdata API for a single file.

Further documentation about WASAPI and the Archive-It implementation can be found at the following URLs. 

* WASAPI: https://github.com/WASAPI-Community/data-transfer-apis
* Archive-It documentation: https://github.com/WASAPI-Community/data-transfer-apis/tree/master/ait-specification

## Partner Metadata API

The Archive-It partner metadata API allows Archive-It partners to query the API used internally by the Archive-It system to perform create, read, update, and delete actions against Archive-It partner metadata, including for collections, seeds, crawl definitions, jobs, etc.

The script `archive_it_partner_api.py` shows how to authenticate against the partner metadata API and includes a few example queries, including a query for a specific seed and a query for all of the seeds associated with a given Archive-It collection, and examples of how to parse out publicly accessible seeds, actively captured seeds, and unique subjects associated with seeds.

The file `example_seed.json` includes the JSON returned from the Archive-It partner metadat API for a single seed.