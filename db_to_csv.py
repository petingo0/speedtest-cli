#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016 Di Giuseppe, Luciano
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import traceback
import sqlite3
import sys
import csv
import os

try:
	con = sqlite3.connect('results.db')

	cur = con.cursor()

	result = cur.execute('''SELECT * FROM results''')

	rows = cur.fetchall()

	dir = os.path.dirname(__file__)

	result_file=os.path.join(dir,'output.csv')

	if sys.version_info[0] < 3:
                with open(result_file, 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Date', 'Client', 'Server', 'City', 'Distance', 'Latency', 'Download', 'Upload'])
                    writer.writerows(rows)
	else:

		with open(result_file, 'w', newline='') as f:
		    writer = csv.writer(f)
		    writer.writerow(['Date', 'Client', 'Server', 'City', 'Distance', 'Latency', 'Download', 'Upload'])
		    writer.writerows(rows)

	con.close()
except:
	var = traceback.format_exc()
	print(var)
	e = sys.exc_info()[0]
	print("Error: %s" % e) 	
