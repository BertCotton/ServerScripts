import speedtest
import subprocess
import graphitesend
import datetime
import time

print "Speed test started %s " % datetime.datetime.now()

start = time.time()
try:
	s = speedtest.Speedtest()
	print "Getting Best Server"
	s.get_best_server()
	print "Testing Download Speed"
	s.download()
	print "Testing Upload Speed"
	s.upload()

	results = s.results.dict()
	g = graphitesend.init(prefix="speedtest")
	g.send("ping", results["ping"])
	g.send("download", results["download"])
	g.send("upload", results["upload"])
except Exception,e:
	print str(e)

end = time.time()
duration = (end - start)
print "Speed test finished %s " % datetime.datetime.now()
print "Duration %s " % duration
