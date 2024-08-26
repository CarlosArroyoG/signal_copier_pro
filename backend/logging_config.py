import logging
from logging.handlers import RotatingFileHandler

def configure_logging(app):
    if not app.debug:
        file_handler = RotatingFileHandler('signal_copier.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Signal Copier startup')