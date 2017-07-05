"""
Entry point for the mail sender module
"""
import logging

from flask import Flask, request, jsonify
from flask_cors import CORS

from mailsenderengine.validators import validate_message
from mailsenderengine.mailsender import mail_sender

mailer = Flask(__name__)
CORS(mailer)
_logger = logging.getLogger("mailsenderengine")


@mailer.route("/", methods=["POST"])
def send_message():
    """
    Takes input message and sends it via the mail servers.
    """
    try:
        message = request.get_json()
        _logger.debug('Message received: %s', message)
        if message is not None and validate_message(message):
            status, response = mail_sender.send_message(message)
            if status:
                return jsonify({
                    'message_id': response['message_id'],
                    'errors': response['errors']
                })
            return jsonify({
                'errors': response['errors']
            }), 400
        return jsonify({
            'errors': ['Message was not provided']
        })

    except Exception:  # pylint: disable=W0703
        _logger.error("A unhandled error was encountered", exc_info=True)
        return jsonify({}), 500
