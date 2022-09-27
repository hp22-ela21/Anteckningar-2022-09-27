# Imports:
import paho.mqtt.client as mqtt # Imports MQTT library.

def client_on_connect(client, data, flags, return_code):
   """
   client_on_connect: Callback routine which gets called when trying to connect to
                      a host/broker such as broker.hivemq.com. If the return code is 0,
                      the connection was succesful, otherwise, connection failed.
   """
   if return_code != 0:
      print("Could not connect to host \"" + str(client._host) + "\"!\n")
   else:
      print("Succesfully connected to host \"" + str(client._host) + "\"!\n")
   return

def client_on_disconnect(client, data, return_code):
   """
   client_on_disconnect: Callback routine which gets called when disconnecting
                         from a host/broker. If the return code is 0, the connection
                         was deliberate, others the connection was unexpected.
   """ 
   if return_code != 0:
      print("Unexpected disconnection from host \"" + str(client._host) + "\"!\n")
   else:
      print("Successfully disconnected from host \"" + str(client._host) + "\"!\n")
   return

def client_on_message(client, data, message):
   """
   client_on_message: Callback routine which gets called when a subscriber receives
                      a message from the subscribed topic. This message (payload) is 
                      received as a binary file and has to be decoded to UTF-8. The
                      message (payload) is printed along with the topic (address) it
                      was received from.
   """
   s = message.payload.decode("utf-8") # Converts message from binary to string.
   print("Recevied message \"" + str(s) + "\" from topic \"" + str(message.topic) + "\"!\n")
   return

def main():
   """
   main: Creating a MQTT server, which gets connected to host "broker.hive.com".
         The server subscribes to topic "python/mqtt/1". When a message is 
         received, it gets printed in the terminal by the callback routine
         client_on_message.
   """
   # Creating a MQTT server:
   server1 = mqtt.Client() 

   # Connects function pointers to the callback routines:
   server1.on_connect = client_on_connect
   server1.on_disconnect = client_on_disconnect
   server1.on_message = client_on_message

   # Connects to host "broker.hivemq.com":
   server1.connect("broker.hivemq.com")
   if not server1.is_connected():
      server1.reconnect()

   # Subscribes to topic "python/mqtt/1":
   server1.subscribe("python/mqtt/1", 1)

   # Starting MQTT thread:
   server1.loop_start()

   # Keeps program running continuously:
   while True: 
      pass
   return

################################################################################
# If this is the startup file, the main function is called to start the program.
################################################################################
if __name__ == "__main__":
   main()