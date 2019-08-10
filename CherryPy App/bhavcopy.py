from io import BytesIO,StringIO
from zipfile import ZipFile
from urllib.request import urlopen
from urllib.error import HTTPError
import datetime
import redis
import os
import pandas as pd
redisConn = redis.from_url(os.environ.get("REDIS_URL",'redis:'))
d = datetime.date.today() 
csvData = ""
if d.isoweekday() in range(1, 6):
    file_url = "https://www.bseindia.com/download/BhavCopy/Equity/EQ"+d.strftime("%d%m%y")+"_CSV.ZIP"
    # file_url = "https://www.bseindia.com/download/BhavCopy/Equity/EQ090819_CSV.ZIP"
    try:
        resp = urlopen(file_url)
    except HTTPError as e:
        print(e)
        print("Script Execution Failed on "+d.strftime("%d-%m-%Y"))
    else:
        zipfile = ZipFile(BytesIO(resp.read()))
        for line in zipfile.open(zipfile.namelist()[0]).readlines():
            csvData+=line.decode('utf-8')
        data = pd.read_csv(StringIO(csvData), sep=",")
        data.sort_values("OPEN", axis=0, ascending=False, inplace=True, kind='quicksort', na_position='last')
        dataDict = data[['SC_NAME', 'OPEN', 'HIGH', 'LOW', 'CLOSE']].to_dict('records')
        SC_CODEList = data[['SC_CODE']].values.tolist()
        SC_NameList = data[['SC_NAME']].values.tolist()
        top10Keys = SC_CODEList[:10]
        top10Keys.reverse()
        redisConn.flushall()
        redisConn.mset({"date":d.strftime("%d-%m-%Y")})
        redisConn.lpush('top10Keys', *[item[0] for item in top10Keys])
        dictionary = {index[0]: value for index,value in zip(SC_CODEList,dataDict)}
        for SC_CODE, item in dictionary.items():
            redisConn.hmset(SC_CODE, item) 
        returnDict = {}
        for name, code in zip(SC_NameList,SC_CODEList):
            returnDict[name[0]] = code[0]
        redisConn.mset(returnDict)
        print("Script Execution Successful on "+d.strftime("%d-%m-%Y"))