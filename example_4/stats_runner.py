#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:21:38 2018

@author: Alexander
"""

# Import base libraries
from lcmodel import LC_Initialize, compute_simple_statistics
import pandas as pd
import numpy as np

import logging
import datetime

log_level = logging.INFO
# create logger
logger = logging.getLogger(__name__)
logger.setLevel(log_level)

fh = logging.FileHandler('script_output.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)


# initialise the calculator

# raster = "amz_prode_NA_utm.tif"
# raster = "amz_prode_NA_utm_corrected_only_indian_reserves_masked.tif"

rasterlist = [line.rstrip('\n') for line in open('filelist.txt')]

start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 'Euclidean Nearest-Neighbor Distance' will still blow up,

# ['Edge density',
#                  'Number of Patches',
#                  'Mean patch area',
#                 'Median patch area']
                 
desired_funcs = [
    'Edge length',
    'Edge density',
    'Median patch area',
    'Mean patch perimeter']

# 'Euclidean Nearest-Neighbor Distance'


print("we will work with files: {}".format(rasterlist))
logger.info("we will work with files: {} ".format(rasterlist))

# 'Like adjacencies'
print(desired_funcs)

# initialise empty dict
results_dict = {}
results_dict['year'] = []

for smt in desired_funcs:
    results_dict[smt] = []

for raster in rasterlist:

    # all raster have only one class "2"
    cli=2

    print("initialising with ... {} ... at {}".format(raster, start))
    logger.info("initialising with ... {} ... at {}".format(raster, start))

    lc_calc = LC_Initialize(raster)
    print("doing stuff for lc class {}".format(cli))
    logger.info("doing stuff for lc class {}".format(cli))
    # need to initialise cl_array and labelled_array for current class
    print("initialising labelled array and fcc .. {}".format( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    logger.info("initialising labelled array and fcc .. {}".format( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    lc_calc.create_cl_array_for_class(cli)
    lc_calc.f_ccl(lc_calc.cl_array)

    results_dict['year'].append(raster)

    for smt in desired_funcs:
        print("next metric is {}".format(smt))
        logger.info("next metric is {}".format(smt))
        print("stating metric calculation .. {}".format( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        logger.info("stating metric calculation .. {}".format( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        met_tup = lc_calc.execSingleMetric(smt, cli)
        print(met_tup)
        logger.info("{}".format(met_tup))
        results_dict[smt].append(met_tup[1])
        print("finished this metric calculation .. {}".format( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        logger.info("finished this metric calculation .. {}".format( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

# d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=results_dict)
df.to_csv('lc-stats.csv', sep=';')
print(df.head(5))

