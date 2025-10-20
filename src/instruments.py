##########################################################################################
# Importing relevant libraries
##########################################################################################

import vxi11
import matplotlib
import numpy as np
import time
import pylab
import matplotlib.pyplot as plt
from si_prefix import si_format

##########################################################################################
# Establishing and testing communication with networked instruments
##########################################################################################

# Creating instrument object g for signal generator connected at IP address 172.17.51.102
g = vxi11.Instrument('172.17.51.102')
print(g.ask('*idn?'))

# Creating instrument object o for oscilloscope connected at IP address 172.17.51.103
o = vxi11.Instrument('172.17.51.103')
print(o.ask('*idn?'))

##########################################################################################
# Remote reading of signal generator parametars
##########################################################################################
def rrsg():
    print('For this signal parametars are:')
    print ('Vpp=',float(g.ask(":sour1:volt:ampl?")),'V')
    print ('Vamp=',float(g.ask(":sour1:volt:ampl?"))/2,'V')
    print ('Voffset=',float(g.ask(":sour1:volt:offs?")),'V')
    print ('f=',float(g.ask(":sour1:freq?")), 'Hz')
    print ('\n')

time.sleep(10)
##########################################################################################
# A function for automated measurments of waveforms from oscilloscope
##########################################################################################

def mo(channel):
      time.sleep(1)
      o.write('waveform:source channel' + str(channel))
      o.write('waveform:format ascii')
      raw_data = o.ask('waveform:data?').split(',')
      V = [float(i) for i in raw_data[:1400]]
      offset = float(o.ask(':channel' + str(channel) + ':offset?'))
      scale = float(o.ask(':channel' + str(channel) + ':scale?'))
      Vdisplay = [(i + offset) / scale for i in V[:1400]]
      return Vdisplay

##########################################################################################
# A function for automated plotting and saving graphs of waveforms from oscilloscope
##########################################################################################
def psgraph():
    plt.close()
    plt.figure(figsize=(7,4))
    plt.xlim(-7,7)
    plt.ylim(-4,4)
    plt.xticks(range(-7,8), 15 * '')
    plt.yticks(range(-4,5), 9 * '')
    plt.legend(['line_up', 'line_down'])
    h = np.linspace(-7,7,1400)
    plt.plot(h, mo(1), 'y', label = 'CH1')
    plt.plot(h, mo(2), 'c', label = 'CH2')
    plt.xlabel('TD ' + str(si_format(float(o.ask('timebase:scale?'))))+'s/div')
    plt.ylabel('CH1 ' + str(si_format(float(o.ask('channel1:scale?'))))+' V/div' +', CH2 '+ str(si_format(float(o.ask('channel2:scale?'))))+' V/div')
    plt.legend()
    plt.grid()
    print ('f=',float(g.ask(":sour1:freq?")), 'Hz')
    timestr = time.strftime("%Y%m%d-%H%M%S")
    plt.savefig('D:\Vezzbe\ANE\Vezba 01\waveform-oscilloscope-' + timestr + '.pdf', bbox_inches = 'tight')
    plt.show()
    


##########################################################################################
# Remote configuration of signal generator parametars
##########################################################################################

##########################################################################################
# sin
##########################################################################################

g.write(":outp1 off")
time.sleep(1)
g.write(":sour1:func sin")
g.write(":sour1:volt:high 3")
g.write(":sour1:volt:low -1")
g.write(":sour1:freq 1e3")
time.sleep(1)
g.write(":outp1 on")

print('For this signal parametars are:')
print ('Vpp=',float(g.ask(":sour1:volt:ampl?")),'V')
print ('Vamp=',float(g.ask(":sour1:volt:ampl?"))/2,'V')
print ('Voffset=',float(g.ask(":sour1:volt:offs?")),'V')
print ('f=',float(g.ask(":sour1:freq?")), 'Hz')

psgraph()
time.sleep(3)
