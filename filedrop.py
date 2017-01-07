from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, ALL

import os
import sys

#app_root = os.environ.get('APPLICATION_ROOT', '/')
#print(" * Using root:  %s" % app_root, file=sys.stderr)

fileset = UploadSet('files', ALL)

app = Flask(__name__)
app.config['UPLOADED_FILES_DEST'] = 'uploads/'

configure_uploads(app, fileset)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'file' in request.files:
        filename = fileset.save(request.files['file'])
        return filename

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
