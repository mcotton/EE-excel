## EE-excel ##

You need to do some stuff to get this up and running

 - this is using python 3, should be minor work on convert backwards to python 2
 - you'll need to have requests, flask, openpyxl installed
 - create an `uploads` directory
 - set debug to `False `
 - `pip3 install -r requirements.txt`
 - `export FLASK_ENV=production`
 - `chomod +x startup.sh`
 - `./startup.sh`


 actually, you should really just use docker

  - `docker build -t ee-excel .`
  - `docker run -d -p 4000:4000 ee-excel`