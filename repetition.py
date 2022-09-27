################################################################################
# repetition.py: Repetition of Python library RPi.GPIO implementation.
################################################################################
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Global data members:
leds_enabled = False # Indicates led state.

def button_pressed(pin):
   """
   button_pressed: Callback-routine, which gets called at pressdown of the push
                   button connected to pin 27. The led state is toggled by
                   toggling the variable leds_enabled.
   """
   global leds_enabled 
   leds_enabled = not leds_enabled
   return

def leds_init(self):
   """
   leds_init: Configuring leds to outputs.

              - self: Reference to a list containing pin numbers for the leds.
   """
   for i in self:
      GPIO.setup(i, GPIO.OUT)
   return

def leds_blink(self, blink_speed_ms):
   """
   leds_blink: Blinking leds with specified delay time in milliseconds.

               - self          : Reference to a list containing pin numbers for the leds.
               - blink_speed_ms: Blink speed measured in milliseconds.
   """
   import time
   for i in self: 
      GPIO.output(i, 1) 
      time.sleep(blink_speed_ms / 1000.0) 
      GPIO.output(i, 0) 
   return

def leds_off(self):
   """
   leds_off: Disabling leds.
             
             - self: Reference to a list containing pin numbers for the leds.
   """
   for i in self:
      GPIO.output(i, 0)
   return

def main():
   """
   main: Storing pin numbers 17, 22 and 23 for three leds in a list. 
         The leds are set to output by calling the function leds_init.

         A push button is connected to pin 27. This pin is set to input
         and an event is enabled at rising edge. When an event is occuring
         the callback routine button_pressed is called to toggle the state
         of the leds between blinking every 100 milliseconds and being disabled.
   """
   global leds_enabled

   leds = [ 17, 22, 23 ] 
   leds_init(leds) 
   GPIO.setup(27, GPIO.IN) 
   GPIO.add_event_detect(27, GPIO.RISING, button_pressed, 100)

   while True: 
      if leds_enabled:
         leds_blink(leds, 100)
      else:
         leds_off(leds)
   return

################################################################################
# If this is the statup file, the main function is called to start the program.
################################################################################
if __name__ == "__main__":
   main()