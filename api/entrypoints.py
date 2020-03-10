import os

import redis
import requests
from flask import jsonify
from flask_util_job_runner.api_utils import secured_with_token, with_request_params, handle
from flask_util_job_runner.definitions import REDIS_ADDRESS
from flask_util_job_runner.flask_utils import setup_app

app = setup_app()

pool = redis.ConnectionPool(REDIS_ADDRESS, port=6379, db=0)
r = redis.Redis(connection_pool=pool)


@app.route("/health", methods=['GET'])
@secured_with_token()
def health():
    urls_to_ping = ['http://webservice.namespace1/ping', 'http://asyncwebservice.namespace1/ping',
                    'http://readwebservice.namespace1/ping', 'http://minio-hl.minio:9000/minio/health/live']
    status = {}
    status_up_all = True
    for utp in urls_to_ping:
        status[utp], status_up = get_status(utp)
        status_up_all = status_up_all and status_up
    status_redis_up = r.ping()
    status_up_all = status_up_all and status_redis_up
    status['redis'] = {'status': 'ok'} if status_redis_up else {'status': 'down'}
    if status_up_all:
        return jsonify(status)
    else:
        return jsonify(status), 500


def get_status(utp):
    status_ok_constant = {'status': 'ok'}
    status_down_constant = {'status': 'down'}
    try:
        resp = requests.get(utp, timeout=2)
    except requests.exceptions.RequestException as e:
        return status_down_constant, False
    if resp.ok:
        return status_ok_constant, True
    else:
        return status_down_constant, False


@app.route("/webservice", methods=['POST'])
@secured_with_token()
@with_request_params(["data"])
def webservice(data, uuid_str):
    version = 'namespace1'
    method_name = 'webservice'
    app.logger.info("webservice call")
    return handle(method_name, version, uuid_str, {'data': data, 'uuid_str': uuid_str})


@app.route("/readwebservice", methods=['POST'])
@secured_with_token()
@with_request_params(["uuid_requested"])
def readwebservice(uuid_requested, uuid_str):
    version = 'namespace1'
    method_name = 'readwebservice'
    return handle(method_name, version, uuid_str, {'uuid_requested': uuid_requested, 'uuid_str': uuid_str})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8081)))
