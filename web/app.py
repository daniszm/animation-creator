import boto3
import os
from flask import Flask
from flask import render_template, request, flash
from media.s3_storage import S3MediaStorage

app = Flask(__name__)

s3 = boto3.resource('s3')
media_storage = S3MediaStorage(s3, os.getenv('APP_BUCKET_NAME'))

@app.route("/")
def hello():
  return render_template(
    'upload_files.html'
  )

@app.route("/upload", methods=['POST'])
def handle_upload():
    if 'uploaded_file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    uploaded_file = request.files['uploaded_file']
    media_storage.store (
        dest="/uploaded/%s" % uploaded_file.filename,
        source=uploaded_file
    )
    return "OK"

@app.route("/make-animation")
def make_animation():
    return render_template(
      "make_animation.html",
      invitation="only limit is yourself"
    )

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)
