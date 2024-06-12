import sys
import socket
from flask import Flask, request
import subprocess

app = Flask(__name__)
server_started = False

def exit_app():
    sys.exit()

@app.route('/', methods=['GET', 'POST'])
def _main():
	if request.method == 'POST':
		print('POST')
		_type =request.args.get('brand')
		print(_type)
		_type =request.args.get('frag_name')
		print(_type)
		_type =request.args.get('conc')
		print(_type)
		_type =request.args.get('ml')
		print(_type)
		return 'ok'
@app.route('/shutdown', methods=['POST'])
def shutdown_server():
	print('SHUTDOWN')
	global server_started
	if not server_started:
		raise RuntimeError('Сервер не запущен')

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.connect(('localhost', 5000))
	server_socket.send(b'Shutdown')
	server_socket.close()
	print('Сервер выключен')
	return 'Сервер выключен'

if __name__ == '__main__':
    server_started = True
    app.run(debug=True, port=5000)
