'''
This scraper grabs all the complaints from DHS's long-term care complaints site. This version grabs the following fields:

abuse number 
city
facility 
incident date 
investigation complete date 
facility type 
allegation 
outcome 

The purpose of this scraper is to compare it to the data we got from the state.

'''

from __future__ import print_function
import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime
from random import randint
from time import sleep


startTime = datetime.now()

fac_types = ['RCF','ALF', 'NF ']
list_of_complaints=[]
totals_list_for_export = []
link_list_for_export = []

for fac_type in fac_types:
    browser = RoboBrowser(history = True, parser='lxml')
    url = 'https://apps.state.or.us/cf2/spd/facility_complaints/'

    browser.open(url)
    form = browser.get_form(action = 'act_ComplaintSelection.cfm')
    form['txtBeginDate']='01/01/1995'
    form['txtEndDate']='03/26/2017'
    form['ProviderCategory'] = fac_type

    browser.submit_form(form)
    content = browser.parsed

    link_list = []
    totals_list = []
    facility_names = []

    for row in content.find_all(text = re.compile('^\s+\d{1,3}\s+$')):
        totals_list.append(row.strip())
        totals_list_for_export.append(row.strip())

    for row in content.find_all('a', attrs={'href': re.compile("^dsp_details.cfm")}):
        link_list.append(row.get('href'))
        link_list_for_export.append(row.get('href'))
    
    df = pd.DataFrame(totals_list, link_list).reset_index()
    columns = ('link','total_complaints')
    df.columns = columns

    for row in df['link']:
        browser.open('https://apps.state.or.us/cf2/spd/facility_complaints/'+row)
        content = browser.parsed
        provider_complaints = []
        rec_num = len(provider_complaints)

        for report in content.find_all('b', text = re.compile('Report Number:')):
        
            abuse_record = {
                  "fac_name": content.find_all('b')[1].getText() if fac_type =='NF ' else content.find_all('b')[0].getText(),
                  "city_name": content.find_all('b')[2].getText() if fac_type=='NF ' else content.find_all('b')[1].getText(),
                  "load_of_info": content.find_all('td', width='75%')[0].getText(),
                  "fac_type": fac_type,
                  "abuse_number":report,
                }

            provider_complaints.append(abuse_record)
            rec_num = len(provider_complaints)

            date_record = {
                "online_incident_date": content.find_all(text = re.compile('\d{2}/\d{2}/\d{4}'))[rec_num*2-2],
                "inv_comp_date": content.find_all(text = re.compile('\d{2}/\d{2}/\d{4}'))[rec_num*2-1],
                "abuse_number":report,
                }

            record = dict(date_record.items() | abuse_record.items())
            list_of_complaints.append(record)

data = pd.DataFrame(list_of_complaints)
data['abuse_number'] = data['abuse_number'].astype(str)
data['abuse_number'] = data['abuse_number'].apply(lambda x: x.split(' ')[3])
#data['allegation'] = data['load_of_info'].apply(lambda x: x.split('\xa0 ')[2])
#data['outcome'] = data['load_of_info'].apply(lambda x: x.split('\xa0 ')[4])
data.drop('load_of_info',1, inplace = True)


'''
Export csv with complaints
'''
data.to_csv('/Users/fzarkhin/OneDrive - Advance Central Services, Inc/fproj/github/database-story/data/scraped/scraped_complaints_4_19.csv', index = False)
'''
Export csv with total complaints per facility, as per the site itself.
'''
pd.DataFrame(totals_list_for_export, link_list_for_export).reset_index().to_csv('/Users/fzarkhin/OneDrive - Advance Central Services, Inc/fproj/github/long-term-care/scraped_data/scraped_complaint_totals_4_19.csv')

#How long did all of this take?
print (datetime.now() - startTime)
