from flask import Flask, render_template_string
from markupsafe import escape
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.ERROR, filename='app_errors.log')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    safe_name = escape(name)
    return f"Hello, {safe_name}!"

# Handle 404 errors (Page Not Found)
@app.errorhandler(404)
def page_not_found(error):
    return render_template_string("<h1>404 - Page Not Found</h1>"), 404

# Handle 500 errors (Internal Server Error)
@app.errorhandler(500)
def internal_error(error):
    return render_template_string("<h1>500 - Internal Server Error</h1>"), 500

# Catch-all for unhandled exceptions (with logging only)
@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error("Unhandled Exception: %s", error, exc_info=True)
    return render_template_string("<h1>Something went wrong.</h1><p>Please try again later.</p>"), 500
