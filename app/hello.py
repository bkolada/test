import logging
from flask import Flask, jsonify

app = Flask(__name__)
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

@app.route('/')
def default_route():
    app.logger.debug('this is a DEBUG message')
    app.logger.info('this is an INFO message')
    app.logger.warning('this is a WARNING message')
    app.logger.error('this is an ERROR message')
    app.logger.critical('this is a CRITICAL message')
    return 'aoeu'

@app.route('/err')
def r():
    raise Exception('dupa')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
