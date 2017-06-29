import re
import subprocess
import graphitesend

website = "8.8.8.8"
ping = subprocess.Popen(["ping", "-n", "-c 1", website], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, error = ping.communicate()
if out:
	time = int(re.findall(r"time=(\d+)", out)[0])
	g = graphitesend.init(prefix="ping", system_name='')
	g.send("8_8_8_8",time)

