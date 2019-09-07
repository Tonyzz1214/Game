#coding=utf-8
import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt

filename="E:\\software\\CDF\\data.csv"
lines = []
test = "-51.67"
test2=float(test)


with open(filename,'r') as f:
    lines = f.read().split('\n')
print (lines)
dataSets1=[]
dataSets2=[]
dataSets3=[]
for line in lines:
    tmp1=line.split(',')[0]
    tmp1=tmp1.replace(tmp1[0],"-")
    tmp2 = line.split(',')[1]
    tmp2 = tmp2.replace(tmp2[0], "-")
    tmp3 = line.split(',')[2]
    tmp3 = tmp3.replace(tmp3[0], "-")
    dataSets1.append(float(tmp1))
    dataSets2.append(float(tmp2))
    dataSets3.append(float(tmp3))
print (dataSets1)
sample = dataSets1
ecdf = sm.distributions.ECDF(sample)
x = np.linspace(-70, max(sample))
y = ecdf(x)
plt.plot(x, y, linewidth = '1',label="0dB")

sample = dataSets2
ecdf = sm.distributions.ECDF(sample)
x = np.linspace(-70, max(sample))
y = ecdf(x)
plt.plot(x, y, linewidth = '1',label="-2dB")

sample = dataSets3
ecdf = sm.distributions.ECDF(sample)
x = np.linspace(-70, max(sample))
y = ecdf(x)
plt.plot(x, y, linewidth = '1',label="-4dB")

plt.xlabel('RSRP')
plt.ylabel('CDF')
plt.title('800K RSRP')

plt.legend(loc='upper left')
plt.show()