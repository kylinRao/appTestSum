#! /usr/bin/env python 
#coding=utf-8 
import redis

print redis.__file__
# 连接，可选不同数据库 
r = redis.Redis(host='127.0.0.1', port=6379)

# ------------------------------------------- 
# 看信息 
info = r.info()
for key in info:
  print "%s: %s" % (key, info[key])

# 查数据库大小 
print '\ndbsize: %s' % r.dbsize()

# 看连接 
print "ping %s" % r.ping()

# 选数据库 
#r.select(2)
print "start to work on redis!!"
for i in range(1,100):
        print i
        r.set("R_{i}".format(i=i),i-1)

for key in r.keys("R_*"):
        print "delete {key}".format(key = key)
        r.delete(key)
~                        
