"""
Responsible for using the different vendors for sending the mail message.
"""

import logging

from mailsenderengine.vendors.mailgun import MailGunMailSender
from mailsenderengine.vendors.sendgrid import SendGridMailSender

_logger = logging.getLogger(__name__)

class _MailSender:
    def __init__(self):
        self.mailers = [
            SendGridMailSender,
            MailGunMailSender
        ]

    def send_message(self, message):    
        for mailer in self.mailers:
            status, response = mailer.send_message(message)
            if status:
                return True, response
        _logger.error('Could not send mail via any of the mailers', exc_info=True)
        return False, None


mail_sender = _MailSender()
