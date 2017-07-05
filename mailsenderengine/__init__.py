"""
Initialises the root package
"""

import logging.config

from mailsenderengine.config import settings

logging.config.dictConfig(settings.logger_config)
