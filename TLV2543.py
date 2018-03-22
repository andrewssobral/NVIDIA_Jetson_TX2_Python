import spidev
import timeit
import time
import math
import statistics


spi_30 = spidev.SpiDev()
spi_30.open(3, 0)  # open spi port 3, device (CS) 0
spi_30.max_speed_hz = 1
# CPOL = 0  , clock is zer in idle mode
# CPHA =0 , data read in first edge
#spi mode = 0b00  ,  [CPOL|CPHA]
spi_30.mode = 0


to_send = [0x0C,0x0C]

m12=[]

start_time = timeit.default_timer()
for x in range(1, 20):
   r=spi_30.xfer2(to_send)
   L=r[1]
   H=r[0]
   d12=(H*16)+math.ceil(L/16)
   m12.append(d12)  
   print(str(x)+ "\t" + str(d12))
   time.sleep(0.1)
   
   
elapsed = timeit.default_timer() - start_time
print(elapsed)

print("min" + "\t" + str(min(m12)))
print("max" + "\t" + str(max(m12)))
print("diff" + "\t" + str(max(m12)-min(m12)))
print("median" + "\t" + str(statistics.median(m12)))
print("mean" + "\t" + str(statistics.mean(m12)))
print("std" + "\t" + str(statistics.stdev(m12)))


f12=open('f12.txt','w')
for ele in m12:
    f12.write(str(ele)+'\n')
f12.close()
