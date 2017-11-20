# Deploying with docker

**Note:** This documentation is intentionally generic so that it can
be copy-pasted between projects - do not put project specific details here.

This document explains how to do various sysadmin related tasks when your
site has been deployed under docker. These deployment modes are supported:

* **production**: no debug etc is enabled, has its own discrete database. Configure
  your production environment in core.settings.prod_docker - this
  DJANGO_SETTINGS_MODULE is used when running in production mode.
* **staging**: Configure your staging environment in core.settings.staging_docker -
  this DJANGO_SETTINGS_MODULE is used when running in production mode.

# Build your docker images and run them

## Production

You can simply run the provided script and it will build and deploy the docker
images for you in **production mode**.

```
cd deployment
# allow pg volume to be written to
sudo chmod -R a+rwX pg/postgres_data/
make deploy
sudo chmod -R a+rwX static
```

Now point your browser at the ip of the web container on port 8080 or to the
host port mapping as defined in the fig.yml file.


To make a superuser account do:

```
make shell
python manage.py createsuperuser
exit
```
## Local Development

Ensure that you are in the project **deployment directory**.
```
cd /path/to/django-channels-api/deployment
```
Then to setup the local development environment run the following commands:

```
make deploy
# Start the needed docker containers with
make web
# Start the web development containers with
make devweb 
```

After a succssful run of the above commands, you need to point the pycharm remote enterpreter to the remote python enterpreter for this project.

Next go to pycharm ssh remote enterpreter settings and point the **localhost** to port **64203**. 
And in edit configuration settings for the **django debug server** let the browser run on address **http://0.0.0.0:64202.**
Once these setups are in place you will be able to load the remote entrepreter python version and installed packages for development as well as being able to run the django server in the browser.

## Staging

The procedure is exactly the same as production, but you should preceed 
each command with 'staging' e.g. ``make staging-deploy``.

**Note:** VERY IMPORTANT - for staging deployment you should use a **separate
git checkout**  from the production checkout as the code from the git checkout
is shared into the source tree.

## Using make

The following key make commands are provided for production:

* **build** - build production containers
* **run** - builds then runs db and uwsgi services
* **collectstatic** - collect static in production instance
* **migrate** - run django migrations in production instance

Additional make commands are provided in the Makefile - please see there
for details.

#### Arbitrary commands

Running arbitrary management commands is easy 


## Setup nginx reverse proxy

You should create a new nginx virtual host - please see
``*-nginx.conf`` in the deployment directory for examples. There is
one provided for production and one for staging.

Simply add the example file (renaming them as needed) to your 
``/etc/nginx/sites-enabled/`` directory and then modify the contents to 
match your local filesystem paths. Then use

```
sudo nginx -t
```

To verify that your configuration is correct and then reload / restart nginx
e.g.

```
sudo /etc/init.d/nginx restart
```


### Managing containers

Please refer to the general [fig documentation](http://www.fig.sh/cli.hyml)
for further notes on how to manage the infrastructure using fig.

# Configuration options

You can configure the base port used and various other options like the
image organisation namespace and postgis user/pass by editing the ``fig*.yml``
files.
