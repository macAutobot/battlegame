#!/usr/bin/python
import tornado.ioloop
import tornado.web
import tornado.websocket
import uuid
import json
import vars

id = {}
clients = {}
i = 0
class WebSocketHandler(tornado.websocket.WebSocketHandler):
	
	def check_origin(self, origin):
		return True
	
	def open(self):
		global clients
		global id
		global i
		print "new client connected."
		self.id = str(uuid.uuid4())
		id[i] = self.id
		i+=1
		clients[self.id] = self
		print(self.id)
		self.write_message(vars.SERVER_ACK)
		
	def on_message(self, message):
		data = json.loads(message)
		user = data[vars.CLIENT_SEND][vars.FROM_USER]
		if "max" in user:
			for j in range(len(id)):
				if clients[id[j]].id == self.id: # look if name has been assigned an id
					#if so print bot ID's and print name and send ack
					print clients[id[j]].id
					print self.id
					print "Server ack", data[vars.CLIENT_SEND][vars.FROM_USER]
					clients[id[j]].write_message(vars.SERVER_ACK)
		elif"jose" in user:
			for j in range(len(id)):
				if clients[id[j]].id == self.id: # look if name has been assigned an id
					#if so print bot ID's and print name and send ack
					print clients[id[j]].id
					print self.id
					print "Server ack", data[vars.CLIENT_SEND][vars.FROM_USER]
					clients[id[j]].write_message(vars.SERVER_ACK)
		#	self.close() #closes connection to websockets
		else:
			self.write_message(vars.SERVER_ERR)
		
		
	def on_close(self):
		print "Closing client connection."
		


application = tornado.web.Application([
    (r"/websocket", WebSocketHandler),
])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
