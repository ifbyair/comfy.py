#!/usr/bin/env python

from component import Component
from component import ComponentType
from message import Message
from message import MessageType

class Cronos(Component):
	def __init__(self):
        Component.__init__(self,ComponentType.CRONOS)

    def run(self):
    	while(True):
    		pass