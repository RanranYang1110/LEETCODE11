#-*- coding:utf-8 -*-
# @author: qianli
# @file: test1.py
# @time: 2019/08/27
#-*- coding:utf-8 -*-
# @author: qianli
# @file: test1.py
# @time: 2019/03/19
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.signal import stft
from scipy.fftpack import fft, hilbert
from sklearn.preprocessing import MinMaxScaler
from scipy.io import loadmat

def STFT(inputdata, fs):
    inputdata = inputdata - np.mean(inputdata)
    f, t, Zxx = stft(inputdata, fs, window='hann', nperseg=fs / 16, noverlap=fs / 32, nfft=fs / 16)
    #    f, t, Zxx = stft(inputdata, fs, window ='hann', nperseg = fs/2, noverlap = fs/4, nfft = fs/2)
    Zxx = np.abs(Zxx) * 4
    scaler = MinMaxScaler(feature_range=(0, 1))
    Zxx_scaled = scaler.fit_transform(Zxx)
    return t, f, Zxx_scaled


def get_hil(data, fs):
    '''
    获取振动信号data经hilber包络解调之后的频谱
    输入：data 振动数据
         fs 采样频率
    输出：f1 频率
         ff1 幅值
    '''
    try:
        if type(data) == 'list':
            data = np.array(data)

        N = len(data)
        data = data.reshape(N)
        data1 = data - np.mean(data)
        hh1 = hilbert(data1)
        hh2 = np.sqrt(data1 ** 2 + hh1 ** 2)
        hh3 = hh2 - np.mean(hh2)
        ff1 = np.abs(fft(hh3)) * 2 / N  # 对信号进行hilbert变换之后进行fft
        f1 = np.linspace(0, (N - 1) * fs / N, N)
        fx = f1[0: int(np.floor(N / 2))]
        fy = ff1[0: int(np.floor(N / 2))]
        return fx, fy
    finally:
        pass
def STHT(inputdata, fs, nperseg, noverlap):
    inputdata = inputdata - np.mean(inputdata)
    N = inputdata.shape[0]
    row = int(fs/2 / (fs / nperseg) + 1)
    column = int(N / noverlap + 1)

    zxx = np.zeros([row, column])
    f = np.linspace(0, fs/2, row, endpoint=True)
    t = np.linspace(0, 1, column, endpoint=True)
    for jj in range(1, column-1):
        ii = jj -1
        # data = inputdata[int(ii * noverlap) : int(ii*noverlap + nperseg)]
        if ii == column - 2:
            data = inputdata[int(ii * noverlap - noverlap): int(ii * noverlap - noverlap + nperseg)]
        else:
            data = inputdata[int(ii * noverlap): int(ii * noverlap + nperseg)]
        # if ii == column - 2:
        #     data = data.reshape(int(noverlap))
        #     data = data * np.hanning(noverlap)
        #     fx, fy = get_hil(data, fs)
        # else:
        data = data.reshape(int(nperseg))
        data = data * np.hanning(nperseg)
        fx, fy = get_hil(data, fs)

        zxx[:800,ii] = fy
    return t, f, zxx

def draw_figure(x, y, z, savename):
    plt.close('all')
    fig, ax = plt.subplots(1)
    ax.pcolormesh(x, y, z)
    ax.axis('tight')
    plt.ylim([0,500])
    #    plt.show()
    plt.style.use('ggplot')
    plt.axis('off')

    plt.xticks([])
    plt.yticks([])
    # dpi是设置清晰度的，大于300就很清晰了，但是保存下来的图片很大
    #    fig.set_size_inches(0.32/3,0.32/3) #dpi = 300, output = 700*700 pixels
    fig.set_size_inches(2.56 / 3, 2.56 / 3)  # dpi = 300, output = 700*700 pixels

    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.savefig(savename, format='jpg', transparent=True, dpi=300, pad_inches=0)

filepath1 = r"D:\7-学习资料\a-study\自我学习\专利\20190813发明--基于卷积神经网络的轴承故障方法\预处理数据"
files_dir1 = os.listdir(filepath1)
for name1 in files_dir1[:2]:
    print(name1)
    filepath3 = os.path.join(filepath1,name1)
    data = loadmat(filepath3)
    data = data['y_final']
    fs = 25600
    t, f, Zxx = STHT(data.reshape(fs).tolist(), fs,nperseg=fs/16, noverlap=fs/32)
    # savename1 = name1[:-4] + '.jpg'
    # savepath = os.path.join(r"D:\7-学习资料\a-study\自我学习\专利\20190827发明--连续包络谱变换\图像数据",name1[:8])
    # if not os.path.exists(savepath):
    #     os.mkdir(savepath)
    # savename = os.path.join(savepath, savename1)
    # draw_figure(t, f, Zxx, savename)