cpp_home
========
The ChokePoint Project map page, now in a tasty Python flavour.

## Requirements
  * django 1.4 - https://docs.djangoproject.com/en/dev/intro/install/
  * django-compositekey HEAD - https://github.com/simone/django-compositekey.git
  
## Installation
  * Copy cpp_home/settings_local-SAMPLE.py to cpp_home/settings_local.py and 
  ** Edit settings_local.py to match your environment.
  ** Please specify your own CloudMade API key. Get yours at http://CloudMade.com/
  * If using Eclipse+pydev, copy pydevproject-SAMPLE to .pydevproject

## Running
```
$ cd cpp_home
$ python manage.py runserver 
```
  
