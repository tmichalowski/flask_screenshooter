import os
from subprocess import Popen, PIPE
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import json
with open('config.json') as json_data_file:
   config = json.load(json_data_file)

abspath = lambda *p: os.path.abspath(os.path.join(*p))
ROOT = "/root/flask_nodejs/img"
today=datetime.date.today()

def execute_command(command):
   result = Popen(command, shell=True, stdout=PIPE).stdout.read()
   if len(result) > 0 and not result.isspace():
      raise Exception(result)


def do_screen_capturing(url, screen_path, width, height):
   options = webdriver.ChromeOptions()
   options.binary_location = ("/usr/bin/google-chrome-stable")

   for i in config["app"]["chrome_options"]:
      options.add_argument(i)

   driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options) #executable_path="/usr/local/bin/geckodriver")
   driver.set_window_size(width, height)
   driver.set_page_load_timeout(30)

   timeout = 20

   driver.get(url)
   try:



      element_present = EC.presence_of_element_located((By.ID, 'element_id'))
      WebDriverWait(driver, timeout).until(element_present)
      element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'element_id')))
   except TimeoutException:
      pass


   driver.save_screenshot(screen_path)

   driver.close()

def do_crop(params):
   print ("Croping captured image..")
   command = [
      'convert',
      params['screen_path'],
      '-crop', '%sx%s+0+0' % (params['width'], params['height']),
      params['crop_path']
   ]
   execute_command(' '.join(command))


def do_thumbnail(params):
   print ("Generating thumbnail from croped captured image..")
   command = [
      'convert',
      params['crop_path'],
      '-filter', 'Lanczos',
      '-thumbnail', '%sx%s' % (params['width'], params['height']),
      params['thumbnail_path']
   ]
   execute_command(' '.join(command))


def get_screen_shot(**kwargs):
   url = kwargs['url']
   width = int(kwargs.get('width', 1920)) # screen width to capture
   height = int(kwargs.get('height', 1080)) # screen height to capture
   filename = kwargs.get('filename', 'screen') # file name e.g. screen.png
   path = kwargs.get('path', ROOT) # directory path to store screen
   file_date = kwargs.get('date', str(today))
   crop = kwargs.get('crop', False) # crop the captured screen
   crop_width = int(kwargs.get('crop_width', width)) # the width of crop screen
   crop_height = int(kwargs.get('crop_height', height)) # the height of crop screen
   crop_replace = kwargs.get('crop_replace', False) # does crop image replace original screen capture?

   thumbnail = kwargs.get('thumbnail', False) # generate thumbnail from screen, requires crop=True
   thumbnail_width = int(kwargs.get('thumbnail_width', width)) # the width of thumbnail
   thumbnail_height = int(kwargs.get('thumbnail_height', height)) # the height of thumbnail
   thumbnail_replace = kwargs.get('thumbnail_replace', False) # does thumbnail image replace crop image?
   filename="_".join([str(file_date),filename])
   filename="".join([filename,".png"])
   screen_path = abspath(path, filename)
   crop_path = thumbnail_path = screen_path

   if thumbnail and not crop:
      raise Exception('Thumnail generation requires crop image, set crop=True')

   do_screen_capturing(url, screen_path, width, height)

   if crop:
      if not crop_replace:
         crop_path = abspath(path, 'crop_'+filename)
      params = {
         'width': crop_width, 'height': crop_height,
         'crop_path': crop_path, 'screen_path': screen_path}
      do_crop(params)

      if thumbnail:
         if not thumbnail_replace:
            thumbnail_path = abspath(path, 'thumbnail_'+filename)
         params = {
            'width': thumbnail_width, 'height': thumbnail_height,
            'thumbnail_path': thumbnail_path, 'crop_path': crop_path}
         do_thumbnail(params)
   return screen_path, crop_path, thumbnail_path


if __name__ == '__main__':
   '''
       Requirements:
       install selenium (in your virtualenv, if you are using that)
       install chrome and chromedriver
   '''

   url = "http://play.grafana-zabbix.org/d/000000024/triggers?orgId=2"
#   url = "http://play.grafana-zabbix.org/d/000000011/grafana-zabbix-org?orgId=2"
   screen_path, crop_path, thumbnail_path = get_screen_shot(
      url=url, filename='sof.png',
      crop=True, crop_replace=False,
      thumbnail=True, thumbnail_replace=False,
      thumbnail_width=200, thumbnail_height=150,
   )
