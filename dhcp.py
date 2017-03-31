import re

from subprocess import Popen, PIPE, check_output

def get_processes_running():
    """
    Takes tasklist output and parses the table into a dict
    """
    tasks = check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
    p = []
    for task in tasks:
        m = re.match(b'(.*?)\\s+(\\d+)\\s+(\\w+)\\s+(\\w+)\\s+(.*?)\\s.*', task.encode())
        if m is not None:
            p.append({"image":m.group(1).decode(),
                        "pid":int(m.group(2).decode()),
                        "session_name":m.group(3).decode(),
                        "session_num":int(m.group(4).decode()),
                        "mem_usage":int(m.group(5).decode('ascii', 'ignore'))
                        })
    return( p)

def test():
    print(*[line.decode('cp866', 'ignore') for line in Popen('tasklist', stdout=PIPE).stdout.readlines()])

    lstp = get_processes_running()
    for p in lstp:
        print(p)
    return

if __name__ == '__main__':
    test()
