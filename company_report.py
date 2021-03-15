import pandas as pd
from configparser import ConfigParser
import pickle as pkl
import requests, os, re
from openpyxl import load_workbook
from urllib.request import urlopen
import json



config = ConfigParser()
config.read('auth.ini')
fmp_key = config.get('auth', 'fmp_key')


symbol = "BMY"
timeframe = "annual"
millions = 1000000


def income_statement(ticker=symbol, api_key=fmp_key, period=timeframe,statement="income-statement"):
    
    data = requests.get("https://financialmodelingprep.com/api/v3/" + 
                        statement+ "/" +symbol + "?period=" + period + "&apikey=" + api_key)
    data = data.json()

    data = data[0:5]

    #revenue = data[0]['revenue']/millions

    return data


def balance_sheet(ticker=symbol, api_key=fmp_key, period=timeframe,statement="balance-sheet-statement"):
        
    data = requests.get("https://financialmodelingprep.com/api/v3/" +
                        statement + "/" + symbol + "?period=" + period + "&apikey=" + api_key)
    data = data.json()

    data = data[0:5]

    return data


def cash_flow_statement(ticker=symbol, api_key=fmp_key, period=timeframe,statement="cash-flow-statement"):
    
    data = requests.get("https://financialmodelingprep.com/api/v3/" +
                           statement + "/" + symbol + "?period=" + period + "&apikey=" + api_key)
    data = data.json()

    data = data[0:5]

    return data


def quote(ticker=symbol,statement='quote',api_key=fmp_key):
    data = requests.get("https://financialmodelingprep.com/api/v3/" +
                        statement + "/" + symbol + "?apikey=" + api_key)
    data = data.json()

    price = data[0]['price']
    market_cap = data[0]['marketCap']
    shares_outstanding = data[0]['sharesOutstanding']


    return price, market_cap, shares_outstanding


def growth_ratios(ticker=symbol):

    IS_data = income_statement(symbol)

    #Revenue Growth
    rev_new = IS_data[0]['revenue']/millions
    rev_old = IS_data[1]['revenue']/millions
    rev_change = '{:,.2%}'.format(((rev_new-rev_old)/rev_old))

    #Net Income Growth
    income_new = IS_data[0]['netIncome']/millions
    income_old = IS_data[1]['netIncome']/millions
    income_change = '{:,.2%}'.format(((income_new-income_old)/income_old))

    #Net Income Growth
    eps_new = IS_data[0]['eps']
    eps_old = IS_data[1]['eps']
    eps_change = '{:,.2%}'.format(((eps_new-eps_old)/eps_old))

    #EBITDA
    ebitda_new = IS_data[0]['ebitda']
    ebitda_old = IS_data[1]['ebitda']
    ebitda_change = '{:,.2%}'.format(((ebitda_new-ebitda_old)/ebitda_old))

    #Dividend Growth Rate
    
    return rev_change, income_change, eps_change, ebitda_change, eps_new, eps_old

def key_ratios(ticker=symbol):

    IS_data = income_statement(symbol)
    BS_data = balance_sheet(symbol)
    #CF_data = cash_flow_statement(symbol)

    #IncomeStatement
    rev = IS_data[0]['revenue']
    COGS = IS_data[0]['costOfRevenue']
    gross_profit = IS_data[0]['grossProfit']
    research_development = IS_data[0]["researchAndDevelopmentExpenses"]
    general_administrative = IS_data[0]["generalAndAdministrativeExpenses"]
    operating_expenses = IS_data[0]["operatingExpenses"]
    depreciation_amortization = IS_data[0]["depreciationAndAmortization"]
    ebitda = IS_data[0]['ebitda']
    operating_income = IS_data[0]["operatingIncome"]
    other_income_expense = IS_data[0]["totalOtherIncomeExpensesNet"]
    ebt = IS_data[0]["incomeBeforeTax"]
    income_tax_expense = IS_data[0]["incomeTaxExpense"]
    net_income = IS_data[0]['netIncome']
    eop_share_outstanding_dil = IS_data[0]["weightedAverageShsOutDil"]  
    eps = net_income/eop_share_outstanding_dil

    #BalanceSheet
    #Assets
    cash_and_cash_equivalents = BS_data[0]['cashAndCashEquivalents']
    short_term_investments = BS_data[0]['shortTermInvestments']
    cash_and_short_term_investments = BS_data[0]['cashAndShortTermInvestments']
    inventory = BS_data[0]['inventory']
    current_assets = BS_data[0]['totalCurrentAssets']
    property_plant_equipment = BS_data[0]['propertyPlantEquipmentNet']
    goodwill = BS_data[0]['goodwill']
    intangible_assets = BS_data[0]['intangibleAssets']
    long_term_investments = BS_data[0]['longTermInvestments']
    tax_assets = BS_data[0]['taxAssets']
    total_Non_Current_assets = BS_data[0]['totalNonCurrentAssets']
    total_assets = BS_data[0]['totalAssets']

    #liabilites
    account_payable = BS_data[0]['accountPayables']
    short_term_debt = BS_data[0]['shortTermDebt']
    deferred_revenue = BS_data[0]['deferredRevenue']
    current_liabilities = BS_data[0]['totalCurrentLiabilities']
    long_term_debt = BS_data[0]['longTermDebt']
    total_non_current_liabilities = BS_data[0]['totalNonCurrentLiabilities']
    total_liabilities = BS_data[0]['totalLiabilities']

    #Shareholder Equity
    common_stock = BS_data[0]['commonStock']
    retained_earnings = BS_data[0]['retainedEarnings']
    totalStockholderEquity = BS_data[0]['totalStockholdersEquity']

    total_liabilites_shareholder_equity = BS_data[0]['totalLiabilitiesAndStockholdersEquity']


    #Quick Ratio
    quick_ratio = (cash_and_cash_equivalents + short_term_investments) / current_liabilities
    
    #Current Ratio
    current_ratio = current_assets/ current_liabilities

    #Debt/Equity
    Debt_Equity = total_liabilities/totalStockholderEquity

    #Debt/Asset
    Debt_Asset = total_liabilities/total_assets
    
    #Return on Equity
    #net_income/totalStockholderEquity
    #Return on Assets
    net_income/total_assets
        
    #Return on Capital
    net_income/(total_assets-current_liabilities)

    #Price to Earnings
        #price_per_share/eps

    #Forward Price to Earnings
        #price_per_share/(forward_eps)

    #Price to Earnings Growth Ratio
        #PriceEarningsRatio/ExpectedRevenueGrowth

    #Adjusted Price to Earnings Growth Ratio
        #PE/((Revenue*Expected Reveune Growth)*(%Cost of Sales)

    #Price to Sales
        #Share Price/(rev/eop_share_outstanding_dil)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

    #Price to Book
        #Price/(totalStockHolderEquity/eop_share_outstanding_dil)

    #Price to Cash Flow
        #Price/(operatingCashFlow/eop_share_outstanding_dil)

    #Price to Free Cash Flow
        #marketCap/freeCashFlow

    #Gross Margin

    #Operating Margin

    #Net Profit Margin

    #Enterprise Value
        #(marketCap - cashAndCashEquivalents +totalDebt)

    #Enterprise Value to Sales
        #enterpriseValue/revenue

    #Enterprise Value to Operating Cash Flow
        #enterpriseValue/operatingCashflow

    #Enterprise Value to EBITDA
        #enterpriseValue/ebitda
    return  quick_ratio

def dcf(ticker=symbol):
    pass


#rev_new = income_statement()[0]['revenue']/millions
#print(key_ratios())
#print(income_statement())
