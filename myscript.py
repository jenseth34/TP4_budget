import os
os.system('git bisect start')
os.system('git bisect run python manage.py test ')
