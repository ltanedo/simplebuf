import simplebuf

RECORD_NAME   = "Option"
REPEATED_NAME = "Example"
MESSAGE_NAME  = "Option_Chains"

simplebuf.create(
        RECORD_NAME   = RECORD_NAME,
        REPEATED_NAME = REPEATED_NAME,
        MESSAGE_NAME  = MESSAGE_NAME, 
        FIELDS = [
            {"name" : "putCall",          "type" : "str"},
            {"name" : "quoteTimeInLong",  "type" : "int"},
            {"name" : "exchangeName",     "type" : "str"},
            {"name" : "symbol",           "type" : "str"},
            {"name" : "underlying",       "type" : "str"},
            {"name" : "bidPrice",         "type" : "float"},
            {"name" : "askPrice",         "type" : "float"},
            {"name" : "bidSize",          "type" : "int"},
            {"name" : "askSize",          "type" : "int"},
            {"name" : "volatility",       "type" : "float"},
            {"name" : "delta",            "type" : "float"},
            {"name" : "gamma",            "type" : "float"},
            {"name" : "theta",            "type" : "float"},
            {"name" : "vega",             "type" : "float"},
            {"name" : "rho",              "type" : "float"},
            {"name" : "openInterest",     "type" : "int"},
            {"name" : "totalVolume",      "type" : "int"},
            {"name" : "expirationDate",   "type" : "str"},
            {"name" : "daysToExpiration", "type" : "int"},
            {"name" : "strikePrice",      "type" : "float"},
            {"name" : "underlyingPrice",  "type" : "float"}, 
            {"name" : "percentInTheMoney","type" : "float"}, 
        ]
    )


simplebuf.generate(
        RECORD_NAME   = RECORD_NAME, 
        REPEATED_NAME = REPEATED_NAME, 
        MESSAGE_NAME  = MESSAGE_NAME,
        sample = 
            {
                "putCall" : "put",
                "quoteTimeInLong": 1669182918,
                "exchangeName" : "OPRA",
                "symbol" : "AAPL221125C00070000",
                "underlying" : "AAPL",
                "bidPrice" : 0.0,
                "askPrice" : 0.0,
                "bidSize" : 100,
                "askSize" : 100,
                "volatility" : 0.0,
                "delta" : 0.0,
                "gamma" : 0.0,
                "theta" : 0.0,
                "vega" : 0.0,
                "rho" : 0.0,
                "openInterest" : 100,
                "totalVolume" : 100,
                "expirationDate" : "09/23/2020",
                "daysToExpiration" : 100,
                "strikePrice" : 0.0,
                "underlyingPrice" : 0.0, 
                "percentInTheMoney" : 0.0, 
            }
    )

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
            "volatility" : 99.9,
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
        },
        {
            "putCall" : "put",
            "quoteTimeInLong": 1669182918,
            "exchangeName" : "OPRA",
            "symbol" : "asdfhasdfasdfasdfasdfasdf",
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

