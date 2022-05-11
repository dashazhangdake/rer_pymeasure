"""
Cryocon34 temperature controller
__author__ = "HaoQiu, XunLi"
__copyright__ = "Copyright (C) 2004 Author Name"
__license__ = "Public Domain"
__version__ = "1.0"
"""


import pymeasure
import time, sys
from pymeasure.adapters import VXI11Adapter
from pymeasure.instruments import Instrument

class cryocon34(Instrument):
    def reset(self): # Be cautious, you cannot access the instrument within 15s after reset
        self.write("*RST")

    def control_en(self): # Enable heating
        self.write('HEAT:RANGE HI')
        self.write('CONTROL')

    def get_tempK(self):
        self.write('INP A:TEMP?')
        tempK=self.read()
        return float(tempK)
    
    def get_heater(self):
        self.write('SYSTEM:HTRHST?')
        tempK=self.read()
        return str(tempK)

    def set_tempK(self, tempK):
        cmd="HEAT:SETP %s K" % str(tempK)
        self.write(cmd)

    def wait_tempK(self, tempK):
        tempK=float(tempK)
        now=self.get_tempK()
        while abs(now-tempK)>0.3:
            time.sleep(2)
            now=self.get_tempK()
            print ("setpoint: %s   current: %s    difference: %s" % (tempK,now,abs(now-tempK)))
    
    def watch_tempK(self):
        start=time.time()
        while True:
            time.sleep(1)
            now=self.get_tempK()
            print ("current: %s %s" % (time.time()-start,now))
            sys.stdout.flush()


adapter = VXI11Adapter("TCPIP::10.8.129.155::gpib0,12::INSTR")
tempcon=cryocon34(adapter, "cryocon34")
# tempcon.write("*RST")
# time.sleep(20)
print ("Current Temperature",)
print (tempcon.get_tempK())

tempcon.control_en()
# get channal A temperature
print ("setting temperature")
tempcon.set_tempK(320)
print ("watiing")
tempcon.wait_tempK(320)