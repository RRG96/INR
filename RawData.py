import scipy.io
import mne
import time
import AdquisicionPruebas as ap
raw=mne.io.read_raw_fif('Datos EEG/FriMay311920522019.fif')
raw.plot(n_channels=7, scalings=None ,duration=5, show=True,block=True)