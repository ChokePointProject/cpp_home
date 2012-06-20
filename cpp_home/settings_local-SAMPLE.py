# Copy this file to settings_local.py and customize to taste

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cpp', # Or path to database file if using sqlite3.
        'USER': 'databaseuser', # Not used with sqlite3.
        'PASSWORD': 'databasepassword', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Get your cloudmade API key at http://developers.cloudmade.com/
CLOUDMADE_KEY='get_yer_key_at_www_cloudmade_com'