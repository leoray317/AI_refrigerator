import shutil
import urllib.request as request
from contextlib import closing


username =r'user'
password =r'12345'

with closing(request.urlopen(f'ftp://{username}:{password}@127.0.0.1/nobody/test.txt')) as r:
    with open('test.txt', 'wb') as f:
        shutil.copyfileobj(r, f)