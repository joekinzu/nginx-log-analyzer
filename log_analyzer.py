#!/usr/bin/env python
# -*- coding: utf-8 -*-


# log_format ui_short '$remote_addr  $remote_user $http_x_real_ip [$time_local] "$request" '
#                     '$status $body_bytes_sent "$http_referer" '
#                     '"$http_user_agent" "$http_x_forwarded_for" "$http_X_REQUEST_ID" "$http_X_RB_USER" '
#                     '$request_time';

import re 
import time

config = {
    "REPORT_SIZE": 1000,
    "REPORT_DIR": "./reports",
    "LOG_DIR": "./log"
}


def main():
    logdict = []
    сtotal = 0
    btotal = 0
    with open("4") as f:
        for l in f:
            сtotal += 1
            btotal += float(l.split(' ')[-1])
            # btotal += float(re.split(r' ', l)[-1])
    print(сtotal)
    print(btotal)

    start=time.time()

    with open("4") as f:
        for l in f:
            data = l.split(' ')
            url = data[7]
            byte = float(data[-1])
            if not any(url in d for d in logdict):
                logdict.append({url: byte, 'count': 1, 'count_perc': (1/сtotal)*100, 'time_perc': (byte/btotal)*100, 'time_avg': byte, 'time_max': byte})
            else:
                for d in range(len(logdict)):
                    if url in logdict[d]:
                        logdict[d]['count'] +=  1
                        logdict[d]['count_perc'] = (logdict[d]['count']/сtotal)*100
                        logdict[d][url] += byte
                        logdict[d]['time_perc'] = (logdict[d][url]/btotal)*100
                        logdict[d]['time_avg'] = (logdict[d][url]/logdict[d]['count'])
                        logdict[d]['time_max'] = logdict[d]['time_max'] if logdict[d]['time_max'] > byte else byte     
    print ("time", time.time()-start)
    
    # write to file
    with open("bla.txt", "w") as f:
        for s in logdict:
            f.write(str(s) +"\n")
        
        
if __name__ == "__main__":
    main()
