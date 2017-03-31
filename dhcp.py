import subprocess  # Runs a command on the cmd line

res = subprocess.check_output("ipconfig /all")
print(res)