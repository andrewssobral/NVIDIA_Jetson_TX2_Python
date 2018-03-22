import i2cdev
import numpy as np
from time import sleep


dac=i2cdev.I2C(0x62,1)

for x in np.arange(0,4095,10):
   v= ((np.floor((33000*x)/4095))/(10000))
   print(v)
   H = int(x / 16)
   L = int(( x - (16 * H) ) * 16)
   data_to_send = bytes([64,H,L])
   dac.write(data_to_send)
   #print([64,H,L])
   sleep(0.1)


print('finished')
