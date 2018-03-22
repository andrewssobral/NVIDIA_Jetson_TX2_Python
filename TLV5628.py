import sys, os, time
import spidev
import math

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


spi_31 = spidev.SpiDev()
spi_31.open(3, 1)  # open spi port 3, device (CS) 0
spi_31.max_speed_hz = 1
# CPOL = 0  , clock is zer in idle mode
# CPHA =1 , data read in second edge
#spi mode = 0b00  ,  [CPOL|CPHA]
spi_31.mode = 1


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
   gpio_write(1)
   print("GPIO 388 is ready")
except:
   print("Error in GPIO 388 value!")
   sys.exit(os.EX_OK)


for x in range(1, 256):
   v_hat=(x/256)*255
   volt=math.ceil(v_hat)
   to_send = [0x02,volt]
   r=spi_31.xfer2(to_send)
   gpio_write(0)
   gpio_write(1)
   print("update")
   time.sleep(0.01) 

try:
   gpio_close()
except:
   print("port is not closed!")
   sys.exit(os.EX_OK)
