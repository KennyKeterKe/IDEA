from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/junyu/Desktop/Storage'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['GET', 'POST'])
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print("Saving file to:", save_path)
        file.save(save_path)
        return 'File uploaded successfully!'
    else:
        return 'No file selected.'

if __name__ == '__main__':
    app.run()

