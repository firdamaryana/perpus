from perpus.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'firdamaryana$perpus',
    	'USER': 'firdamaryana',
	    'PASSWORD' : 'mysqlpassword',
	    'HOST':'mysql.server'
    }
}
