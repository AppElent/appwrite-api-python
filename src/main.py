import json

from .router import Router


# 
def main(context):
    try:
        # Parse the request payload to get the endpoint path and data
        payload = json.loads(context.req.payload)
        path = payload.get("path")
        
        if not path:
            return context.res.json({
                "status": "error",
                "message": "No path provided in payload."
            }, 400)

        # Use the router to handle the request
        response, status = router.handle_request(path, payload)
        return context.res.json(response, status)

    except ValueError as e:
        # Handle cases where no route matches
        return context.res.json({
            "status": "error",
            "message": str(e)
        }, 404)
    
    except Exception as e:
        # Handle unexpected errors
        return context.res.json({
            "status": "error",
            "message": str(e)
        }, 500)
