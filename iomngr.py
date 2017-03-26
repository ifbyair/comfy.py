#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from queue import Queue
import select
from threading import Thread
from component import Component
from component import ComponentType
from message import Message
from message import MessageType

timeout = 0.1 # seconds

class IOMngr(Component):
    """
    Component responsible for interaction with user.
    """

    def __init__(self):
        Component.__init__(self,ComponentType.IOMANAGER)
        self.prompt = "main > "

    def run(self):
    	self.print_prompt()
    	while (True):
    		try:
    			ready = select.select([sys.stdin], [], [], timeout)[0]
    			if( ready ):
    				for f in ready:
    					uinput = f.readline().rstrip()
    					if( uinput ):
    						self.send_up(Message(self.signature,MessageType.USER_INPUT,uinput))
    				self.print_prompt()
    			else:
    				if( self.check_inbox()):
    					self.proc_msg(self.inbox.get())
    					self.print_prompt()
    				self.send_heartbeat()
    		except KeyboardInterrupt:
    			print("Type \"exit\" if you would like to finish")
    			self.print_prompt()

    def proc_msg(self,msg):
    	print(msg)

    def print_prompt(self):
    	print(self.prompt,end="",flush=True)

    def set_prompt(self,prompt):
    	self.prompt = prompt
