# # Adapted from: http://godelsmarket.blogspot.co.uk/2012/07/non-gui-ib-historical-data-downloader.html
#
# from time import sleep, strftime, localtime
# from ib.ext.Contract import Contract
# from ib.opt import ibConnection, message
#
# new_symbolinput = ['GOOG']
# newDataList = []
# dataDownload = []
#
# def historical_data_handler(msg):
#   global newDataList
#   print msg.reqId, msg.date, msg.open, msg.high, msg.low, msg.close, msg.volume
#   if ('finished' in str(msg.date)) == False:
#     new_symbol = new_symbolinput[msg.reqId]
#     dataStr = '%s, %s, %s, %s, %s, %s, %s' % (new_symbol, strftime("%Y-%m-%d %H:%M:%S", localtime(int(msg.date))), msg.open, msg.high, msg.low, msg.close, msg.volume)
#     newDataList = newDataList + [dataStr]
#   else:
#     new_symbol = new_symbolinput[msg.reqId]
#     filename = 'minutetrades' + new_symbol + '.csv'
#     csvfile = open('csv_day_test/' + filename,'wb')
#     for item in newDataList:
#       csvfile.write('%s \n' % item)
#     csvfile.close()
#     newDataList = []
#     global dataDownload
#     dataDownload.append(new_symbol)
#
# con = ibConnection()
# con.register(historical_data_handler, message.historicalData)
# con.connect()
#
# symbol_id = 0
# for i in new_symbolinput:
#   print i
#   qqq = Contract()
#   qqq.m_symbol = i
#   qqq.m_secType = 'STK'
#   qqq.m_exchange = 'SMART'
#   qqq.m_currency = 'USD'
#   con.reqHistoricalData(symbol_id, qqq, '', '1 D', '1 min', 'TRADES', 1, 2)
#   symbol_id = symbol_id + 1
#   sleep(0.5)
#
# print dataDownload

from ib.ext.Contract import Contract
from ib.ext.Order import Order
from ib.opt import ibConnection, message
from time import sleep

def watchAll(msg):
    print(msg)

con = ibConnection()
con.registerAll(watchAll)
con.connect()
sleep(1)

fx = Contract()
fx.m_secType = "CASH"
fx.m_symbol = "USD"
fx.m_currency = "CAD"
fx.m_exchange = "IDEALPRO"
con.reqMktData(1,fx,"",False)

ord = Order()
ord.m_orderType = 'MKT'
ord.m_totalQuantity = 100000
ord.m_action = 'BUY'
ord.m_transmit = False
con.placeOrder(1234,fx,ord)