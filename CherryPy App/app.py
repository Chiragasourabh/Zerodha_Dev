import cherrypy
from jinja2 import Environment, FileSystemLoader
import datetime
import random
import string
import os
import redis

env = Environment(loader=FileSystemLoader('templates'))
env.globals.update(zip=zip)
redisConn = redis.from_url(os.environ.get("REDIS_URL",'redis:'))

class Root:

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        today = datetime.date.today().strftime("%d-%m-%Y")
        bhavday = redisConn.mget("date")[0].decode()
        return tmpl.render(today =  today, bhavday = bhavday)
        # return """<a href="MarketInfo"><h1>Go to MarketInfo!</h1></a>"""

    @cherrypy.expose
    def MarketInfo(self, scname = None):
        tmpl = env.get_template('MarketInfo.html')
        today = datetime.date.today().strftime("%d-%m-%Y")
        answerList = []
        scCodes = []
        bhavday = redisConn.mget("date")[0].decode()
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
            
        return tmpl.render(today =  today, bhavday = bhavday, code = scCodes, data = answerList)

conf=   {
        "/css": {
            "tools.staticdir.on": True, 
            "tools.staticdir.dir": os.path.abspath("./css")
                }
        }

cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(Root(),config=conf)