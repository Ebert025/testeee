from flask import Flask, request, jsonify
import subprocess
import os
import uuid
import yt_dlp as yt
app = Flask(__name__)
DOWNLOAD_FOLDER = "down"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

yt._real_main(["https://www.youtube.com/watch?v=jVMgTkIFXJo"])
@app.route('/download', methods=['GET'])
def download_spotify():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Parâmetro "url" é obrigatório.'}), 400

    session_id = str(uuid.uuid4())
    session_folder = os.path.join(DOWNLOAD_FOLDER, session_id)
    os.makedirs(session_folder)

    #bagaça aq

@app.route('/file/<session_id>/<filename>')
def serve_file(session_id, filename):
    file_path = os.path.join(DOWNLOAD_FOLDER, session_id, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'Arquivo não encontrado'}), 404
    return app.send_static_file(file_path)

@app.route('/')
def index():
    return jsonify({'mensagem': 'API SPDL online. Use /download?url=...'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)