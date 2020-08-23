import QuantLib as ql
import math
import sys, os

import functionClass.funcClass as func

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
# setting Hull White parameters
a = 0.01 # Hull White Model parameter
sigma = 0.10 # Hull White Model parameter

# setting option
strike  = 0.01 / 100
forward = 0.01 / 100
#vol     = 0.10 for sigma
Notional = 10000.00
optionType = ql.Option.Call
optionStartDate = calendar.advance(settlementDate, 6, ql.Months) 
optionMatulity = calendar.advance(optionStartDate, 6, ql.Months)

# Hull White
a = 0.01 # Hull White Model parameter
sigma = 0.10 # Hull White Model parameter

bf_bl_hw = func.blackFormulaForBackwardLookingTermRateInHullWhiteModel()

capletPrice = bf_bl_hw.price(optionType, 
                            settlementDate, 
                            optionStartDate, 
                            optionMatulity, 
                            strike,
                            forward,
                            a,
                            sigma)

discuountFactor = tmpYieldCurve.discount(optionMatulity)
capletPrice = discuountFactor * capletPrice * Notional

print('capletPrice =', capletPrice)