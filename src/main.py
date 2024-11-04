import json

from .router import router
from .routes import *


# 
def main(context):
    try:
        # Parse the request payload to get the endpoint path and data
        request = context.req
        path = context.req.path
        
        if not path:
            return context.res.json({
                "status": "error",
                "message": "No path provided in payload."
            }, 400)

        # Use the router to handle the request
        context.log(f"Handling request for path: {path}")
        context.log('Query parameters', json.dumps(request.query))
        response, status = router.handle_request(path, request, context.log)
        context.log(json.dumps(response), status)
        return context.res.json(response, status, {'Access-Control-Allow-Origin': '*'})

    except ValueError as e:
        # Handle cases where no route matches
        return context.res.json({
            "status": "error",
            "message": str(e)
        }, 404, {'Access-Control-Allow-Origin': '*'})
    
    except Exception as e:
        # Handle unexpected errors
        return context.res.json({
            "status": "error",
            "message": str(e)
        }, 500, {'Access-Control-Allow-Origin': '*'})
