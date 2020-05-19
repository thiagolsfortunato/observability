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

hostname = os.getenv("HOSTNAME", default = "service_c")
SERVICE_HOST = os.getenv("SERVICE_HOST", default = "localhost")
SERVICE_PORT = os.getenv("SERVICE_PORT", default = "3000")
SERVICE_URL = "http://{0}:{1}".format(SERVICE_HOST, SERVICE_PORT)

app = Flask(__name__)

messages = ["ada", "cdawcs", "biasjy", "polasi", "nasjba"]

@app.route('/', methods=['GET'])
def name():
  msg = """
  <h1>Welcome to Message App :)</h1>
  <h3>Hostname: {0}</h3>
  """.format(hostname)
  logger.info('[SERVICE-C]', extra={'hostname': hostname, 'method': request.method, 'url': request.url, 'user-agent': request.user_agent})
  logger.info(msg, extra={'status': 200, 'content_type': 'text/html'})
  return Response(msg, status=200, content_type="text/html")

@app.route('/search', methods=['GET'])
def get():
  logger.info('[SERVICE-C]', extra={'hostname': hostname, 'method': request.method, 'url': request.url, 'user-agent': request.user_agent})
  if request.args.get('msg'):
    msg = request.args.get('msg')
    params = {'msg': msg}
    resp = requests.get(SERVICE_URL + "/search", params=params)
  else:
    resp = requests.get(SERVICE_URL+ "/search")
  logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
  return Response(resp.text, status=resp.status_code, content_type=resp.headers['content-type'])

@app.route('/add', methods=['POST'])
def save():
  logger.info('[SERVICE-C]', extra={'hostname': hostname, 'method': request.method, 'url': request.url, 'user-agent': request.user_agent})
  if request.args.get('msg'):
    msg = request.args.get('msg')
    params = {'msg': msg}
    resp = requests.post(SERVICE_URL + "/add", params=params)
    logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
  return Response(resp.text, status=resp.status_code, content_type=resp.headers['content-type'])

@app.route('/delete', methods=['DELETE'])
def delete():
  logger.info('[SERVICE-C]', extra={'hostname': hostname, 'method': request.method, 'url': request.url, 'user-agent': request.user_agent})
  if request.args.get('msg'):
    msg = request.args.get('msg')
    params = {'msg': msg}
    resp = requests.delete(SERVICE_URL + "/delete", params=params)
    logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
  return Response(resp.text, status=resp.status_code, content_type=resp.headers['content-type'])

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8003)

  # if request.args.get('msg'):
  #   msg = request.args.get('msg')
  #   res = ""
  #   for message in messages:
  #     if msg == message:
  #       res = msg
  #   if res:
  #     # logger.info(res, extra={'status': 200, 'url': resp.url})
  #     return jsonify(res), 200
  #   else:
  #     # logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
  #     return jsonify("msg not found"), 404
  # if request.args.get('sorted'):
  #   # logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
  #   return jsonify(messages.sort()), 200
  # # logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
  # return jsonify(messages), 200
    
  # if request.args.get('message'):
  #   msg = request.args.get('message')
  #   params = {'message': msg}
  #   resp = requests.get(SERVICE_DB_URL + "/search", params=params)
  # else:
  #   resp = requests.get(SERVICE_DB_URL+ "/search")
  # app.logger.info(resp)
  # return Response(resp.text, status=resp.status_code, content_type=resp.headers['content-type'])

# @app.route('/add', methods=['POST'])
# def save():
#   logger.info('[SERVICE-C]', extra={'hostname': hostname, 'method': request.method, 'url': request.url, 'user-agent': request.user_agent})
#   if request.args.get('msg'):
#     msg = request.args.get('msg')
#     if msg not in messages:
#       messages.append(msg)
#       index = messages.index(msg)
#       # logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
#       return jsonify(index), 200
#     else:
#       # logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
#       return jsonify('message already exists'), 409
#   # logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})      
#   return jsonify('error'), 400

  # logger.info(hostname, extra={'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})

  # resp = requests.post(SERVICE_DB_URL + "/add", json=message)
  # app.logger.info(resp.text, resp.status_code)
  # return Response(resp.text, status=resp.status_code, content_type=resp.headers['content-type'])

# @app.route('/delete', methods=['DELETE'])
# def delete():
#   logger.info('[SERVICE-C]', extra={'hostname': hostname, 'method': request.method, 'url': request.url, 'user-agent': request.user_agent})
#   if request.args.get('msg'):
#     msg = request.args.get('msg')
#     if msg in messages:
#       index = messages.index(msg)
#       messages.pop(index)
#       # logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
#       return jsonify(index), 200
#     else:
#       # logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
#       return jsonify('Message not found'), 404
#   # logger.info('[SERVICE-C]', extra={'hostname': hostname, 'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})
#   return jsonify('error'), 400

  # logger.info(hostname, extra={'status': resp.status_code, 'url': resp.url, 'data': resp.text, 'content-type': resp.headers['content-type']})

  # params = {'message': msg}
  # resp = requests.delete(SERVICE_DB_URL + "/delete", params=params)
  # app.logger.message(resp)
  # return Response(resp.text, status=resp.status_code, content_type=resp.headers['content-type'])

