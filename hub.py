#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from iomngr import IOMngr
from message import Message
from message import MessageType
from component import ComponentType
import component
from logger import Logger

# IOComponent = 0

class Hub():
    """
    Central hub for all Comfy's functions.
    Tasks:
    1. Control all the components
    2. Monitor component's health
    3. TBD
    """

    def __init__(self):
        self.components = {}
        self.signature = component.generate_signature()
        self.iopipe = ''
        self.logger = ''
        self.alarms = []

    def add_iopipe(self,p):
        self.iopipe = p.get_signature()
        self.components[self.iopipe] = p

    def add_logger(self,l):
        self.logger = l.get_signature()
        self.components[self.logger] = l

    def start(self):
        for c in self.components:
            self.components[c].setDaemon(True)
            self.components[c].start()

    def main_loop(self):
        while (True):
            for c in self.components:
                if( self.components[c].check_outbox()):
                    self.proc_msg(self.components[c].get_message())

    def proc_msg(self,msg):
        mtype = msg.get_type()
        if( mtype == MessageType.HEARTBEAT ):
            self.log('heartbeat from ' + msg.get_signature()) # hearbeat received
        elif( mtype == MessageType.USER_INPUT ):
            self.log('processing input: ' + msg.get_content()) # process user input
        elif( mtype == MessageType.USER_OUTPUT ):
            self.log('processing output: ' + msg.get_content())
        elif( mtype == MessageType.COMMAND ):
            self.log('processing command') # process command
        else:
            self.log('bad message type') # shit happens - unknown message type

    def log(self,log_entry):
        m = Message(self.signature,MessageType.LOG_ENTRY,log_entry)
        self.components[self.logger].send_down(m)

if __name__ == "__main__":
    shell = Hub()

    shell.add_iopipe(IOMngr())
    shell.add_logger(Logger())

    shell.start()
    shell.main_loop()
