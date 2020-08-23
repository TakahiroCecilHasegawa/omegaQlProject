import QuantLib as ql
import math

# General Setting
calendar = ql.Japan()
settlementDate = ql.Date(28, ql.September, 2018)
settlementDays = 2
today = calendar.advance(settlementDate, -settlementDays, ql.Days)
ql.Settings.instance().setEvaluationDate(today)

# tmp yield curve
tmpYieldCurve = ql.FlatForward(settlementDate, 
                                ql.QuoteHandle(ql.SimpleQuote(0.01 /100)),
                                ql.Actual365Fixed(),
                                ql.Compounded,
                                ql.Continuous)

# setting option
strike  = 0.01 / 100
forward = 0.01 / 100
vol     = 0.10
Notional = 10000.00
optionType = ql.Option.Call
optionStartDate = calendar.advance(settlementDate, 6, ql.Months) 
optionMatulity = calendar.advance(optionStartDate, 6, ql.Months)

capletPrice = ql.blackFormula(optionType, 
                                strike, 
                                forward, 
                                vol * math.sqrt((optionMatulity - optionStartDate) / 360))

discuountFactor = tmpYieldCurve.discount(optionMatulity)
capletPrice = discuountFactor * capletPrice * Notional

print('capletPrice =', capletPrice)