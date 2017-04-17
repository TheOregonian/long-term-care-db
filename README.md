# Long-term Care Complaints Data and Analysis

This repo covers the raw data, munging of that data, and analysis that support several 
passages in the story "XXXXXX by The Oregonian/OregonLive.

## Data

These are the datasets relied on for all analyses:

1. Complaints substantiated by the Department of Human Service's Aging and Disabilities 
program against nursing facilities (NF), assisted living facilities (ALF), and residential
 care (RCF) facilities from 2015 to May 2016, with less-reliably complete records in late
 2015 and 2016. 
 
This dataset was munged using the following datasets: 
a) All investigated complaints 2005-early 2016
b) All substantiated complaints (with narratives) 2010-early 2016
c) A lookup table for complaint outcome codes
d) Fifty-two complaints that DHS had mislabelled as unsubstantiated
d) All complaints the department had posted on its searchable database of substantiated 
complaints on March 25, 2017, located here: 
https://apps.state.or.us/cf2/spd/facility_complaints/. The data were scraped using this 
Python code(LINK HERE).
e) Data scraped from the same site, but on April 12, 2017. 


2. All nursing, assisted living and residential care facilities open in September, 2016, 
with characteristics and complaint counts. 

This dataset was munged using the following:
a) The complaints dataset listed above. 
b) All NF/ALF/RCF facilities open in September, 2016
c) Ownership history of all above facilities

## Analyses

- __Passage__: "...state officials have excluded nearly 8,000 substantiated complaints of 
substandard care from the state’s website."
- __Analysis__: This notebook shows our calculations.

***

- __Passage__: "...state officials have excluded nearly 8,000 substantiated complaints of 
substandard care from the state’s website."
- __Analysis__: This notebook shows our calculations.

***

- __Passage__: "...state officials have excluded nearly 8,000 substantiated complaints of 
substandard care from the state’s website."
- __Analysis__: This notebook shows our calculations.

***

- __Passage__: "...state officials have excluded nearly 8,000 substantiated complaints of 
substandard care from the state’s website."
- __Analysis__: This notebook shows our calculations.

## Technical Notes

To re-run the analyses above, you'll need Python 3.X, as well as the Python libraries 
listed in [requirements.txt](requirements.txt).

## Feedback

If you have questions or feedback about the data or analyses, contact Fedor Zarkhin 
at fzarkhin@oregonian.com.
