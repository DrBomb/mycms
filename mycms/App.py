from flask import Flask, render_template, request, url_for
import json, os

app = Flask(__name__)

def create_app(settings):
    app = Flask(__name__)
    app.config.from_object(settings)
    if os.getenv("REACT") is not None:
        @app.context_processor
        def redo_url():
            def url_for_new(endpoint,**values):
                import re
                match = re.search("bundles",values.get("filename"))
                if match is not None:
                    return "".join([os.getenv("REACT"),"/static/",values.get('filename')])
                else:
                    return url_for(endpoint,**values)
            return dict(url_for=url_for_new)

    @app.route("/")
    @app.route("/index")
    def index():
        return render_template("index.html")
    @app.route("/api")
    def api():
        return json.dumps(app.config)
    return app
