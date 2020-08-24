#!/usr/bin/env python

'''
coding challenge-insight-2020-data-engineering-admission
Tasks for this python program: 
Each line in the output file should list the following fields in the following order:
product(name should be in lower case and year)
1. total number of complaints received for that product and year 
2. total number of companies receiving at least one complaint for 
   that product and year 
3. highest percentage (rounded to the nearest whole number) of total  
   complaints filed against one company for that product and year
   i.e., Any percentage between 0.5% and 1%, inclusive, should round
   to 1% and anything less than 0.5% should round to 0%)
'''

import csv, sys
import datetime as dt


''' First Step:1- Read input file '''
Year = []    # Received year of each complaints.
Product = [] # Product name. 
Company = [] # Company name.
Case = []    # Case includes information about (year, product and company) of each complaint.

filename = 'complaints.csv'
with open(filename, newline='') as f:
    
    reader = csv.reader(f)
    header = next(reader)
    try:
        for row in reader:
            
            yr = dt.datetime.strptime(row[0],'%Y-%m-%d').year
            Year.append(yr)
            Product.append(row[1].lower())    
            Company.append(row[7].lower())
            Case.append([yr,row[1].lower(),row[7].lower()])


    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

    finally:
        f.close()

Product.sort()  # Product should be sorted alphabetically
Year.sort()   # Year should be listed in chronological order
Case.sort()


'''Second Step:2- Create dictionaries ''' 
''' and you may have a Look of the keys & values by uncomment ptint command '''

## Dictionary of Year 
dic_Y = {}
for key in Year:                   #Here we make a dictionary for year and the key are elements and value  of the 
                                   #year is counted in each list
    dic_Y[key] = dic_Y.get(key, 0) +1
    
#    print(dic_Y)

## Dictionary of Product
dic_P = {}
for key in Product:
    
    dic_P[key] = dic_P.get(key, 0) + 1
    
# print(dic_P)


''' Third Step:3-Data analysis and save the output '''

''' Loop-1. Product'''
for key_P in dic_P.keys():
        
    ''' Loop-2. Year'''
    for key_Y in dic_Y.keys():
        
        num = 0    # Task1: total number of complaints received for that product and year.
        company = []   # company name.
        for data in Case:
            
            if data[0] == key_Y and data[1] == key_P:
                num = num +1
                company.append(data[2])
                
        if num !=0:   
            
            ## Create a company dictionary to obtain answers for Task 2 and 3.
            dic_co = {}
            for key in company:
                dic_co[key] = dic_co.get(key, 0)+1
            num_co = len(dic_co)
            percentage = round(max(dic_co.values())/num*100)
            
            ## Add double quotation marks to product name if there is a comma (,) .
            if ',' in key_P:
                key_P_p = '\"'+ key_P +'\"'    # Product key for print.
            else:
                key_P_p = key_P
            
            ##  Now, write to 'report.csv’
            with open('report.csv','a', newline = '') as f:
                writer = csv.writer(f)
                writer.writerow([key_P_p, key_Y, num, num_co, percentage])
