from flask import Flask, request, jsonify, render_template, send_from_directory, make_response
import flask, os
from model import tempo, waveshow

app = Flask(__name__)

UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['wav'])

@app.route('/test/upload')
def upload_test():
    return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def create_text(filename, result):
    result_text = str(result)
    text_filename = filename.replace('wav', 'txt')
    text_file_path = "result/"+ text_filename
    text_file = open(text_file_path, 'w')
    text_file.write(result_text)
    print(text_filename)
    return text_filename

def api_download(dirpath, text_filename):
    response = make_response(send_from_directory(dirpath, text_filename, as_attachment=True))
    return response

def return_img_stream(img_path):
    import base64
    img_stream = ""
    with open(img_path, "rb") as img_file:
        img_stream = img_file.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream

@app.route("/api/upload", methods=["GET", "POST"], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    if flask.request.method == "POST":
        print('request method is POST')
        audio = request.files["audio"]
        if audio and allowed_file(audio.filename):
            print("已读取文件")
            audio_filename = str(audio.filename)
            audio.save(os.path.join(file_dir, audio_filename))
            audio_path = os.path.join(file_dir, audio_filename)
            img_path = waveshow(audio_path)
            img_stream = return_img_stream(os.path.join("/root/myproject/",img_path))
            result =  tempo(audio_path)
            return render_template('upload.html', img_stream = img_stream, state = "SUCCESS",result = result)

if __name__ == "__main__":
    app.run()
