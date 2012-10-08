#!/usr/bin/env python
# -*- coding:Utf-8 -*-

import xmlrpclib


rpc = xmlrpclib.Server("http://localhost:8080")


print rpc.format("toto", 28)



rpc.shutdown()



# vim: ts=4:sw=4:ai
