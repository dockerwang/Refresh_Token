#!/usr/bin/env python
# -*- coding:utf-8 -*-
##
 #
 
import sys
sys.path.append("../src/")

from CorpApi import *
from TestConf import *

## test
api = CorpApi(TestConf['CORP_ID'], TestConf['CONTACT_SYNC_SECRET'])

try :
    ##
    response = api.httpCall(
            CORP_API_TYPE['USER_CREATE'],
            {
                'userid' : 'wp1',
                'name' : 'wangpeng',
                'mobile' : '15000000000',
                'email' : 'wp@gxnu.edu.cn',
                'department' : 1,
            })
    print(response)

    ##
    response = api.httpCall(
            CORP_API_TYPE['USER_GET'],
            { 
                'userid' : 'wp1',
            })
    print(response)

    ##
    response = api.httpCall(
            CORP_API_TYPE['USER_CREATE'],
            { 
                'userid' : 'wp1',
            })
    print(response)

except ApiException as e :
    print(e.errCode, e.errMsg)

    ##
    response = api.httpCall(
            CORP_API_TYPE['USER_CREATE'],
            { 
                'userid' : 'wp1',
            })
    print(response)


