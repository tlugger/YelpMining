import csv
import pandas as pd


#http://stackoverflow.com/questions/3979077/how-can-i-convert-a-string-to-an-int-in-python
def convertStr(s):
    """Convert string to either int or float."""
    try:
        ret = float(s)
    except ValueError:
        #It's a String.
        ret = s
    return ret

#creates the avg weather value based on both rows
def getAvgWeatherVal(s1,s2):
    tmp=0
    #CLOUD COVERAGE TYPES BUILDS BASE VALUE
    if 'CLR' in s1:
        tmp=5
    if 'FEW' in s1:
        tmp=4.5
    if 'SCT' in s1:
        tmp=4
    if 'BKN' in s1:
        tmp=3.5
    if 'OVC' in s1:
        tmp=3
    if ' OVC' in s1:
        tmp=3.5
    if '15' in s1:
        tmp=2.5
    if '26' in s1:
        tmp=2
    if '23' in s1:
        tmp=2.5
    if '57' in s1:
        tmp=2.5
    if '41' in s1:
        tmp=2.5

    #WEATHER CONDITIONS MODIFY VALUE
    if 'RA:02 ' in s2:
        tmp=tmp-2
    if 'SN:03 ' in s2:
        tmp=tmp-3
    if 'HZ:7 ' in s2:
        tmp=tmp-1
    if 'BR:1 ' in s2:
        tmp=tmp-1
    if 'GR' in s2:
        tmp=tmp-3
    if 'FG:2 ' in s2:
        tmp=tmp-1.5
    if 'SG' in s2:
        tmp=tmp-2.5
    if 'DZ:01' in s2:
        tmp=tmp-1.5

    return tmp
        

##Removes empty rows from a fresh data file
with open("pitt2016.csv", 'r') as inp, open('edit.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    #gets rid of SOD
    for row in csv.reader(inp):
        #nodata 
        if row[6] != "SOD" :
            writer.writerow(row)

##Removes rows with undesireable times
with open("edit.csv", 'r') as inp, open('dates.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    #for dates
    for row in csv.reader(inp):
        #taks out 11PM-4:59AM
        if ' 0:' not in row[5] and ' 1:' not in row[5] and ' 2:' not in row[5] and ' 3:' not in row[5] and ' 4:' not in row[5] and ' 23:' not in row[5] and ' 24:' not in row[5]:
            writer.writerow(row)


##fills in nans with appropriate values

df = pd.read_csv("dates.csv")
df['HOURLYSKYCONDITIONS'].fillna('CLR',inplace=True)
df['HOURLYPRSENTWEATHERTYPE'].fillna('0',inplace=True)
df.to_csv('filleddates.csv', sep=',')

tmp=0
with open("filleddates.csv", 'r') as inp, open('avgweather.csv', 'w', newline='') as out:
    writer = csv.writer(out, lineterminator='\n')

    for row in csv.reader(inp):
        ##needs implementation still refer to LCD_documentation for weather types vs data representation
        ##here need to convert HOURLYSKYCONDITIONS and HOURLYPRESENTWEATHERTYPE
        ##to a value representing what we think is the "average weather rating"
        ##this will write to avgweather.csv
        writer.writerow([getAvgWeatherVal(row[8],row[10])])
        
        
##At this point the hourly average weather rating is in the csv avgweather.csv
# with an extra 0 at the top
#cut and pasted this row into DAILYSunset in avgthis.csv for convinience
#next run createdailyaverages.py to get daily averages from avgthis.csv
#these daily averages will be in avgdailyweather.csv
##README has more clarification
        

##before you do this you need to add the new column to the data fram
##this will make a daily average for weather and add each daily
##daily average weather value to the stars dataframe that has daily average stars            

#dailyavgweather=df.groupby('DATE')['AVGWEATHER'].mean()
#stars=pd.read_csv('stars.csv')
#dailyavgweather=df.groupby('DATE')['AVGWEATHER'].mean()
#stars["avg_weather"] = dailyavgweather


        
