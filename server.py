import os
import sentry_sdk

from bottle import run, route
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://2bce7a18f1f845598cdbfa101b37b456@o496202.ingest.sentry.io/5570228",
    integrations=[BottleIntegration()]
)

@route('/')
def index():
    return "Hello"

@route('/success')
def success():
    return "Success!"

@route('/fail')
def fail():
    raise RuntimeError('FAIL')

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)