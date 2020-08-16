import QuantLib as ql

# General Setting
calendar = ql.Japan()
settlementDate = ql.Date(28, ql.September, 2018)
settlementDays = 2
today = calendar.advance(settlementDate, -settlementDays, ql.Days)
ql.Settings.instance().setEvaluationDate(today)

# OIS rate
ovn1dRate = ql.SimpleQuote(0.073 / 100.0)
ovnTnRate = ql.SimpleQuote(0.073 / 100.0)
ois1WRate = ql.SimpleQuote(0.073 / 100.0)
ois2WRate = ql.SimpleQuote(0.073 / 100.0)
ois3WRate = ql.SimpleQuote(0.073 / 100.0)
ois1MRate = ql.SimpleQuote(0.074 / 100.0)
ois2MRate = ql.SimpleQuote(0.075 / 100.0)
ois3MRate = ql.SimpleQuote(0.076 / 100.0)
ois4MRate = ql.SimpleQuote(0.077 / 100.0)
ois5MRate = ql.SimpleQuote(0.078 / 100.0)
ois6MRate = ql.SimpleQuote(0.079 / 100.0)
ois7MRate = ql.SimpleQuote(0.080 / 100.0)
ois8MRate = ql.SimpleQuote(0.080 / 100.0)
ois9MRate = ql.SimpleQuote(0.081 / 100.0)
ois10MRate = ql.SimpleQuote(0.081 / 100.0)
ois11MRate = ql.SimpleQuote(0.082 / 100.0)
ois12MRate = ql.SimpleQuote(0.083 / 100.0)
ois15MRate = ql.SimpleQuote(0.087 / 100.0)
ois18MRate = ql.SimpleQuote(0.092 / 100.0)
ois2YRate = ql.SimpleQuote(0.1010 / 100.0)
ois3YRate = ql.SimpleQuote(0.1373 / 100.0)
ois4YRate = ql.SimpleQuote(0.1800 / 100.0)
ois5YRate = ql.SimpleQuote(0.2325 / 100.0)
ois6YRate = ql.SimpleQuote(0.3181 / 100.0)
ois7YRate = ql.SimpleQuote(0.4375 / 100.0)
ois8YRate = ql.SimpleQuote(0.5425 / 100.0)
ois9YRate = ql.SimpleQuote(0.6465 / 100.0)
ois10YRate = ql.SimpleQuote(0.7400 / 100.0)
ois12YRate = ql.SimpleQuote(0.9725 / 100.0)
ois15YRate = ql.SimpleQuote(1.1875 / 100.0)
ois20YRate = ql.SimpleQuote(1.4800 / 100.0)
ois25YRate = ql.SimpleQuote(1.6125 / 100.0)
ois30YRate = ql.SimpleQuote(1.6625 / 100.0)

# Yield Curve Construction
# Setting JPY OverNight, TONAR
oisDayCounter = ql.Actual365Fixed()
jpyON = 'Tonar'
tonar = ql.OvernightIndex(jpyON,
                          0,
                          ql.JPYCurrency(),
                          ql.Japan(),
                          ql.Actual365Fixed())

# Setting OverNightRate
overNight1D = ql.DepositRateHelper(ql.QuoteHandle(ovn1dRate),
                                   ql.Period(1, ql.Days),
                                   settlementDays,
                                   calendar,
                                   ql.ModifiedFollowing,
                                   False,
                                   oisDayCounter)

# Setting OverNightIndexSwap(OIS)Rate
tn2D = ql.OISRateHelper(settlementDays,
                        ql.Period(2, ql.Days),
                        ql.QuoteHandle(ovnTnRate),
                        tonar)

ois1W = ql.OISRateHelper(settlementDays,
                        ql.Period(1, ql.Weeks),
                        ql.QuoteHandle(ois1WRate),
                        tonar)

ois2W = ql.OISRateHelper(settlementDays,
                        ql.Period(2, ql.Weeks),
                        ql.QuoteHandle(ois2WRate),
                        tonar)

ois3W = ql.OISRateHelper(settlementDays,
                        ql.Period(3, ql.Weeks),
                        ql.QuoteHandle(ois3WRate),
                        tonar)

ois1M = ql.OISRateHelper(settlementDays,
                        ql.Period(1, ql.Months),
                        ql.QuoteHandle(ois1MRate),
                        tonar)

ois2M = ql.OISRateHelper(settlementDays,
                        ql.Period(2, ql.Months),
                        ql.QuoteHandle(ois2MRate),
                        tonar)

ois3M = ql.OISRateHelper(settlementDays,
                        ql.Period(3, ql.Months),
                        ql.QuoteHandle(ois3MRate),
                        tonar)

ois4M = ql.OISRateHelper(settlementDays,
                        ql.Period(4, ql.Months),
                        ql.QuoteHandle(ois4MRate),
                        tonar)

ois5M = ql.OISRateHelper(settlementDays,
                        ql.Period(5, ql.Months),
                        ql.QuoteHandle(ois5MRate),
                        tonar)

ois6M = ql.OISRateHelper(settlementDays,
                        ql.Period(6, ql.Months),
                        ql.QuoteHandle(ois6MRate),
                        tonar)

ois7M = ql.OISRateHelper(settlementDays,
                        ql.Period(7, ql.Months),
                        ql.QuoteHandle(ois7MRate),
                        tonar)

ois8M = ql.OISRateHelper(settlementDays,
                        ql.Period(8, ql.Months),
                        ql.QuoteHandle(ois8MRate),
                        tonar)

ois9M = ql.OISRateHelper(settlementDays,
                        ql.Period(9, ql.Months),
                        ql.QuoteHandle(ois9MRate),
                        tonar)

