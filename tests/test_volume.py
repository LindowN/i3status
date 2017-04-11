from pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import math

def giveMeVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    getTheFuckinVolum = volume.GetMasterVolumeLevelScalar()
    getTheFuckinVolum = getTheFuckinVolum * 100
    return math.floor(getTheFuckinVolum)

def test_volume():
    print(giveMeVolume())