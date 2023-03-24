import os
from datetime import datetime
import time

for i in range(50):
    print(i)
    cmd = "../wrk2/wrk -D exp -t 10 -c 10 -d 30 -L -s ./wrk2/scripts/social-network/compose-post.lua http://10.10.1.1:8080/wrk2-api/post/compose -R 10"
    os.system(cmd)
    ts = "jaeger-traces/s100/" + str(datetime.now().strftime("%Y%m%d%H%M%S"))
    print(ts)
    ret = "curl -s 'http://10.10.1.1:16686/api/traces?service=compose-post-service&lookback=1m&prettyPrint=true&limit=200' > " + ts
    os.system(ret)
    time.sleep(30)