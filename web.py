from flask import Flask, request #import main Flask class and request object
import sys
from selenium import webdriver
from app import get_screen_shot
import os
import datetime
abspath = lambda *p: os.path.abspath(os.path.join(*p))
ROOT = "/root/flask_nodejs/screenshots"
today=str(datetime.date.today())
app = Flask(__name__) #create the Flask app


@app.route('/snapshooter')
def snapshooter():
   url = request.args.get('url') #if key doesn't exist, returns None

   width = request.args.get('width', 1024) # screen width to capture
   height = request.args.get('height', 768) # screen height to capture
   filename = request.args.get('filename', 'screen') # file name e.g. screen.png
   path = request.args.get('path', ROOT ) # directory path to store screen
   crop = request.args.get('crop', False) # crop the captured screen
   crop_width = request.args.get('crop_width',width) # the width of crop screen
   crop_height = request.args.get('crop_height',height) # the height of crop screen
   crop_replace = request.args.get('crop_replace',False) # does crop image replace original screen capture?
   file_date = request.args.get('date',today)
   thumbnail = request.args.get('thumbnail', False) # generate thumbnail from screen, requires crop=True
   thumbnail_width = request.args.get('thumbnail_width',width) # the width of thumbnail
   thumbnail_height = request.args.get('thumbnail_height',height) # the height of thumbnail
   thumbnail_replace = request.args.get('thumbnail_replace',False) # does thumbnail image replace crop image?

   screen_path = get_screen_shot(url=url, crop=crop, thumbnail=crop, filename=filename,width=width, height=height, file_date=file_date, path=path)
   return '''
<h1>Screenshoting URL: {}</h1>
<p><strong>Possible parameters:</strong></p>
<p><strong>Required:</strong></p>
<p>url = URL of page to save</p>
<p><strong>Optional:</strong></p>
<p><br /> width = default (1024)&nbsp;# screen width to capture<br /> height = default (768)&nbsp; # screen height to capture<br /> filename = default ('screen.png') # file name e.g. screen.png<br /> path = default (ROOT) # directory path to store screen</p>
<p><br /> crop = default (False) # crop the captured screen<br /> crop_width =(width)# the width of crop screen<br /> crop_height = (height) # the height of crop screen<br /> crop_replace = (False) # does crop image replace original screen capture?</p>
<p>thumbnail = default (False) # generate thumbnail from screen, requires crop=True<br /> thumbnail_width = (width) # the width of thumbnail<br /> thumbnail_height = (height) # the height of thumbnail<br /> thumbnail_replace = (False) # does thumbnail image replace crop image?</p>
<p>Created by</p>
<p>Tomasz Michalowski</p>
<p>&nbsp;</p>
'''.format(url)


if __name__ == '__main__':
   app.run(debug=True, port=5000) #run app in debug mode on port 5000

