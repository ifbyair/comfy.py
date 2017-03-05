#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from queue import Queue
from threading import Thread
from component import Component
import select

timeout = 0.1 # seconds
# last_work_time = time.time()

class IOMngr(Component):
    """
    Component responsible for interaction with user.
    """

    def __init__(self):
        Component.__init__(self)
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
    						self.send_up(uinput)
    				self.print_prompt()
    			else:
    				if( self.check_inbox()):
    					self.proc_msg(self.inbox.get())
    					self.print_prompt()
    		except KeyboardInterrupt:
    			print("Type \"exit\" if you would like to finish")
    			self.print_prompt()

    def proc_msg(self,msg):
    	print(msg)

    def print_prompt(self):
    	print(self.prompt,end="",flush=True)
