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
   main: Creating a MQTT client object and setting up function pointers to callback
         routines. Then the client is connected to host "broker.hivemq.com"
   """
   import time

   # Creating a MQTT client:
   client1 = mqtt.Client() 

   # Sets up function pointers to callback routines:
   client1.on_connect = client_on_connect
   client1.on_disconnect = client_on_disconnect
   client1.on_message = client_on_message

   # Connecting to host "broker.hivemq.com":
   client1.connect("broker.hivemq.com")
   # If the client is not connected, a reconnection is done:
   if not client1.is_connected():
      client1.reconnect()
   
   # Starting MQTT thread:
   client1.loop_start()

   # Waiting one second for connection to start:
   time.sleep(1)

   while True:
      # Reads messages from the terminal:
      s = input("Enter a message to publish or a blank line to finish:\n")
      print()

      # If a message was entered it gets published to topic "python/mqtt/1":
      if s:
         msg = client1.publish(topic = "python/mqtt/1", payload = s, qos = 1)
         msg.wait_for_publish()
      # Else the MQTT thread is stopped and the client disconnects from the host:
      else: 
         client1.loop_stop()
         client1.disconnect()
         break
   # Prints a farewell before the program terminates:
   print("Bye!\n")
   return 

################################################################################
# If this is the startup file, the main function is called to start the program.
################################################################################
if __name__ == "__main__":
   main()