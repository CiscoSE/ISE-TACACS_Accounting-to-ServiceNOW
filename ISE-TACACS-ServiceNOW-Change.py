#!/usr/bin/python3

"""
Copyright (c) 2018 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import requests
import json
import time
import datetime


# User defined values ServiceNOW
user = 'admin'
pwd = 'C1sco12345!'

# Define Variables and constants for ServiceNOW
ServiceNOW_url = 'https://dev65894.service-now.com/api/now/table/change_request'
ServiceNOW_upload_url = 'https://dev65894.service-now.com/api/now/attachment/file?table_name=change_request&table_sys_id='

#  Headers and mime type text/csv
headers = {"Content-Type":"application/json","Accept":"application/json"}
upload_headers = {"Content-Type":"application/json","Accept":"application/json"}
day = datetime.date.today()
files = open('/var/log/logstash/tacacs-' + str(day), 'rb').read()

def post_servicenow_change():
    sn_response = requests.post(ServiceNOW_url, auth=(user, pwd), headers=headers, \
                                data="{\"type\":\"Normal\", \
                                \"short_description\":\"TACACS Accounting Logs for tacacs-" + str(day) + "\", \
                                \"category\":\"Network\" \
                                }")
    return sn_response.json()

def upload_servicenow_change(id, files):
    sn_response = requests.post(ServiceNOW_upload_url + id + "&file_name=tacacs-" + str(day), auth=(user, pwd), headers=upload_headers, \
                                data=files)
    return sn_response.json()

# Create a change
ret = post_servicenow_change()
# Figure out what the Sys_ID is
sys_id = ret['result']['sys_id']
ret = upload_servicenow_change(sys_id,files)
