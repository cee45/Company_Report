import requests
import json
import pandas as pd
from openpyxl import load_workbook
import numpy as np

#Indivdual ID
td_consumer_key = 'S0EQ4NG1V2LRXAMAE4BSLCD7TLGWNNQW'

#Add Ticker Symbol
ticker = 'BRK.B'


base_url = 'https://api.tdameritrade.com/v1/instruments?&symbol={stock_ticker}&projection={projection}'

endpoint = base_url.format(stock_ticker = ticker,
            projection='fundamental')
page = requests.get(url=endpoint,
            params={'apikey' : td_consumer_key})
content = json.loads(page.content)

#print(content[ticker].keys())
description = content[ticker]['description']

fundamental = content[ticker]['fundamental']

#print(fundamental.keys())

symbol = fundamental['symbol']
#Technicals
high52 = fundamental['high52']
low52 = fundamental['low52']

#Dividend
dividendamount = fundamental['dividendAmount']
dividendyield = fundamental['dividendYield']
dividenddate = fundamental['dividendDate']
dividendpayamount = fundamental['dividendPayAmount']
dividendpaydate = fundamental['dividendPayDate']
dividend_growth_rate = fundamental['divGrowthRate3Year']

#Ratios
price_to_earnings = fundamental['peRatio']
price_earningsgrowth = fundamental['pegRatio']
price_to_book = fundamental['pbRatio']
price_sales = fundamental['prRatio']
price_cashflow = fundamental['pcfRatio']
quick_ratio = fundamental['quickRatio']
current_ratio = fundamental['currentRatio']

#Financials
gross_margin = fundamental['grossMarginTTM']
margin_percent = fundamental['netProfitMarginTTM']
operating_margin = fundamental['operatingMarginTTM']
gross_marginQtr = fundamental['grossMarginMRQ']
net_profit_marginQtr = fundamental['netProfitMarginMRQ']
operation_marginQtr = fundamental['operatingMarginMRQ']
return_on_equity = fundamental['returnOnEquity']
return_on_assets = fundamental['returnOnAssets']
return_on_investment = fundamental['returnOnInvestment']

interest_coverage = fundamental['interestCoverage']
total_debt_to_capital = fundamental['totalDebtToCapital']
longterm_debt_equity = fundamental['ltDebtToEquity']
total_debt_equity = fundamental['totalDebtToEquity']
eps = fundamental['epsTTM']
eps_changeTTM = fundamental['epsChangePercentTTM']
epsyoy = fundamental['epsChangeYear']
epsyoypct = fundamental['epsChange']
revenue_change = fundamental['revChangeYear']
revenueyoy = fundamental['revChangeTTM']
revenueyoypct = fundamental['revChangeIn']
shares_outstanding = fundamental['sharesOutstanding']
marketcapfloat = fundamental['marketCapFloat']
marketcap = fundamental['marketCap']
bookvalue_pershare =fundamental['bookValuePerShare']
shortinvtofloat = fundamental['shortIntToFloat']
shortintdaytocover = fundamental['shortIntDayToCover']

#Volitility
beta = fundamental['beta']
vol1dayavg = fundamental['vol1DayAvg']
vol10dayavg = fundamental['vol10DayAvg']
vol3monthavg = fundamental['vol3MonthAvg']

#print(description)
#df = pd.DataFrame([operating_margin])

#print(beta)

#print(fundamental.keys())

'''[symbol, high52, low52, marketcap, shares_outstanding, marketcapfloat, beta,
 dividendamount, dividendyield, dividenddate, dividend_growth_rate, dividendpayamount, dividendpaydate,
 price_to_earnings, price_earningsgrowth, price_to_book, price_sales, price_cashflow,
 gross_margin, margin_percent, operating_margin, gross_marginQtr, net_profit_marginQtr, operation_marginQtr,
 return_on_equity, return_on_assets, return_on_investment, quick_ratio, current_ratio,
 interest_coverage, total_debt_to_capital, longterm_debt_equity, total_debt_equity, bookvalue_pershare,
 eps, eps_changeTTM, epsyoy, epsyoypct,
 revenue_change, revenueyoy, revenueyoypct, shortinvtofloat, shortintdaytocover,
 vol1dayavg, vol10dayavg, vol3monthavg],'''


"""df = pd.DataFrame(np.array([symbol, high52, low52, marketcap, shares_outstanding, marketcapfloat, beta,
                            dividendamount, dividendyield, dividenddate, dividend_growth_rate, dividendpayamount, dividendpaydate,
                            price_to_earnings, price_earningsgrowth, price_to_book, price_sales, price_cashflow,
                            gross_margin, margin_percent, operating_margin, gross_marginQtr, net_profit_marginQtr, operation_marginQtr,
                            return_on_equity, return_on_assets, return_on_investment, quick_ratio, current_ratio,
                            interest_coverage, total_debt_to_capital, longterm_debt_equity, total_debt_equity, bookvalue_pershare,
                            eps, eps_changeTTM, epsyoy, epsyoypct,
                            revenue_change, revenueyoy, revenueyoypct, shortinvtofloat, shortintdaytocover,
                            vol1dayavg, vol10dayavg, vol3monthavg]),
                    index=['symbol', 'high52', 'low52',  'marketCap', 'shares_outstanding',
                        'marketcapfloat', 'beta',
                        'dividendAmount', 'dividendYield', 'dividendDate', 'divGrowthRate3Year',
                        'dividendPayAmount', 'dividendPayDate',
                        'price_to_earnings', 'price_earningsgrowth', 'price_to_book', 'price_sales',
                        'price_cashflow',
                        'gross_margin', 'margin_percent', 'operating_margin', 'grossMarginQtr',
                        'net_profit_marginQtr', 'operation_marginQtr',
                        'returnOnEquity', 'returnOnAssets', 'returnOnInvestment',
                        'quickRatio', 'currentRatio',
                        'interestCoverage', 'totalDebtToCapital', 'longterm_debt_equity',
                        'total_debt_equity', 'bookvalue_pershare',
                        'eps', 'epsChangePercentTTM', 'epsyoy', 'epsyoypct',
                        'revenue_change', 'revenueyoy', 'revenueyoypct',
                        'shortIntToFloat', 'shortIntDayToCover',
                        'vol1DayAvg', 'vol10DayAvg', 'vol3MonthAvg'])

df_T = df.T
print(df_T)

#df_T.to_excel('/Users/christopher/Documents/template.xlsx',index=False,header=True,sheet_name='Data')"""

print(content)

print(dividend_growth_rate)
print(return_on_equity)