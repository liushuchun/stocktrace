'''
Created on 2011-3-7

@author: simon
'''
import sys, traceback
from datetime import date
from datetime import datetime
from datetime import timedelta
from stock import Stock
from lxml import etree
from lxml.html import parse
from dao.stockdao import *
from lxml import etree
from lxml.html import parse
import io    
    
#parse stock statistics data from BB finance
def parseKeyStatData(code):        
    url = 'http://www.bloomberg.com/quote/'+code+':CH'   
        
    page = parse(url).getroot()
    #result = etree.tostring(page)
    #print result
    r = page.xpath('//table[@class="key_stat_data"]');
    tree= etree.ElementTree(r[0])  
    #print etree.tostring(tree)
    stats = tree.xpath('//td[@class="company_stat"]')
#    for stat in stats:
#        print stat.text
    pe = stats[0].text
    estimatedPe = stats[1].text
    marketCap = stats[5].text
    pb = stats[9].text
    ps = stats[10].text    
    updateTickerWithKeyStats(code,pe,pb,ps,marketCap)

                    
if __name__ == '__main__':
#    stocks = ['600327','600739','600573','600583','600718','600827','601111','601866','600880']
#    parseKeyStatData('600000')
    stocks = findAllExistentTickers()
    for stock in stocks:
       parseKeyStatData(stock)
#    for stock in stocks:
#        getHistorialData(stock)
#    getHistorialData('600383',True,'2011-01-01')