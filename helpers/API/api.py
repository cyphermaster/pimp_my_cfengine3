# -*- coding:Utf-8 -*-


def format(*args):
	print "format() called with " + " ".join(map(str,args))
	return "Format OK."



def shutdown():
	print "shutdown() called"
	return True



# vim: ts=4:sw=4:ai
