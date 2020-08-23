import QuantLib as ql
import math

class blackFormulaForBackwardLookingTermRateInHullWhiteModel:
    
    def price(self, optionType, valuationDate, startDate, matulity, strike, forward, a, sigma):
        
        _T = 0.0
        if valuationDate < startDate:
            _T = 1/(2*a)*(((1-math.exp(-a*(matulity-startDate)/360))/a)**2)*(1-math.exp(-2*a*(startDate-valuationDate)/360))
            +1/(a**2)*((matulity-startDate)/360+2/a*math.exp(-a*(matulity-startDate)/360)-1/(2*a)*math.exp(-2*a*(matulity-startDate)/360)-3/(2*a)) 
        else:
            _T = 1/(a**2)*((matulity-valuationDate)/360+2/a*math.exp(-a*(matulity-valuationDate)/360)-1/(2*a)*math.exp(-2*a*(matulity-valuationDate)/360)-3/(2*a))
        
        _stdDev = sigma*math.sqrt((_T/360))
        _delta = (matulity-startDate)/360
        _price = ql.blackFormula(optionType, 1+strike*_delta, 1+forward*_delta, _stdDev) / _delta
        
        return _price

if __name__ == '__main__':
    bf_bl_hw = blackFormulaForBackwardLookingTermRateInHullWhiteModel()
    
    # test set
    calendar = ql.Japan()
    settlementDate = ql.Date(28, ql.August, 2019)
    settlementDays = 2
    today = calendar.advance(settlementDate, -settlementDays, ql.Days)
    ql.Settings.instance().setEvaluationDate(today)
    
    optionType = ql.Option.Call
    strike  = 0.01 / 100
    forward = 0.01 / 100
    a = 0.01 # Hull White Model parameter
    sigma = 0.10 # Hull White Model parameter
    notional = 10000.00
    
    optionStartDate = calendar.advance(settlementDate, 6, ql.Months) 
    optionMatulity = calendar.advance(optionStartDate, 6, ql.Months)

    print('price test (v < s < t)= ', bf_bl_hw.price(optionType, 
                                        settlementDate, 
                                        optionStartDate, 
                                        optionMatulity, 
                                        strike, 
                                        forward, 
                                        a, 
                                        sigma) * notional)
    
    settlementDate = calendar.advance(optionStartDate, 1, ql.Months)
    settlementDays = 2
    today = calendar.advance(settlementDate, -settlementDays, ql.Days)
    ql.Settings.instance().setEvaluationDate(today)
    print('price test (s < v < t)= ', bf_bl_hw.price(optionType, 
                                        settlementDate, 
                                        optionStartDate, 
                                        optionMatulity, 
                                        strike, 
                                        forward, 
                                        a, 
                                        sigma) * notional)