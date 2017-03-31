from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw import AudioUtilities, IAudioEndpointVolume
import math
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
getTheFuckinVolum = volume.GetMasterVolumeLevelScalar()
getTheFuckinVolum = getTheFuckinVolum * 100
print(math.floor(getTheFuckinVolum))
#volume.SetMasterVolumeLevel(-20.0, None)
