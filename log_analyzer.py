import re 
import time
import pandas as pd 
import numpy as np


def main():
    ctotal = 0
    btotal = 0
    dict1 = {}
    df = pd.DataFrame(columns=('URL', 'Time'))

    start=time.time()

    with open('2.log') as f:
        for l in f:
            data = l.split(' ')
            ctotal += 1
            url = data[7]
            btotal += float(data[-1])
            # count, count perc, data, data perc, data avg, data max
            dict1[ctotal] = [url, float(data[-1])]


    print('total rows: ',ctotal)
    print('total data: ',btotal)

    # df = pd.DataFrame.from_dict(dict1, orient='index', columns=['URL', 'Count', 'Count %', 'Time', 'Time %', 'Time AVG', 'Time MAX'])
    df = pd.DataFrame.from_dict(dict1, orient='index', columns=['URL','Time'])

    df = (df.groupby('URL').agg({'Time': ["count", sum, "mean", max, "median"]}))
    # df.to_json('file.json', orient = 'split', compression = 'infer', index = 'true') 

    df.to_csv('result.csv') 
    print(df)
    

    print ("time", time.time()-start)


        
        
if __name__ == "__main__":
    main()
