import bloodFunctions as b
import time
import numpy as np
import matplotlib.pyplot as plt


samples = []


initSpiAdc()
start = time.time()

while time.time()-start<60:
    samples.append(float(getAdc()))
    time.sleep(0.01)

finish = time.time()
saveMeasures(samples, len(samples), 0, start, finish)
showMeasures(samples, len(samples), 0, start, finish)
