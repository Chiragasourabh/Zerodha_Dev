import cherrypy
from jinja2 import Environment, FileSystemLoader
import datetime
import random
import string
import os

env = Environment(loader=FileSystemLoader('templates'))

class Root:

    @cherrypy.expose
    def index(self):
        return """<a href="MarketInfo"><h1>Go to MarketInfo!</h1></a>"""

    @cherrypy.expose
    def MarketInfo(self, length=8):
        tmpl = env.get_template('MarketInfo.html')
        today = datetime.date.today().strftime("%d-%m-%Y")
        jsondict = [{"code": 1689486, "name": "zdcvzrretw", "open": 1848, "high": 1173, "low": 1758, "close": 1320}, {"code": 1121348, "name": "xrdeicragj", "open": 1518, "high": 1059, "low": 1957, "close": 1582}, {"code": 1540229, "name": "vsxtnnmccs", "open": 1672, "high": 1994, "low": 1088, "close": 1115}, {"code": 1296105, "name": "dfzwymgodt", "open": 1138, "high": 1545, "low": 1207, "close": 1915}, {"code": 1005583, "name": "ricsomluli", "open": 1609, "high": 1874, "low": 1787, "close": 1332}, {"code": 1537976, "name": "xuvgmkqalu", "open": 1001, "high": 1288, "low": 1896, "close": 1531}, {"code": 1588605, "name": "kxgvjiasxv", "open": 1712, "high": 1613, "low": 1049, "close": 1810}, {"code": 1097495, "name": "ogvyxyvhnx", "open": 1610, "high": 1755, "low": 1190, "close": 1281}, {"code": 1216148, "name": "utapsfjjto", "open": 1892, "high": 1416, "low": 1392, "close": 1508}, {"code": 1917835, "name": "naxnxqesdy", "open": 1961, "high": 1079, "low": 1389, "close": 1774}, {"code": 1082580, "name": "tssfuqmsou", "open": 1031, "high": 1063, "low": 1244, "close": 1774}, {"code": 1877137, "name": "lvtejmxbma", "open": 1633, "high": 1848, "low": 1999, "close": 1553}, {"code": 1698907, "name": "sqqsvubljk", "open": 1324, "high": 1224, "low": 1471, "close": 1779}, {"code": 1350046, "name": "gcexzifvuz", "open": 1057, "high": 1066, "low": 1516, "close": 1542}, {"code": 1130141, "name": "crlvvbmoto", "open": 1005, "high": 1211, "low": 1504, "close": 1071}, {"code": 1902609, "name": "appukhlgmg", "open": 1939, "high": 1399, "low": 1045, "close": 1566}, {"code": 1322998, "name": "mxsamwfyds", "open": 1435, "high": 1171, "low": 1076, "close": 1122}, {"code": 1796390, "name": "hejlhfzjsj", "open": 1703, "high": 1994, "low": 1772, "close": 1091}, {"code": 1774009, "name": "fhaasmkgpy", "open": 1237, "high": 1237, "low": 1822, "close": 1495}, {"code": 1662527, "name": "ydlxvokwqq", "open": 1483, "high": 1060, "low": 1227, "close": 1179}, {"code": 1198610, "name": "ticvherayi", "open": 1196, "high": 1234, "low": 1643, "close": 1545}, {"code": 1392706, "name": "pkgxuctour", "open": 1872, "high": 1944, "low": 1229, "close": 1088}, {"code": 1500184, "name": "myyyisjyex", "open": 1363, "high": 1410, "low": 1296, "close": 1989}, {"code": 1861385, "name": "jwigbmhwmj", "open": 1766, "high": 1548, "low": 1351, "close": 1213}, {"code": 1766215, "name": "dscvuaifhk", "open": 1166, "high": 1277, "low": 1967, "close": 1285}, {"code": 1843370, "name": "wuoidtouuu", "open": 1534, "high": 1475, "low": 1475, "close": 1721}, {"code": 1784286, "name": "eptnijpixd", "open": 1196, "high": 1425, "low": 1506, "close": 1718}, {"code": 1071982, "name": "fshfvfjice", "open": 1025, "high": 1263, "low": 1757, "close": 1864}, {"code": 1213863, "name": "reigvedixd", "open": 1419, "high": 1334, "low": 1514, "close": 1782}, {"code": 1900782, "name": "gpzrlugrps", "open": 1209, "high": 1499, "low": 1501, "close": 1967}, {"code": 1579086, "name": "avnkvsguni", "open": 1346, "high": 1166, "low": 1982, "close": 1660}, {"code": 1585629, "name": "mtfcfyoyca", "open": 1947, "high": 1146, "low": 1292, "close": 1861}, {"code": 1320641, "name": "mrvzqazkth", "open": 1525, "high": 1469, "low": 1108, "close": 1307}, {"code": 1733395, "name": "wbokxtxbpz", "open": 1148, "high": 1160, "low": 1286, "close": 1919}, {"code": 1121106, "name": "xufwfwfthz", "open": 1954, "high": 1684, "low": 1720, "close": 1732}, {"code": 1797466, "name": "ffbgwtgzpc", "open": 1385, "high": 1159, "low": 1829, "close": 1806}, {"code": 1718608, "name": "cdasudssjr", "open": 1980, "high": 1097, "low": 1386, "close": 1783}, {"code": 1660595, "name": "plugjzmhgi", "open": 1455, "high": 1541, "low": 1006, "close": 1227}, {"code": 1405569, "name": "viphnhrbgh", "open": 1516, "high": 1329, "low": 1065, "close": 1622}, {"code": 1771354, "name": "coyvjgkyxz", "open": 1477, "high": 1491, "low": 1536, "close": 1242}, {"code": 1535470, "name": "dzjdzjpncc", "open": 1781, "high": 1494, "low": 1308, "close": 1102}, {"code": 1634101, "name": "ifhfmvrctc", "open": 1118, "high": 2000, "low": 1856, "close": 1908}, {"code": 1147908, "name": "bpkrtokjac", "open": 1464, "high": 1333, "low": 1266, "close": 1656}, {"code": 1104409, "name": "yfucuqpsfi", "open": 1366, "high": 1273, "low": 1518, "close": 1132}, {"code": 1386646, "name": "jmdiiwroxf", "open": 1239, "high": 1326, "low": 1949, "close": 1182}, {"code": 1369065, "name": "hprnlgbhsh", "open": 1308, "high": 1640, "low": 1756, "close": 1957}, {"code": 1268046, "name": "gfgcyduned", "open": 1120, "high": 1297, "low": 1614, "close": 1156}, {"code": 1114921, "name": "xbcwkpvcbq", "open": 1836, "high": 1129, "low": 1152, "close": 1278}, {"code": 1579038, "name": "jwhhthrmnl", "open": 1908, "high": 1974, "low": 1367, "close": 1767}, {"code": 1727452, "name": "kuvwsrrryi", "open": 1124, "high": 1010, "low": 1734, "close": 1113}]
        return tmpl.render(date =  today, data = jsondict[:int(length)])

conf=   {
        "/css": {
            "tools.staticdir.on": True, 
            "tools.staticdir.dir": os.path.abspath("./css")
                }
        }

cherrypy.quickstart(Root(),config=conf)