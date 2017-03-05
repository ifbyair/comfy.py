#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from iomngr import IOMngr

IOComponent = 0

class Hub():
    """
    Central hub for all Comfy's functions.
    Tasks:
    1. Control all the components
    2. Monitor component's health
    3. TBD
    """

    def __init__(self):
        self.components = []

    def add_component(self,purpose,c):
        purpose = len(self.components)
        self.components.append(c)

    def start(self):
        for c in self.components:
            c.setDaemon(True)
            c.start()

    def main_loop(self):
        while (True):
            for c in self.components:
                if( c.check_outbox()):
                    self.proc_msg(c.get_message())

    def proc_msg(self,msg):
        if( msg == "exit"):
            sys.exit(0)
        elif( msg == "heartbeat"):
            self.components[IOComponent].send_down("heartbeat received")
        else:
            self.components[IOComponent].send_down("not sure what you want me to do")

    def setIOcomponent(self,io_index):
        self.io_index = io_index


if __name__ == "__main__":
    shell = Hub()

    shell.add_component(IOComponent,IOMngr())

    shell.start()
    shell.main_loop()
