import libmushu
from libmushu.ampdecorator import AmpDecorator
from libmushu.driver.gtec import GUSBamp
from libmushu.driver.randomamp import RandomAmp
import matplotlib.pyplot as plt
import mne
import numpy as np
import time
from mne.time_frequency import tfr_morlet
from multiprocessing import Process
from random import randint

savedata = []
savedata1 = []
savedata2 = []
savedata3 = []
savedata4 = []
savedata5 = []
savedata6 = []
savedata7 = []
savedata8 = []
savedata9 = []
savedata10 = []
savedata11 = []
savedata12 = []
savedata13 = []

def configurar(canales, tipo_canal, frecuencia, repeticiones):
    ch_types = []
    ch_names = []
    sfreq = frecuencia
    rand = randint(3, 5)
    contador = repeticiones * (8 + rand)
    #plt.ion( )
    #fig, fig_axes = plt.subplots(nrows=canales, ncols=1, constrained_layout=True, sharex=True)
    fig_axes = 0
    global amp
    available_amps = libmushu.get_available_amps()
    print available_amps
    ampname = available_amps[0]
    amp = libmushu.get_amp(GUSBamp)
    #amp = AmpDecorator(GUSBamp)
    #amp.configure(fs=frecuencia, channels=canales)
    nombre = time.asctime()
    nombre = nombre.replace(':',' ')
    tipo_canal = tipo_canal.lower()
    for i in range(0, canales + 2):
        if i < canales:
            ch_types.append(str(tipo_canal))
        if i >= canales:
            ch_types.append('stim')
    tipo_canal = tipo_canal.upper()
    for i in range(0, canales + 2):
        if i < canales:
            ch_names.append(str(tipo_canal) + ' 00' + str(i + 1))
        if i > canales:
            ch_names.append('STI 014')
        if i == canales + 1:
            ch_names.append('MK 000')
    info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)
    return info, nombre, fig_axes, contador

def adquisicion(canales, frecuencia):
    data, trigger = amp.get_data()
    print trigger
    y = []
    marcador = []
    y.extend(data[:, 0])
    marcador.extend(data[:, 0])
    marcador[0] = 1
    marcador[len(data) - 1] = 1
    for i in range(1, len(data) - 1):
        marcador[i] = 0
    for i in range(0, len(data)):
        y[i] = randint(0, 1)
    return data, y, marcador

def preprocesamiento(data, y, info, marcador):
    data1 = np.array([data[:, 0],data[:, 1],data[:, 2],data[:, 3],data[:, 4],data[:, 5],data[:, 6],data[:, 7],data[:, 8],data[:, 9],data[:, 10],data[:, 11], y[:], marcador[:]])
    raw = mne.io.RawArray(data1, info)
    picks = mne.pick_types(raw.info, meg=False, eeg=True, eog=False, stim=False, exclude='bads')
    raw.notch_filter(np.arange(50, 128, 50), picks=picks, filter_length = 'auto', phase = 'zero')
    raw.filter(8, 32, filter_length = 'auto')
    return raw, data1, picks

def procesamiento(raw, picks, canales):
    n_cycles = 5
    freqs = np.arange(8, 34, 3) 
    events = mne.find_events(raw, stim_channel = 'STI 014')
    event_id = dict(aud_l=1) 
    tmin = 0
    tmax = 0.5 
    baseline = (None, 0)
    epochs = mne.Epochs(raw, events, event_id, tmin, tmax, proj=True, picks=picks, baseline=baseline, preload=False)
    power = tfr_morlet(epochs, freqs=freqs, n_cycles=n_cycles, return_itc=False, decim=3, n_jobs=1)
    promedio = power.data[0]
    for i in range(1, canales):
        promedio = promedio + power.data[i]
    promedio = promedio / canales
    promedio1 = promedio[0]
    for i in range(1, 8):
        promedio1 = promedio1 + promedio[i]
    promedio1 = promedio1 / 8
    promedio2 = 0
    for i in range(0, len(promedio1)):
        promedio2 = promedio2 + promedio1[i]
    promedio2 = promedio2 / len(promedio[0])
    print 'Potencia promedio: ', promedio2
    return power
    
def ploteotiemporeal(data, canales, fig_axes):
    for i in range(0, canales):
        fig_axes[i].plot(data[i, :])
    plt.pause(0.000000000000000001)
    for i in range(0, canales):
        fig_axes[i].cla( )

def ploteomorlet(power, canales):
    for i in range(0, canales):
        power.plot([power.ch_names.index('EEG 00' + str(i))])

def guardar(data, tiempo, y, nombre, info, intentos, frecuencia):
    savedata.extend(data[0, :])
    savedata1.extend(data[1, :])
    savedata2.extend(data[2, :])
    savedata3.extend(data[3, :])
    savedata4.extend(data[4, :])
    savedata5.extend(data[5, :])
    savedata6.extend(data[6, :])
    savedata7.extend(data[7, :])
    savedata8.extend(data[8, :])
    savedata9.extend(data[9, :])
    savedata10.extend(data[10, :])
    savedata11.extend(data[11, :])
    savedata12.extend(data[12, :])
    savedata13.extend(data[13, :])
    tiempo = len(savedata)/frecuencia
    if tiempo == intentos:
        amp.stop()
        savedata13[0] = 2
        savedata13[intentos * frecuencia - 1] = 2
        data1 = np.array([savedata[:], savedata1[:], savedata2[:], savedata3[:], savedata4[:], savedata5[:], savedata6[:], savedata7[:], savedata8[:], savedata9[:], savedata10[:], savedata11[:], savedata12[:], savedata13[:]])
        saveraw = mne.io.RawArray(data1, info)
        saveraw.save('C:/Users/Rodro/Desktop/Tesis/Pruebas/Datos EEG' + '/' + str(nombre) + '.fif')
    return tiempo
 
def iniciar(canales, frecuencia, info, nombre, axes, intentos):
    tiempo = 0
    amp.start()
    while tiempo <= intentos:
        data, y, marcador = adquisicion(canales, frecuencia)
        raw, data1, picks = preprocesamiento(data, y, info, marcador)
        power=procesamiento(raw, picks, canales)
        #ploteotiemporeal(data1, canales, axes)
        tiempo = guardar(data1, tiempo, y, nombre, info, intentos, frecuencia)

if __name__ == '__main__':
    canales = 12
    frecuencia = 256
    repeticiones = 1
    info, nombre, axes, intentos = configurar(canales, 'eeg', frecuencia, repeticiones)
    iniciar(canales, frecuencia, info, nombre, axes, intentos)