#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from queue import Queue
from threading import Thread

class Component(Thread):
    """
    Base class for any component, not for instantiation.
    """

    def __init__(self):
        Thread.__init__(self)
        self.inbox  = Queue()
        self.outbox = Queue()

    def run(self):
        pass

    def send_up(self,msg):
        """ Send a message to the Hub """
        self.outbox.put(msg)

    def send_down(self,msg):
        """ Send a message to the Component """
        self.inbox.put(msg)

    def check_inbox(self):
        """ Check inbox for messages """
        return not self.inbox.empty()

    def check_outbox(self):
        return not self.outbox.empty()

    def get_message(self):
        return self.outbox.get()