ois10M = ql.OISRateHelper(settlementDays,
                        ql.Period(10, ql.Months),
                        ql.QuoteHandle(ois10MRate),
                        tonar)

ois11M = ql.OISRateHelper(settlementDays,
                        ql.Period(11, ql.Months),
                        ql.QuoteHandle(ois11MRate),
                        tonar)

ois12M = ql.OISRateHelper(settlementDays,
                        ql.Period(12, ql.Months),
                        ql.QuoteHandle(ois12MRate),
                        tonar)

ois15M = ql.OISRateHelper(settlementDays,
                        ql.Period(15, ql.Months),
                        ql.QuoteHandle(ois15MRate),
                        tonar)

ois18M = ql.OISRateHelper(settlementDays,
                        ql.Period(18, ql.Months),
                        ql.QuoteHandle(ois18MRate),
                        tonar)

ois2Y = ql.OISRateHelper(settlementDays,
                        ql.Period(2, ql.Years),
                        ql.QuoteHandle(ois2YRate),
                        tonar)

ois3Y = ql.OISRateHelper(settlementDays,
                        ql.Period(3, ql.Years),
                        ql.QuoteHandle(ois3YRate),
                        tonar)

ois4Y = ql.OISRateHelper(settlementDays,
                        ql.Period(4, ql.Years),
                        ql.QuoteHandle(ois4YRate),
                        tonar)

ois5Y = ql.OISRateHelper(settlementDays,
                        ql.Period(5, ql.Years),
                        ql.QuoteHandle(ois5YRate),
                        tonar)

ois6Y = ql.OISRateHelper(settlementDays,
                        ql.Period(6, ql.Years),
                        ql.QuoteHandle(ois6YRate),
                        tonar)

ois7Y = ql.OISRateHelper(settlementDays,
                        ql.Period(7, ql.Years),
                        ql.QuoteHandle(ois7YRate),
                        tonar)

ois8Y = ql.OISRateHelper(settlementDays,
                        ql.Period(8, ql.Years),
                        ql.QuoteHandle(ois8YRate),
                        tonar)

ois9Y = ql.OISRateHelper(settlementDays,
                        ql.Period(9, ql.Years),
                        ql.QuoteHandle(ois9YRate),
                        tonar)

ois10Y = ql.OISRateHelper(settlementDays,
                        ql.Period(10, ql.Years),
                        ql.QuoteHandle(ois10YRate),
                        tonar)

ois12Y = ql.OISRateHelper(settlementDays,
                        ql.Period(12, ql.Years),
                        ql.QuoteHandle(ois12YRate),
                        tonar)

ois15Y = ql.OISRateHelper(settlementDays,
                        ql.Period(15, ql.Years),
                        ql.QuoteHandle(ois15YRate),
                        tonar)

ois20Y = ql.OISRateHelper(settlementDays,
                        ql.Period(20, ql.Years),
                        ql.QuoteHandle(ois20YRate),
                        tonar)

ois25Y = ql.OISRateHelper(settlementDays,
                        ql.Period(25, ql.Years),
                        ql.QuoteHandle(ois25YRate),
                        tonar)

ois30Y = ql.OISRateHelper(settlementDays,
                        ql.Period(30, ql.Years),
                        ql.QuoteHandle(ois30YRate),
                        tonar)

# Calculation for JPYOISDF
helpers = []
helpers.append(overNight1D)
helpers.append(tn2D)
helpers.append(ois1W)
helpers.append(ois2W)
helpers.append(ois3W)
helpers.append(ois1M)
helpers.append(ois2M)
helpers.append(ois3M)
helpers.append(ois4M)
helpers.append(ois5M)
helpers.append(ois6M)
helpers.append(ois7M)
helpers.append(ois8M)
helpers.append(ois9M)
helpers.append(ois10M)
helpers.append(ois11M)
helpers.append(ois12M)
helpers.append(ois15M)
helpers.append(ois18M)
helpers.append(ois2Y)
helpers.append(ois3Y)
helpers.append(ois4Y)
helpers.append(ois5Y)
helpers.append(ois6Y)
helpers.append(ois7Y)
helpers.append(ois8Y)
helpers.append(ois9Y)
helpers.append(ois10Y)
helpers.append(ois12Y)
helpers.append(ois15Y)
helpers.append(ois20Y)
helpers.append(ois25Y)
helpers.append(ois30Y)

oisTermStructureDayCounter = ql.Actual365Fixed()
oisTermStructure = ql.PiecewiseLogLinearDiscount(settlementDate,
                                                  helpers,
                                                  oisTermStructureDayCounter)
oisTermStructure.enableExtrapolation() # For Extrapolation

print('JPYOISDF(1D) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(1, ql.Days))))

print('JPYOISDF(TN) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(2, ql.Days))))
# tmp 1
for i in range(0,3):
    print('JPYOISDF(' + str(i+1) +'W) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(i + 1, ql.Weeks))))
# tmp 2
for i in range(0,12):
    print('JPYOISDF(' + str(i+1) +'M) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(i + 1, ql.Months))))

print('JPYOISDF(' + str(15) +'M) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(15, ql.Months))))

print('JPYOISDF(' + str(18) +'M) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(18, ql.Months))))
# tmp 3
for i in range(2,11):
    print('JPYOISDF(' + str(i) +'Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(i, ql.Years))))

print('JPYOISDF(' + str(12) +'Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(12, ql.Years))))

print('JPYOISDF(' + str(15) +'Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(15, ql.Years))))

print('JPYOISDF(' + str(20) +'Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(20, ql.Years))))

print('JPYOISDF(' + str(25) +'Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(25, ql.Years))))

print('JPYOISDF(' + str(30) +'Y) = ', oisTermStructure.discount(calendar.advance(settlementDate, 
                                                                        ql.Period(30, ql.Years))))
