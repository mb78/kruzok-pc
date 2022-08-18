import logging
from websocket_server import WebsocketServer

def client_name(c): return c['address'][0]+":"+str(c['address'][1])
def log_msg(s):
  print("Message >>>%s<<<"%s)
  return s

def new_client(client, server):

  server.send_message_to_all(log_msg("new client "+client_name(client)))
def new_msg(client,server,msg):
  server.send_message_to_all(log_msg(client_name(client)+" says:"+msg))

server = WebsocketServer(host='127.0.0.1', port=8100, loglevel=logging.INFO)
server.set_fn_new_client(new_client)
server.set_fn_message_received(new_msg)
server.run_forever()
