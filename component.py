#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
from queue import Queue
from threading import Thread
from enum import Enum
from message import Message
from message import MessageType
import string

def generate_signature():
    random.seed()
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

class ComponentType(Enum):
    IOMANAGER = 0
    CRONOS = 1
    ENCODER = 2
    LOGGER = 3

class Component(Thread):
    """
    Base class for any component, not for instantiation.
    """
    def __init__(self,comptype,heartrate=5):
        Thread.__init__(self)
        self.inbox  = Queue()
        self.outbox = Queue()
        self.heartrate = heartrate  # heartbeat rate in seconds
        self.last_heartbeat = 0
        self.signature = generate_signature()
        self.comptype = comptype

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

    def send_heartbeat(self):
        now = int(time.time())
        if( (now - self.last_heartbeat) > self.heartrate ):
            self.send_up(Message(self.signature,MessageType.HEARTBEAT,''))
            self.last_heartbeat = now

    def get_signature(self):
        return self.signature

    def get_heartrate(self):
        return self.heartrate


