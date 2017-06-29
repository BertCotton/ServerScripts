import re
import subprocess
import graphitesend
import datetime
import time

print "Speed test started %s " % datetime.datetime.now()

start = time.time()
try:
	print "Starting speedtest"
	speedtest = subprocess.Popen(["/mnt/scripts/speedtest-linux-amd64-v1.0.2-c"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#speedtest = subprocess.Popen(["cat", "speedtest.log"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print "reading from pipe"
	out, error = speedtest.communicate()
	g = graphitesend.init(prefix="speedtest", system_name='')
	if out:
		ping = float(re.findall(r"Ping \(Lowest\): (\d+\.\d*)", out)[0])
		print "Latency %s ms" % ping
		g.send("ping",ping)

		download = float(re.findall(r"Download \(Max\): (\d+\.\d*)", out)[0])
		print "Download Speed %s Mbit/s" % download
		g.send("download",download)

		upload = float(re.findall(r"Upload \(Max\): (\d+\.\d*)", out)[0])
		print "Upload Speed %s Mbit/s" % upload
		g.send("upload",upload)
	else:
		print "No output from test: %s" % error

except Exception,e:
	print str(e)

end = time.time()
duration = (end - start)
print "Speed test finished %s " % datetime.datetime.now()
print "Duration %s " % duration
