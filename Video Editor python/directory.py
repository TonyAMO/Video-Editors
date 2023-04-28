import os

def path():
   if not os.path.exists('C:\\Project Repo'):
      os.makedirs('C:\\Project Repo')
   return 'C:\\Project Repo'