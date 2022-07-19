import subprocess

from click import command

cmd = ["python3 -m pip install pycurl;python3 -m pip install pyserial;python3 -m pip install mysql-connector-python"]

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    line=proc_stdout.decode().split('\n')
    print(line)

counter = 0
for count, command in enumerate(cmd):
    counter= counter+1
    subprocess_cmd(cmd)