import json
import requests

CardNumber = 9900000067544760269
CardNumber = str(CardNumber)

baseURL = 'https://gcdev.matas.dk'

# get card series number and total cards

getCardSeriesNumberAPI = baseURL + f'/v1/series/listPagination?query={CardNumber}&start=0&limit=10'
print(getCardSeriesNumberAPI)

getCardSeriesNumberAPIResponse = requests.get(getCardSeriesNumberAPI, timeout=20, verify=False)
print(getCardSeriesNumberAPIResponse)

