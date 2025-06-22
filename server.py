from flask import Flask, request
import subprocess, os, signal

app = Flask(__name__)
current_process = None

@app.route('/run')
def run():
    global current_process
    file = request.args.get('file')
    if not file:
        return 'No file specified', 400

    if current_process:
        try:
            os.killpg(os.getpgid(current_process.pid), signal.SIGTERM)
        except:
            pass

    current_process = subprocess.Popen(
        ['python', file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid
    )
    return f'Running {file}', 200

@app.route('/terminate', methods=['POST'])
def terminate():
    global current_process
    if current_process:
        try:
            os.killpg(os.getpgid(current_process.pid), signal.SIGTERM)
        except:
            pass
        current_process = None
        return 'Terminated', 200
    return 'No process running', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
