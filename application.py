import os
from flask import Flask

application = Flask(__name__)


@application.route("/")
def home():
    app_env = os.environ.get("APP_ENV", "not set")
    color = os.environ.get("APP_COLOR", "blue")
    debug = os.environ.get("DEBUG_MODE", "not set")
    version = "1.0"
    return (
        f"<body style='font-family:Arial;text-align:center;padding-top:60px;background:{color};color:white'>"
        f"<h1>Elastic Beanstalk CI/CD - Version {version}</h1>"
        f"<h2>Environment: {app_env}</h2>"
        f"<p>DEBUG_MODE = {debug}</p>"
        f"<p>Deployed automatically by CodePipeline - Arnav Gandhi</p>"
        f"</body>"
    )


@application.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000)