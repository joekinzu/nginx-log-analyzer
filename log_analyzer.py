#!/usr/bin/env python
# -*- coding: utf-8 -*-


# log_format ui_short '$remote_addr  $remote_user $http_x_real_ip [$time_local] "$request" '
#                     '$status $body_bytes_sent "$http_referer" '
#                     '"$http_user_agent" "$http_x_forwarded_for" "$http_X_REQUEST_ID" "$http_X_RB_USER" '
#                     '$request_time';

import re 
import time

CONFIG = {
    "REPORT_SIZE": 1000,
    "REPORT_DIR": "./reports",
    "LOG_DIR": "./log"
}

# round float digit
def round_float(d):
    return round(d, 3)

# find perc
def perc(d, d1):
    return round_float((d/d1)*100)

# find median
def median(ar):
	sorted(ar)
	n = len(ar)
	# if n % 2 == 1:
	return ar[n//2] if 1>0 else (ar[n//2]+ar[n//2-1])/2

# get lastest filename within folder
def get_file_date(file_path):
	file_date = 1
	return file_path

# get url, request time from nginx log
def parse_data(filename):
	logdict = {}
	ctotal = 0
	btotal = 0

	with open(filename) as f:
		for l in f:
		    data = l.split(' ')
		    ctotal += 1
		    btotal += float(l.split(' ')[-1])
		    logdict[ctotal] = [data[7], float(data[-1])]
	
	return sorted(logdict.items(), key=lambda x: x[1]), ctotal, round_float(btotal)

# write to file
def write_dict_to_file(filename, dict1):
	with open(filename, 'w') as filename:
		for s in dict1:
			filename.write(str(dict1[s]) +"\n")


def main():
	filename = '2.log'
	logdict = {}
	res = {}
	ctotal = 0
	btotal = 0
	count = 0
	tim = 0
	median_array = []
	ss = {}

	start=time.time()

	logdict, ctotal, btotal = parse_data(filename)
	print('total rows: ',ctotal)
	print('total data: ',btotal)

	# with open("bla1.txt", "w") as f:
	#     for s in logdict:
	#         f.write(str(s) +"\n")


	for s in logdict:
	    # print(s[1][0])
	    if ss != s[1][0]:
	        cnt = 1
	        tim = s[1][1]
	        median_array = [tim]
	        count += 1
	        res[count] = {'url':s[1][0],'count': cnt, 'count_perc': perc(cnt,ctotal), 'time_sum': tim, 'time_perc': perc(tim, btotal), 'time_avg': tim, 'time_max': tim, 'time_median': tim}
	        ss = s[1][0]
	        m = tim
	    else:
	        cnt += 1
	        tim = tim + s[1][1]
	        median_array.append(s[1][1])
	        m = m if m > s[1][1] else s[1][1]
	        res[count].update(count = cnt, time_sum = round_float(tim), time_avg =  round_float(tim/cnt), time_max = m, count_perc = perc(cnt,ctotal), time_perc =  perc(tim, btotal), time_median = len(median_array))
	 
	print ('time: ', round_float(time.time()-start))

	# write to file
	write_dict_to_file(CONFIG['REPORT_DIR']+'/'+'result.json', res)
        
        
if __name__ == "__main__":
    main()
