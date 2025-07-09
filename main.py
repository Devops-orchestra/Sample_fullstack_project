from flask import Flask, render_template_string
from markupsafe import escape

app = Flask(__name__)

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

# Optional: Catch-all for uncaught exceptions
@app.errorhandler(Exception)
def unhandled_exception(error):
    return render_template_string(f"<h1>Unexpected Error:</h1><p>{escape(str(error))}</p>"), 500
