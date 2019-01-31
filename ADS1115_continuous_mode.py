# ADS1115 continuous mode

import i2cdev
from time import sleep


ADS1115 = i2cdev.I2C(0x48,0)  # Address = 0x48, I2C bus = 0
sleep(0.1)
ADS1115.write(bytes([int(1),int(244),int(131)])) # write config =1 & chanel 3 + FSE 2v + continoues & 128hz + b00011
sleep(0.1)
ADS1115.write(bytes([int(0)])) # change the pointer to measurment buffer
sleep(0.1)

for x in range(1,100):
   raw_bytes=ADS1115.read(2)
   value = int.from_bytes(raw_bytes, byteorder='big')
   per_value=value/32767
   print(value,per_value)
   sleep(1)

print('finished')
