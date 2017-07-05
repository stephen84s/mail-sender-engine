logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'precise': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'precise',
            'stream': 'ext://sys.stdout',
            'level': 'DEBUG'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG'
        }
    }
}

mailers = {
    'sendgrid': {
        'token':''
    },
    'mailgun': {
        'token': '',
        'url': 'https://api.mailgun.net/v3/sandbox56d903eb62b64bf9bac0151a79e417eb.mailgun.org/messages'
    }
}