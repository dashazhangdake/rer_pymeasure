import pymeasure
import time, sys, os, csv
from pymeasure.adapters import VXI11Adapter
from pymeasure.instruments import Instrument
import numpy as np
from hp4284 import LCR4284
import pandas as pd
import matplotlib.pyplot as plt
from liveplot import liveplot


adapter = VXI11Adapter("TCPIP::10.4.139.144::gpib0,14::INSTR") # change IP and GPIB
LCR = LCR4284(adapter, "LCR4284") # define LCR4284

dir = os.getcwd()
os.chdir(dir)


def f_range(start, end=None, inc=None):
    'A range function to increase frequency, that does accept float increments...'
    L = []

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    while 1:
        next = start + len(L) * inc

        if inc > 0 and next > end:
            break
        elif inc < 0 and next < end:
            break
        L.append(next)

    return L


def pretty(val):
    if val < 1000:
        return (' %s Hz' % val)
    elif val >= 1000 and val <= 1000000:
        return ('%s kHz' % (val / 1000))
    else:
        return ('%s MHz' % (val / 1000000))


def saveData(filename, data, headers):
    f = open('%s.csv' % filename, 'a', newline='')
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writerow(data)


def Low_B(frequency1, frequency2):
    LCR.reset()
    LCR.cls()
    LCR.initial('medium', '20', '0.03','on')  # LCR includes ( integration method and bias:stat) and inital (integration points and voltage level)
    LCR.low_FB(frequency1, frequency2)  # low fb includes LIST:FREQ  and FREQ
    # LCR().low_FB('100000', '100000')
    bias_range = f_range(0.8, -0.7, -0.02)

    measurements = ['CPG']
    file_name = 'xxxx'

    data_store = {}

    for bias in bias_range:
        LCR.bias(bias)  # set up bias
        data_store['bias'] = bias
        print('Testing %s V' % bias)
        for meas in measurements:
            data = LCR.measure(meas)
            c = data[0]
            g = data[1]
            data_store['C'] = c
            data_store['G'] = g
            headers = ['bias', 'C', 'G']
            saveData(file_name, data_store, headers)
            liveplot(bias,c, g).collect()
            sys.stdout.flush()
    liveplot(bias,c, g).stop()
    path = os.path.join(dir, file_name +'.csv')
    df = pd.read_csv(path)
    headers = ['Bias', 'Capacitance', 'Transconductance'] #
    df.to_csv(path, header = headers, index = False)

def sweep_freq_nobias():
    LCR.reset()
    LCR.cls()
    LCR.initial('medium', '5','0.01', 'off')
    bias_range = np.linspace(0, 0, 1).tolist()
    freq_range = f_range(1000,1000000,1000)

    measurements = ['CPG']

    device_name = 'xx' # input your device name

    data_store = {}


    for bias in bias_range:
        file_name = 'C_G_V_' + str(device_name) + '_' + str(bias) + 'V.csv'
        LCR.bias(bias)
        print('Testing %s V' % bias)

        for freq in freq_range:
            LCR.frequency(freq)
            data_store['Frequency'] = freq
            for meas in measurements:
                data = LCR.measure(meas)
                c = data[0]
                g = data[1]
            data_store['C'] = c
            data_store['G'] = g
            headers = ['Frequency', 'C', 'G']
            saveData(file_name, data_store, headers)
            liveplot(bias, c, g).collect()
            sys.stdout.flush()

        liveplot(bias,c, g).stop()
        path = os.path.join(dir, file_name + '.csv')
        df = pd.read_csv(path)
        headers = ['Frequency/Hz', 'Capacitance', 'Transconductance']  #
        df.to_csv(path, header=headers, index=False)


def main():
    Low_B('20Hz', '100Hz')


if __name__ =='__main__':
    main()