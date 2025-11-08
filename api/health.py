# api/health.py
def handler(request):
    # Vercel calls the function with a request-like object.
    # Return a dict to respond with status/body/headers
    return {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": '{"ok": true, "msg": "health check"}'
    }
