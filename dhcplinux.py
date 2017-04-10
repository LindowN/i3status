import subprocess
p = subprocess.Popen(["ps", "-a"], stdout=subprocess.PIPE)
out, err = p.communicate()
if ('Httpd' in out):
    print('Httpd running')
if ('mysql' in out):
    print('mysql running')