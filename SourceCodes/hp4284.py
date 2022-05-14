import pymeasure
from pymeasure.adapters import VXI11Adapter
from pymeasure.instruments import Instrument
import sys
import numpy as np


class LCR4284(Instrument):
    def reset(self):
        self.write("*rst")
        pass

    def cls(self):
        self.write('*cls')
        pass

    def initial(self, integration, integration_num,volt_level, bias):
        self.write('aper' + integration + integration_num)
        self.write("form ascii")
        self.write("corr:open:stat on")
        self.write("corr:shor:stat on")
        self.write("corr:load:stat off")
        self.write('volt:level' + volt_level)
        self.write("init:cont on")
        self.write("bias:stat" + bias)

    def measure_mode(self, mode):
        self.write('func:imp %s' % mode)

    def volt(self, volt):
        self.write("bias:volt %s" % volt)

    def low_FB(self,frequency_1, frequency_2):

        self.write("LIST:FREQ %s" % frequency_1)
        self.write('FREQ %s' % frequency_2)

    def delay(self, time):
        self.write('TRIG:DEL %s' % time)

    def bias(self, voltage):
        self.write("bias:volt %s" % voltage)

    def frequency(self, freq):
        self.write("freq %s" % freq)

    def measure(self, meas):
        self.write('MEM:FILL DBUF')
        self.write('func:imp %s' % meas)
        self.write("trig:imm")
        data = self.values('FETC?')
        self.write('MEM:CLE DBUF')

        return data

    def off(self):
        self.write('bias:stat off')









