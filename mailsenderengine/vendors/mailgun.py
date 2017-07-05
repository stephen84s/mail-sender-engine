"""
Connects to the mail gun host and sends emails
"""

import logging
import requests

from mailsenderengine.config import settings

_logger = logging.getLogger(__name__)


class MailGunMailSender:
    """
    Encapsulates the logic for sending via the MailGun API
    """
    def send_message(self, message):
        """
        Sends the mail message via the Mail gun server
        """
        _logger.debug('Attempting to send message %s, via mailgun', message)
        try:
            url = settings.mailers['mailgun']['url']
            auth = ('api', settings.mailers['mailgun']['token'])
            data = {
                'from': message['from'],
                'to': message['to'],
                'subject': message['subject'],
                'text': message['text']
            }

            response = requests.post(url, auth=auth, data=data)
            _logger.info('Mail sent, response received: %s', response)
            
        except Exception as err: #pylint: disable=W0703
            _logger.error('Error encountered while sending mail via mailgun: %s', err)
            return False, {'error': err}
