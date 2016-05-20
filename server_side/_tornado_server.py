#!/usr/bin/python
import tornado.ioloop
import tornado.web
import tornado.websocket
import uuid
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
		self.write_message("Server has accepted your connection")
		
	def on_message(self, message):
		if "max" in message:
			self.write_message(message)
			for j in range(len(id)):
				print "for loop"
#				clients[id[j]].write_message("Noe of the Above")
			self.write_message("Server has accepted your connection")
			print "the client send: ", message
		else:
			print "Hello Jose"
		#	self.close() #closes connection to websockets
		
		
	def on_close(self):
		print "Closing client connection."
		


application = tornado.web.Application([
    (r"/websocket", WebSocketHandler),
])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
