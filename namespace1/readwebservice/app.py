import os

from flask_util_job_runner.definitions import get_minio_client
from flask_util_job_runner.flask_utils import setup_app, declare_method

from namespace1.readwebservice.utils import MyJob

app = setup_app()
kwargs = {'mc': get_minio_client()}
declare_method(app, 'readwebservice', MyJob, **kwargs)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8086)))
