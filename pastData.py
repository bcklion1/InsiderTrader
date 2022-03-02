from datetime import date
import math
import pandas
import yfinance

def pastData(ticker,change,insiders):
    change=int(change[:-1])
    if insiders>1:
        change=math.ceil(((change/insiders)+2))
    pastsheet=pandas.read_html(f"http://openinsider.com/screener?s={ticker}&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1")

    # print(insiders)
    # print(change)
    pastsheetperc=pastsheet[11].get("ΔOwn")
    if pastsheetperc.get(1) != None:
        closest=False
        for count,perc in enumerate(pastsheetperc,1):
            if perc=="New":
                continue
            perc=int(perc[:-1])
            if not closest or abs(perc-change)<closest[0]:
                closest=(abs(perc-change),count-1)
        print(closest) #closest=(difference between amount bought and previous amounts bought,which row that occured)
        mostsimilar=pastsheet[11].iloc[(closest[1])]
        return mostsimilar

def pastProfits(similar):
    ticker=str(yfinance.Ticker(similar.get("Ticker")))
    dateOfTrade=str(similar.get("Trade Date"))
    print(dateOfTrade)
    if int(dateOfTrade[5:7])==11:
        twoMonths=f"{int(dateOfTrade[:5])+1}-01-{dateOfTrade[9:]}"
    elif int(dateOfTrade[5:7])==11:
        twoMonths=f"{int(dateOfTrade[:5])+1}-02-{dateOfTrade[9:]}"
    else:
        twoMonths=dateOfTrade[:5]+str(int(dateOfTrade[5:8])+2)+dateOfTrade[8:]
    
    return twoMonths
    # hist=ticker.download(ticker,start=dateOfTrade,end=)