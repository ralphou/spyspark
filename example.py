#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sample use for main spyspark function

Note there is also a simple console mode for spyspark.py, mostly for testing.

Created on Mon Nov 20 00:33:22 2017

@author: rvitti
"""
import spyspark

query = 'read(zone and air and temp and siteRef->dis=="67")'
test = spyspark.request(query)
with open("test.csv", "w") as f:
    f.write(test)
    
query2 = 'read(zone and air and temp and siteRef->dis=="67")' + \
         '.hisRead(today)'
test_his = spyspark.request(query2)
with open("test_his.csv", "w") as f:
    f.write(test_his)
