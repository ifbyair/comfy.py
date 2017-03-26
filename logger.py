#!/usr/bin/env python

from component import Component
from component import ComponentType
from message import Message
from message import MessageType

class Logger(Component):
	def __init__(self,logfile='comfy.log'):
		Component.__init__(self,ComponentType.LOGGER)
		self.logfile = logfile

	def run(self):
		while(True):
			self.send_heartbeat()
			if( self.check_inbox()):
				self.proc_msg(self.inbox.get())

	def proc_msg(self,msg):
		if( msg.get_type() != MessageType.LOG_ENTRY ):
			log_entry("Wrong message type sent to logger: " + msg.dump())
			return
		self.log_entry(msg.dump())

	def log_entry(self,l):
		with open(self.logfile,'a') as f:
			f.write(l)
			f.write('\n')
