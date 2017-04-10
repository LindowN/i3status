import wmi
c = wmi.WMI ()

def show_service():
  for process in c.Win32_Service ():
        if process.Name == "wampapache64":
              if process.State == 'Stopped' :
                  print("WAMP server offline")
              else :
                  print("WAMP server online")
        if process.Name == "Dhcp" :
              if process.State == 'Stopped' :
                  print("DHCP Client offline")
              else :
                  print("DCHP Client online")


show_service()
#      print(process.ProcessId, process.Name)
