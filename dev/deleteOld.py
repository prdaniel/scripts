import os
import datetime

dir_to_search = 'C:/Endeca/apps/discoverAuthoring/logs/logserver_output/'
for dirpath, dirnames, filenames in os.walk(dir_to_search):
   for file in filenames:
      curpath = os.path.join(dirpath, file)
      file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
      if datetime.datetime.now() - file_modified > datetime.timedelta(hours=120):
          os.remove(curpath)