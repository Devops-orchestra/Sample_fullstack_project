import logging
import os
from flask import Flask, render_template_string, request
from markupsafe import escape

app = Flask(__name__)

# Set a secure secret key (required for session security)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "your-default-insecure-key")  # Replace in production

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.FileHandler("errors.log"),
        logging.StreamHandler()
    ]
)

@app.route("/")
def hello_world():
    app.logger.info("Accessed home page")
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    safe_name = escape(name)
    app.logger.debug(f"Greeting user: {safe_name}")
    return f"Hello, {safe_name}!"

@app.errorhandler(404)
def page_not_found(error):
    app.logger.warning(f"404 Not Found: {request.path}")
    return render_template_string("<h1>404 - Page Not Found</h1>"), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"500 Internal Server Error: {request.path}")
    return render_template_string("<h1>500 - Internal Server Error</h1>"), 500

@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.exception("Unhandled Exception:")
    return render_template_string("<h1>Something went wrong.</h1><p>Please try again later.</p>"), 500
