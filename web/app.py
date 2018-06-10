import boto3, os, json, uuid, imageio
from flask import Flask
from flask import render_template, request, flash
from media.s3_storage import S3MediaStorage
from media.name_generator import generate_name

app = Flask(__name__)

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

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)
