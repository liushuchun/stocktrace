Revision History
2013/02/05--v0.3
1.screen by Yahoo and support category

2012/09/18--v0.2
1.add django view /zytj/candle

2012/09/11--v0.1
1.Parse history data from Yahoo CSV API
2.Support NHNL screener

stock trace will parse finance data from famous finance web sites and generate some useful report
1.Parse stock data, both realtime and history data from Sina/Yahoo(csv or YDN)/ifeng/Google/reuters  
2.Generate OHLC chart  
3.Screen stocks based on 52 week's high or low percentage


How to run tests:
1. run module
python manage.py test test.yahoo_test
2. run test method
python manage.py test test.yahoo_test.TestSequenceFunctions.test_print_stock



Trade history tracking, stock price notification, compare with worldwide companies.  

Reference:  
https://www.robinhood.com/  
http://www.tradehero.mobi/  





