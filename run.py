#!/usr/bin/env python

from __init__ import app

@app.context_processor
def asset_path_context_processor():
    return {'asset_path': '/static/govuk_template/'}


app.run(debug=True)
