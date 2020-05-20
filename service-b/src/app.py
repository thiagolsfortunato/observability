import os
import sys
import requests
import logging
import json_log_formatter
from flask import Flask, request, jsonify, Response

# Logging
formatter = json_log_formatter.JSONFormatter()
json_handler = logging.StreamHandler(sys.stdout)
json_handler.setFormatter(formatter)
logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

hostname = os.getenv("HOSTNAME", default = "service_b")
SERVICE_HOST = os.getenv("SERVICE_HOST", default = "localhost")
SERVICE_PORT = os.getenv("SERVICE_PORT", default = "8003")
SERVICE_URL = "http://{0}:{1}".format(SERVICE_HOST, SERVICE_PORT)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def name():
  msg = """
  <h1>Welcome to Message App :)</h1>
  <h3>Hostname: {0}</h3>
  """.format(hostname)
  logger.info('[SERVICE-B]', extra={'hostname': hostname, 'method': request.method, 'url': request.url, 'user-agent': request.user_agent})
  return Response(hostname, status=200, content_type="text/html")

@app.route('/search', methods=['GET'])
def get():
  logger.info('[SERVICE-B]', extra={'hostname': hostname, 'method': request.method, 'url': request.url, 'user-agent': request.user_agent})
  if request.args.get('msg'):
    msg = request.args.get('msg')
    params = {'msg': msg}
    resp = requests.get(SERVICE_URL + "/search", params=params)
  else:
    resp = requests.get(SERVICE_URL+ "/search")
  logger.info('[SERVICE-B]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
  return Response(resp.text, status=resp.status_code, content_type=resp.headers['content-type'])

@app.route('/add', methods=['POST'])
def save():
  logger.info('[SERVICE-B]', extra={'hostname': hostname, 'method': request.method, 'url': request.url, 'user-agent': request.user_agent})
  if request.args.get('msg'):
    msg = request.args.get('msg')
    params = {'msg': msg}
    resp = requests.post(SERVICE_URL + "/add", params=params)
    logger.info('[SERVICE-B]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
  return Response(resp.text, status=resp.status_code, content_type=resp.headers['content-type'])

@app.route('/delete', methods=['DELETE'])
def delete():
  logger.info('[SERVICE-B]', extra={'hostname': hostname, 'method': request.method, 'url': request.url, 'user-agent': request.user_agent})
  if request.args.get('msg'):
    msg = request.args.get('msg')
    params = {'msg': msg}
    resp = requests.delete(SERVICE_URL + "/delete", params=params)
    logger.info('[SERVICE-B]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
  return Response(resp.text, status=resp.status_code, content_type=resp.headers['content-type'])

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8002)