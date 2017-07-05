"""
Module for encapsulating send grid related.
"""

import logging

_logger = logging.getLogger(__name__)

class SendGridMailSender:
    """
    Mail sender encapsulating all the logic for SendGrid
    """
    def send_message(self, message):
        _logger.debug('Attempting to send message %s via sendgrid', message)
        return False, None