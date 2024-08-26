import json
from flask import Response

def json_response(data, status=200):
    return Response(
        json.dumps(data),
        status=status,
        mimetype='application/json'
    )

def format_date(date):
    return date.strftime('%Y-%m-%d %H:%M:%S')