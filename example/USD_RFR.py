import QuantLib as ql

# General Setting
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
settlementDate = ql.Date(19, ql.August, 2020)
settlementDays = 2
today = calendar.advance(settlementDate, -settlementDays, ql.Days)
ql.Settings.instance().setEvaluationDate(today)

# SOFR rates
'''
https://apps.newyorkfed.org/markets/autorates/SOFR
'''
ovn1dRate = ql.SimpleQuote(0.10 / 100.0)

# SOFR Futures 1M
'''
https://www.cmegroup.com/trading/interest-rates/stir/one-month-sofr_quotes_globex.html
'''
SofeFutures_1M_list = [
    {'price':99.92, 'convx':0.0, 'Year':2020, 'Month':9},
    {'price':99.92, 'convx':0.0, 'Year':2020, 'Month':10}
]

# SOFR Futures 3M
'''
https://www.cmegroup.com/trading/interest-rates/stir/three-month-sofr_quotes_globex.html
'''
SofeFutures_3M_list = [
    {'price':99.96, 'convx':0.0, 'Year':2021, 'Month':3},
    {'price':99.97, 'convx':0.0, 'Year':2021, 'Month':6},
    {'price':99.975, 'convx':0.0, 'Year':2021, 'Month':9}
]

# SOFR Swap rates
'''
https://www.cmegroup.com/trading/interest-rates/sofr-strip-rates.html
'''
ois2YRate  = ql.SimpleQuote(0.0294 / 100.0)
ois3YRate  = ql.SimpleQuote(0.0213 / 100.0)
ois5YRate  = ql.SimpleQuote(0.1027 / 100.0)
ois10YRate = ql.SimpleQuote(0.4198 / 100.0)
ois20YRate = ql.SimpleQuote(0.6823 / 100.0)
ois30YRate = ql.SimpleQuote(0.7219 / 100.0)

# Yield Curve Construction
# Setting USD OverNight, SOFR
'''
we do not need to set SOFR because ql.Sofr() exits.
'''

# Setting OverNightRate
overNight1D = ql.DepositRateHelper(ql.QuoteHandle(ovn1dRate),
                                   ql.Period(1, ql.Days),
                                   settlementDays,
                                   ql.UnitedStates(ql.UnitedStates.GovernmentBond),
                                   ql.ModifiedFollowing,
                                   False,
                                   ql.Sofr().dayCounter())

# Setting SOFR futures
SofeFutures_1M_hepler_list = []
for SofeFutures_1M in SofeFutures_1M_list:
    priceQuote = ql.QuoteHandle(ql.SimpleQuote(SofeFutures_1M['price']))
    convexityAdjustmentQuote = ql.QuoteHandle(ql.SimpleQuote(SofeFutures_1M['convx']))
    SofeFutures_1M_hepler_list.append(ql.SofrFutureRateHelper(priceQuote,
                                                        SofeFutures_1M['Month'],
                                                        SofeFutures_1M['Year'],
                                                        ql.Monthly, 
                                                        ql.Sofr(), 
                                                        convexityAdjustmentQuote, 
                                                        ql.OvernightIndexFuture.Averaging))

SofeFutures_3M_hepler_list = []
for SofeFutures_3M in SofeFutures_3M_list:
    priceQuote = ql.QuoteHandle(ql.SimpleQuote(SofeFutures_3M['price']))
    convexityAdjustmentQuote = ql.QuoteHandle(ql.SimpleQuote(SofeFutures_3M['convx']))
    SofeFutures_3M_hepler_list.append(ql.SofrFutureRateHelper(priceQuote,
                                                        SofeFutures_3M['Month'],
                                                        SofeFutures_3M['Year'],
                                                        ql.Quarterly, 
                                                        ql.Sofr(), 
                                                        convexityAdjustmentQuote, 
                                                        ql.OvernightIndexFuture.Compounding))

# Setting OverNightIndexSwap(SOFR Swap)Rate
ois2Y = ql.OISRateHelper(settlementDays,
                        ql.Period(2, ql.Years),
                        ql.QuoteHandle(ois2YRate),
                        ql.Sofr())

ois3Y = ql.OISRateHelper(settlementDays,
                        ql.Period(3, ql.Years),
                        ql.QuoteHandle(ois3YRate),
                        ql.Sofr())

ois5Y = ql.OISRateHelper(settlementDays,
                        ql.Period(5, ql.Years),
                        ql.QuoteHandle(ois5YRate),
                        ql.Sofr())

ois10Y = ql.OISRateHelper(settlementDays,
                        ql.Period(10, ql.Years),
                        ql.QuoteHandle(ois10YRate),
                        ql.Sofr())

ois20Y = ql.OISRateHelper(settlementDays,
                        ql.Period(20, ql.Years),
                        ql.QuoteHandle(ois20YRate),
                        ql.Sofr())

ois30Y = ql.OISRateHelper(settlementDays,
                        ql.Period(30, ql.Years),
                        ql.QuoteHandle(ois30YRate),
                        ql.Sofr())

# Calculation for USDRFRDF
helpers = []
helpers.append(overNight1D)
for SofeFutures_1M_hepler in SofeFutures_1M_hepler_list:
    helpers.append(SofeFutures_1M_hepler)

for SofeFutures_3M_hepler in SofeFutures_3M_hepler_list:
    helpers.append(SofeFutures_3M_hepler)

helpers.append(ois2Y)
helpers.append(ois3Y)
helpers.append(ois5Y)
helpers.append(ois10Y)
helpers.append(ois20Y)
helpers.append(ois30Y)

oisTermStructureDayCounter = ql.Actual360()
oisTermStructure = ql.PiecewiseLogLinearDiscount(settlementDate,
                                                  helpers,
                                                  oisTermStructureDayCounter)
oisTermStructure.enableExtrapolation() # For Extrapolation

print('USDRFRDF(1D) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                    ql.Period(1, ql.Days))))

# TODO DFs calc. method of sofr futures should be researched ...  
for i in range(len(SofeFutures_1M_hepler_list)):
    tmpdays = SofeFutures_1M_hepler_list[i].maturityDate().serialNumber() - settlementDate.serialNumber()
    print('USDRFRDF(futures ' + str(SofeFutures_1M_list[i]['Year']) +'_'+ str(SofeFutures_1M_list[i]['Month']) + ') = ', 
                    oisTermStructure.discount(calendar.advance(settlementDate, 
                                              ql.Period(tmpdays, ql.Days))))     

for i in range(len(SofeFutures_3M_hepler_list)):
    tmpdays = SofeFutures_3M_hepler_list[i].maturityDate().serialNumber() - settlementDate.serialNumber()
    print('USDRFRDF(futures ' + str(SofeFutures_3M_list[i]['Year']) + '_' + str(SofeFutures_3M_list[i]['Month']) + ') = ', 
                    oisTermStructure.discount(calendar.advance(settlementDate, 
                                              ql.Period(tmpdays, ql.Days))))   

print('USDRFRDF(2Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                    ql.Period(2, ql.Years))))
print('USDRFRDF(3Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                    ql.Period(3, ql.Years))))
print('USDRFRDF(5Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                    ql.Period(5, ql.Years))))
print('USDRFRDF(10Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                    ql.Period(10, ql.Years))))
print('USDRFRDF(20Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                    ql.Period(20, ql.Years))))
print('USDRFRDF(30Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                    ql.Period(30, ql.Years))))