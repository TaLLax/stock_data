from googlefinance import getQuotes
import simplejson as json
from time import gmtime, strftime
import time
import sqlite3
print (json.dumps(getQuotes('NVDA'), indent=2))
data=json.loads(json.dumps(getQuotes('NVDA'), indent=2))
#x=strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

while(True):
    data=json.loads(json.dumps(getQuotes('NVDA'), indent=2))
    while(True):
        h=strftime("%H", gmtime())
        h=int(h)
        h +=1
        m=strftime("%M", gmtime())
        m=int(m)
        s=strftime("%S", gmtime())
        s=int(s)
        if m < 0:
            while(True):
            
            
                h=strftime("%H", gmtime())
                h=int(h)
                h +=1
                m=strftime("%M", gmtime())
                m=int(m)
                s=strftime("%S", gmtime())
                s=int(s)
                
                time.sleep(1)
                if m >= 35:
                    break
                print(m,s,h)

        #db = sqlite3.connect(r"D:\\aaa.db")
        connection = sqlite3.connect(r"D:\\aaTa.db")

        cursor = connection.cursor()
        tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='stock_data'"
    # delete 
    #cursor.execute("""DROP TABLE employee;""")

        sql_command = """
        CREATE TABLE stock_data (
        staff_number INTEGER PRIMARY KEY,
        ID VARCHAR (30), 
        StockSymbol VARCHAR (30), 
        Index1 VARCHAR (30), 
        LastTradePrice VARCHAR (30), 
        LastTradeWithCurrency VARCHAR (30),
        LastTradeTime VARCHAR (30),
        LastTradeDateTime VARCHAR (30),
        LastTradeDateTimeLong VARCHAR (30));"""
        if not connection.execute(tb_exists).fetchone():
            cursor.execute(sql_command)

       
        ID=data[0]["ID"]
        StockSymbol=data[0]["StockSymbol"]
        Index1=data[0]["Index"]
        LastTradePrice=data[0]["LastTradePrice"]
        LastTradeWithCurrency=data[0]["LastTradeWithCurrency"]
        LastTradeTime=data[0]["LastTradeTime"]
        LastTradeDateTime=data[0]["LastTradeDateTime"]
        LastTradeDateTimeLong=data[0]["LastTradeDateTimeLong"]
        neuedaten=[ID,StockSymbol,Index1,LastTradePrice,LastTradeWithCurrency,LastTradeTime,LastTradeDateTime,LastTradeDateTimeLong]
        #print(neuedaten)
        
        #sql_command = """INSERT INTO stock_data (staff_number,ID,StockSymbol,Index1,LastTradePrice,LastTradeWithCurrency,LastTradeTime,LastTradeDateTime,LastTradeDateTimeLong,Dividend,Yield)
        #VALUES (NULL, data[0]["ID"],data[0]["StockSymbol"],data[0]["Index1"],data[0]["LastTradePrice"],data[0]["LastTradeWithCurrency"],
        #data[0]["LastTradeTime"],data[0]["LastTradeDateTime"],data[0]["LastTradeDateTimeLong"],data[0]["Dividend"],data[0]["Yield"]);"""
        #cursor.execute("INSERT INTO stock_data (staff_number,ID,StockSymbol,Index1,LastTradePrice,LastTradeWithCurrency,LastTradeTime,LastTradeDateTime,LastTradeDateTimeLong)"
        #"VALUES (NULL, :ID,:StockSymbol ,:Index , :LastTradePrice,:LastTradeWithCurrency,:LastTradeTime,:LastTradeDateTime,:LastTradeDateTimeLong,)",json.loads(...)[data])

        
       # sql_command = """INSERT INTO stock_data (staff_number,ID,StockSymbol,Index1,LastTradePrice,LastTradeWithCurrency,LastTradeTime,LastTradeDateTime,LastTradeDateTimeLong)
        #VALUES (NULL, "{ID}","StockSymbol" ,"Index1" ,"LastTradePrice","LastTradeWithCurrency","LastTradeTime","LastTradeDateTime","LastTradeDateTimeLong");"""

        #sql_command = "INSERT INTO stock_data (staff_number,ID,StockSymbol,Index1,LastTradePrice,LastTradeWithCurrency,LastTradeTime,LastTradeDateTime,LastTradeDateTimeLong)"
        
        #cursor.execute(sql_command)
        cursor.execute("INSERT INTO stock_data VALUES (NULL, ?,?,?,?,?,?,?,?)",neuedaten)
        

    # never forget this, if you want the changes to be saved:
        connection.commit()

        connection.close()     
        break
        time.sleep(60)
        #print (json.dumps(getQuotes('AAPL'), indent=2))

     
