#!/usr/bin/env python

from enum import Enum

class MessageType(Enum):
	COMMAND = 0
	USER_INPUT = 1
	USER_OUTPUT = 2
	HEARTBEAT = 3
	LOG_ENTRY = 4

class Message():
	def __init__(self,signature,mtype,content):
		self.signature = signature
		self.mtype = mtype
		self.content = content

	def get_type(self):
		return self.mtype

	def get_signature(self):
		return self.signature

	def get_content(self):
		return self.content

	def dump(self):
		result = str(self.mtype) + " "
		result += self.signature
		result += " "
		result += self.content
		return result