# from flask import Flask, request #import main Flask class and request object
from flask import send_file
import sys
from selenium import webdriver
from app3 import get_screen_shot
import os
import datetime
import json
with open('config.json') as json_data_file:
   config = json.load(json_data_file)

def execute_command(command):
   result = Popen(command, shell=True, stdout=PIPE).stdout.read()
   if len(result) > 0 and not result.isspace():
      raise Exception(result)
   return result

today=str(datetime.date.today())
app = Flask(__name__) #create the Flask app


@app.route('/snapshooter')
def snapshooter():
   url = request.args.get('url') #if key doesn't exist, returns None

   width = request.args.get('width', config['web']['default']['width']) # screen width to capture
   height = request.args.get('height', config['web']['default']['height']) # screen height to capture
   filename = request.args.get('filename', config['web']['default']['filename']) # file name e.g. screen.png
   path = request.args.get('path', config['web']['default']['path'] ) # directory path to store screen
   crop = request.args.get('crop', False) # crop the captured screen
   crop_width = request.args.get('crop_width',config['web']['default']['width']) # the width of crop screen
   crop_height = request.args.get('crop_height',config['web']['default']['height']) # the height of crop screen
   crop_replace = request.args.get('crop_replace',False) # does crop image replace original screen capture?
   file_date = request.args.get('date',str(datetime.date.today()))
   thumbnail = request.args.get('thumbnail', False) # generate thumbnail from screen, requires crop=True
   thumbnail_width = request.args.get('thumbnail_width',config['web']['default']['width']) # the width of thumbnail
   thumbnail_height = request.args.get('thumbnail_height',config['web']['default']['height']) # the height of thumbnail
   thumbnail_replace = request.args.get('thumbnail_replace',False) # does thumbnail image replace crop image?
   try:
      get_screen_shot(url=url, crop=crop, thumbnail=crop, filename=filename,width=width, height=height, file_date=file_date, path=path)
      print "get_screen_shot OK"
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
   except Exception as exception:
      print "get_screen_shot Exception"
      return "get_screen_shot Exception"


@app.route('/snapshooter2')
def snapshooter2():
   url = request.args.get('url') #if key doesn't exist, returns None

   width = request.args.get('width', config['web']['default']['width']) # screen width to capture
   height = request.args.get('height', config['web']['default']['height']) # screen height to capture
   filename = request.args.get('filename', config['web']['default']['filename']) # file name e.g. screen.png
   path = request.args.get('path', config['web']['default']['path'] ) # directory path to store screen
   crop = request.args.get('crop', False) # crop the captured screen
   crop_width = request.args.get('crop_width',config['web']['default']['width']) # the width of crop screen
   crop_height = request.args.get('crop_height',config['web']['default']['height']) # the height of crop screen
   crop_replace = request.args.get('crop_replace',False) # does crop image replace original screen capture?
   file_date = request.args.get('date',str(datetime.date.today()))
   thumbnail = request.args.get('thumbnail', False) # generate thumbnail from screen, requires crop=True
   thumbnail_width = request.args.get('thumbnail_width',config['web']['default']['width']) # the width of thumbnail
   thumbnail_height = request.args.get('thumbnail_height',config['web']['default']['height']) # the height of thumbnail
   thumbnail_replace = request.args.get('thumbnail_replace',False) # does thumbnail image replace crop image?
   screen_path, crop_path, thumbnail_path = get_screen_shot(url=url, crop=crop, thumbnail=crop, filename=filename,width=width, height=height, file_date=file_date, path=path)
   print (screen_path)
   return send_file(screen_path, mimetype='image/png')





if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0', port=5000) #run app in debug mode on port 5000


