#!/usr/bin/env python
# -*- coding:Utf-8 -*-


import api
from SimpleXMLRPCServer import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 8080))



server.register_function(api.format)
server.register_function(api.shutdown)



server.serve_forever()




# vim: ts=4:sw=4:ai
