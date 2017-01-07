# Simple multi filedrop Flask application

This small app lets you start a quick upload server. Files will not be
clobbered by subsequent uploads.

## Run using source

Install requirements:

```
sudo pip3 install -r requirements.txt
```

then run the app:

```
FLASK_APP=filedrop.py flask run
```

Head to http://localhost:5000

Uploaded files will be in `./uploads/`.

## Run using container

Application is exposed by Flask on port 5000. Files are uploaded in
container under `/app/uploads` so you have to mount that path to access
it from host:

```
docker run -p 80:5000 -d --name filedrop -v /some/place:/app/uploads leucos/filedrop
```

You can build the container yourself if you prefer:

```
docker build . -t you/filedrop
```

## Running behind nginx

Assuming you want to run your application under `/uploads` using nginx,
this config section does the trick:

```
location ~ ^/upload(/?)(.*)$ {
    proxy_pass http://127.0.0.1:5555/$2;
    proxy_set_header X-Mount /upload;
}
```

Then run the container on the appropriate port:

```
docker run -p 5555:5000 -d --name filedrop -v /some/place:/app/uploads leucos/filedrop
```

or the app if you prefer:

```
FLASK_APP=filedrop.py flask run --port 5555
```

The `X-Mount` option will help `filedrop` relocate itself at the proper
location. It is not needed if you want to serve the app at `/`.

## Credits

Released under WTFPL licence https://en.wikipedia.org/wiki/WTFPL
except for the contained `dropzonejs` code (http://www.dropzonejs.com/).

Made with <3 by @leucos

