<<<<<<< HEAD
import boto3, os, json, uuid
from flask import Flask
from flask import render_template, request, flash
from media.s3_storage import S3MediaStorage
from media.name_generator import generate_name

=======
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from media.s3_storage import S3MediaStorage
import os
import boto3
import json

#class FilePhotoStack:
    #def add_pending_photo(self, target_name) 
#otworz plik, dopisz do pliku, zamknij plik



class InMemoryPhotoStack:
    def __init__(self):
       self.photos_list = []
    def get_all_photos(self):
       return self.photos_list
    def add_pending_photo(self, target_name):
       self.photos_list.append(target_name) 
s3 = boto3.resource('s3')
storage = S3MediaStorage(s3, os.getenv('APP_BUCKET_NAME'))
>>>>>>> 61eda2c20993700952d18dc68c0c07c2a0acc3cc
app = Flask(__name__)
photo_stack = InMemoryPhotoStack()
sqs = boto3.resource('sqs', region_name="eu-central-1")
pending_orders = sqs.get_queue_by_name(QueueName='JUSTYNAsQUEUE')

s3 = boto3.resource('s3')
media_storage = S3MediaStorage(s3, os.getenv('APP_BUCKET_NAME'))

photos = []

sqs = boto3.resource('sqs', region_name="eu-central-1")
queueRequest = sqs.get_queue_by_name(QueueName=os.getenv('APP_QUEUE_NAME'))

#while True:
#  for message in tweets.receive_messages():
#    print('Message body: %s' % message.body)
#    message.delete()
#  time.sleep(1)

@app.route("/")
def hello():
<<<<<<< HEAD
  return render_template(
    'upload_files.html'
  )

@app.route("/upload", methods=['POST'])
def handle_upload():
  if 'uploaded_file' not in request.files:
    flash('No file part')
    return redirect(request.url)
  uploaded_file = request.files['uploaded_file']
  file_ref = generate_name(uploaded_file.filename)
  get_ref = file_ref + uploaded_file.filename
  media_storage.store (
    dest=get_ref,
    source=uploaded_file
  )
  photos.append(media_storage.contains(get_ref))

#  images = []
#  for photo in photos:
#    images.append(imageio.imread(photo))
#  output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
#  imageio.mimsave(output_file, images, duration=duration)
  
#  media_storage.store (
#    dest=file_ref + output_file.filename,
#    source=output_file
#  )

#  orders.load(current_user()).add_file(file_ref)
  return render_template(
    'sendto.html'
  )

@app.route("/proceed")
def proceed_animation():
  ani_request = {
    "email": request.form['email'],
    "photos": photos
  }

  queueRequest.send_message(MessageBody=json.dumps(ani_request))
  return "OK"

#  order = orders.load(current_user())
#  handler.handle(order,snapshot())

@app.route("/make-animation")
def make_animation():
  return render_template(
    "make_animation.html",
    invitation="only limit is yourself"
  )
=======
    return render_template('upload_form.html')

@app.route("/upload", methods=['POST'])
def make_upload():
    if 'filetoupload' not in request.files:
      return 'fail'
    myfile = request.files['filetoupload']
    target_name = "uploads/%s"%myfile.filename
    storage.store(dest=target_name, source=myfile)
    photo_stack.add_pending_photo(target_name)
    return 'ok'

@app.route("/order")
def order():
    return render_template('order.html', photos=photo_stack.get_all_photos())

@app.route("/proceed", methods=['POST'])
def proceed():
    order_ani_request = {'email': request.form['email'], 'photos': photo_stack.get_all_photos()}
    pending_orders.send_message(MessageBody=json.dumps(order_ani_request))

    return redirect(url_for('order'))
>>>>>>> 61eda2c20993700952d18dc68c0c07c2a0acc3cc

@app.route("/list")
def list():
    mydata=[{"name": "Jakub"}, {"name": "Justyna"}]
    return render_template('peoples.html', peoples=mydata)
if __name__ == '__main__':
<<<<<<< HEAD
  app.run(host="0.0.0.0", port=8080, debug=True)
=======
  app.run(host="0.0.0.0", port=8080, debug=True)
>>>>>>> 61eda2c20993700952d18dc68c0c07c2a0acc3cc
