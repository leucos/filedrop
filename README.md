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
FLASK_APP=upload.py flask run
```

Uploaded files will be in `./uploads/`.

## Run using container

Application is exposed by Flask on port 5000. Files are uploaded in
container under `/app/uploads` so you have to mount that path to access
it from host:

```
docker run -p 80:5000 -d --name filedrop -v /some/place:/app/uploads leucos/filedrop
```

## Mounting behind nginx

Assuming you want to run your application under '/uploads' using nginx,
this config section does the trick:

```
location ~ ^/upload(/?)(.*)$ {
    proxy_pass http://127.0.0.1:5555/$2;
    proxy_set_header X-Mount /upload;
}
```

Then run the container on the appropriate port:

docker run -p 5555:5000 -d --name filedrop -v /some/place:/app/uploads leucos/filedrop

## Credits

Contains `dropzonejs` (http://www.dropzonejs.com/).
Made with <3 by @leucos
