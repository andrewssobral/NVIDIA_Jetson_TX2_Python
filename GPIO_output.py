import sys, os, time


# function definition

def gpio_open():
   f_export = open("/sys/class/gpio/export", 'w')
   f_export.write('388')
   f_export.close()
   print("GPIO 388 is opened")

def gpio_close():
   f_unexport = open("/sys/class/gpio/unexport", 'w')
   f_unexport.write('388')
   f_unexport.close()
   print("GPIO 388 is closed")

def gpio_set_direction():
   f_direction = open("/sys/class/gpio/gpio388/direction", 'w')
   f_direction.write('out')
   f_direction.close()
   print("GPIO 388 is output")

def gpio_write(x):
   if x==0:
      f_value = open("/sys/class/gpio/gpio388/value", 'w')
      f_value.write('0')
      f_value.close()
   else:
      f_value = open("/sys/class/gpio/gpio388/value", 'w')
      f_value.write('1')
      f_value.close()

# main

try:
   gpio_open()
except:
   print("port is busy!")
   sys.exit(os.EX_OK)
 
try:
   gpio_set_direction()
except:
   print("GPIO 388 is not output!")
   sys.exit(os.EX_OK)
  
try:
   gpio_write(0)
   print("GPIO 388 is ready")
except:
   print("Error in GPIO 388 value!")
   sys.exit(os.EX_OK)

for x in range(1, 20):
   gpio_write(1)
   print("GPIO 388 is on")
   time.sleep(0.2)
   gpio_write(0)
   print("GPIO 388 is off")
   time.sleep(0.2) 

try:
   gpio_close()
except:
   print("port is not closed!")
   sys.exit(os.EX_OK)
