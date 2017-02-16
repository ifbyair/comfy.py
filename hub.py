#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import Queue
import threading

print("Hello World!")

class Hub():
    """
    Central hub for all Comfy's functions.
    Tasks:
    1. Control all the components
    2. Monitor component's health
    3. TBD
    """

    components = []

    def __init__(self,queue):
        self.queue = queue

    def add_component(c):
        components.append(c)

    def main_loop(self):
        pass

if __name__ == "__main__":
    main_queue = Queue.Queue()
    shell = Hub(main_queue)

    shell.add_component(IoMngr())

    shell.start()
    shell.main_loop()
