#!/usr/bin/env python
import os
import json

data = [ { 'smtp_server':'smtp.fai.xxx', 'smtp_port':'25', 'root_alias':("admin", "backuppc") } ]
print 'DATA:', repr(data)

data_string = json.dumps(data, indent=2)
print 'JSON:', data_string
