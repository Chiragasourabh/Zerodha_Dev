import cherrypy
from jinja2 import Environment, FileSystemLoader
import datetime
import random
import string
import os
import redis

env = Environment(loader=FileSystemLoader('templates'))
env.globals.update(zip=zip)
redisConn = redis.StrictRedis(host="127.0.0.1",port=6379,db=0)

class Root:

    @cherrypy.expose
    def index(self):
        return """<a href="MarketInfo"><h1>Go to MarketInfo!</h1></a>"""

    @cherrypy.expose
    def MarketInfo(self, scname = None):
        tmpl = env.get_template('MarketInfo.html')
        today = datetime.date.today().strftime("%d-%m-%Y")
        answerList = []
        scCodes = []
        if scname:
            matchingNames = redisConn.scan_iter("*"+scname.upper()+"*")
            for name in matchingNames:
                scCode = redisConn.mget(name.decode())[0]
                scCodes.append(scCode)
                answerList.append(redisConn.hmget(scCode.decode(), "SC_NAME", "OPEN", "HIGH", "LOW", "CLOSE"))
        else:
            scCodes = redisConn.lrange('top10Keys', 0, 10)
            for code in scCodes:
                answerList.append(redisConn.hmget(code.decode(), "SC_NAME", "OPEN", "HIGH", "LOW", "CLOSE"))
            
        return tmpl.render(date =  today, code = scCodes, data = answerList)

conf=   {
        "/css": {
            "tools.staticdir.on": True, 
            "tools.staticdir.dir": os.path.abspath("./css")
                }
        }

cherrypy.quickstart(Root(),config=conf)