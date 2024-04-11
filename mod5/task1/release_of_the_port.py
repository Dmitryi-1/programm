import signal
from flask import Flask
import subprocess
import os


app = Flask(__name__)


def check_port(port: int) -> list[int]:
    command = ['lsof', '-i', f':{port}']
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    pids = []
    for proces in result.stdout.split('\n')[1:]:
        if 'LISTEN' in proces:
            pids.append(int(proces.split()[1]))
    return pids


def kill_processes(pids: list[int]):
    for pid in pids:
        try:
            os.kill(pid, signal.SIGKILL)
        except PermissionError:
            print(f"No permission to kill PID {pid}")
        except ProcessLookupError:
            print(f"Process PID {pid} not found")


@app.route('/')
def simpl():
    return 'All done'


if __name__ == '__main__':
    processes = check_port(5000)
    if processes:
        print(f"Port 5000 is already in use by processes: {processes}. Trying to release the port...")
        kill_processes(processes)

    app.run(port=5000, debug=False)
