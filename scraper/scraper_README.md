# Scraper README

## DHS_scraper.py

This scraper simulates a browser to search [this DHS site](https://apps.state.or.us/cf2/spd/facility_complaints/). It searches the online database for all NF, ALF and RCF complaints that occured between 01-01-1995 and 3-26-2017. 

The scrape first puts into a spreadsheet a list of all facilities that match the search, with a count of total complaints and a link to their complaint pages. That info is exported into a csv at the end of the scrape. The scraper then goes to each facility's individual page and scrapes abuse_number, the dates, and outcomes. 

## Scraper Verification.ipynb

For the manual verification process, I went to the page and put in the exact same search parameters as the scrape. I copy-pasted the results into a spreadsheet and cleaned them up. Then I added the 'total complaints.' The number was off from my scrape by a hanful of complaints. I checked the ones that didn't match. In each of those cases, the 'total complaints' in the search did not match the actual number of complaints shown on the facility page. 

I used two scrape outputs for this analysis, one from 3/25/2017 and another form 3/29/2017.
