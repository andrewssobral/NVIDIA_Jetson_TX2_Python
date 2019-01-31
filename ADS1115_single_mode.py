# ADS1115 single-shot mode

import i2cdev
from time import sleep

ADS1115 = i2cdev.I2C(0x48,0) # Address = 0x48, I2C bus = 0


def ADS1115_read():
  sleep(0.001)
  ADS1115.write(bytes([int(1),int(197),int(131)])) # write config =1 & chanel 0 + FSE 2v + single shot & 128hz + b00011
  sleep(0.008) # wait for conversion
  ADS1115.write(bytes([int(0)])) # change the pointer to measurment buffer
  sleep(0.001)
  c0 = int.from_bytes(ADS1115.read(2), byteorder='big')
  
  sleep(0.001)
  ADS1115.write(bytes([int(1),int(213),int(131)])) # write config =1 & chanel 1 + FSE 2v + single shot & 128hz + b00011
  sleep(0.008) # wait for conversion
  ADS1115.write(bytes([int(0)])) # change the pointer to measurment buffer
  sleep(0.001)
  c1 = int.from_bytes(ADS1115.read(2), byteorder='big')
  
  sleep(0.001)
  ADS1115.write(bytes([int(1),int(229),int(131)])) # write config =1 & chanel 2 + FSE 2v + single shot & 128hz + b00011
  sleep(0.008) # wait for conversion
  ADS1115.write(bytes([int(0)])) # change the pointer to measurment buffer
  sleep(0.001)
  c2 = int.from_bytes(ADS1115.read(2), byteorder='big')
  
  sleep(0.001)
  ADS1115.write(bytes([int(1),int(245),int(131)])) # write config =1 & chanel 3 + FSE 2v + single shot & 128hz + b00011
  sleep(0.008) # wait for conversion
  ADS1115.write(bytes([int(0)])) # change the pointer to measurment buffer
  sleep(0.001)
  a1c3 = int.from_bytes(ADS1115.read(2), byteorder='big')
  
  out = [c0,c1,c2,c3]
  return out


for x in range(1,1000):
   print(ADS1115_read())

print('Finished')
