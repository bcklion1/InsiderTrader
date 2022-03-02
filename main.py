import math
import pandas
from pastData import pastData,pastProfits

sheet2=pandas.read_html("http://openinsider.com/screener?s=&o=&pl=1&ph=&ll=&lh=&fd=7&fdr=&td=7&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=25&vh=&ocl=5&och=&sic1=-1&sicl=100&sich=9999&grp=2&nfl=&nfh=&nil=2&nih=&nol=1&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1")
#test data companies

sheet1=pandas.read_html("http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=1&fdr=&td=3&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=&vh=&ocl=5&och=&sic1=-1&sicl=100&sich=9999&isofficer=1&iscob=1&isceo=1&ispres=1&iscoo=1&iscfo=1&isgc=1&isvp=1&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1")
#individial

# sheet2=pandas.read_html("http://openinsider.com/screener?s=&o=&pl=1&ph=&ll=&lh=&fd=1&fdr=&td=3&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=25&vh=&ocl=5&och=&sic1=-1&sicl=100&sich=9999&grp=2&nfl=&nfh=&nil=2&nih=&nol=1&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1")
#cluster buys

companies=[]
print(sheet2[11].get("ΔOwn"))
sheet1perc=sheet1[11].get("ΔOwn")
sheet2perc=sheet2[11].get("ΔOwn")

#individual buys
if  isinstance(sheet1perc,pandas.core.series.Series):
    for i,j in enumerate(sheet1perc):
            companies.append((sheet1[11]["Ticker"][i],f"{int(j[1:-1])}%",1))
    
else:
    print("no insider trades")
    
#cluster buys
if  isinstance(sheet2perc,pandas.core.series.Series):
    for i,j in enumerate(sheet2perc):
        companies.append((sheet2[11]["Ticker"][i],f"{int(j[1:-1])}%",sheet2[11]["Ins"][i]))
else:
    print("no company trades")
    
# print(sheet2[11])
print(companies)
interest=(pastData(companies[0][0],companies[0][1],companies[0][2]))
print(interest.index)
print(interest.iloc(""))
print(pastProfits(interest))


