import simplebuf

RECORD_NAME   = "Option"
REPEATED_NAME = "Example"
MESSAGE_NAME  = "Option_Chains"

msg = simplebuf.recordsToMessage(
        RECORD_NAME   = RECORD_NAME, 
        REPEATED_NAME = REPEATED_NAME, 
        MESSAGE_NAME  = MESSAGE_NAME,
        data = [ {
            "putCall" : "put",
            "quoteTimeInLong": 1669182918,
            "exchangeName" : "OPRA",
            "symbol" : "AAPL221125C00070000",
            "underlying" : "AAPL",
            "bidPrice" : 1.1,
            "askPrice" : 1.1,
            "bidSize" : 100,
            "askSize" : 100,
            "volatility" : 1.1,
            "delta" : 1.1,
            "gamma" : 1.1,
            "theta" : 1.1,
            "vega" : 1.1,
            "rho" : 1.1,
            "openInterest" : 100,
            "totalVolume" : 100,
            "expirationDate" : "09/23/2020",
            "daysToExpiration" : 100,
            "strikePrice" : 1.1,
            "underlyingPrice" : 1.1, 
            "percentInTheMoney" : 1.1, 
        } ]
    )

new_dict = simplebuf.messageToDict(msg)
new_json = simplebuf.messageToJson(msg)
print(new_dict)

