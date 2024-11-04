from router import Router


# 
def main(req, res):
    try:
        # Parse the request payload to get the endpoint path and data
        payload = json.loads(req.payload)
        path = payload.get("path")
        
        if not path:
            return res.json({
                "status": "error",
                "message": "No path provided in payload."
            }, status=400)

        # Use the router to handle the request
        response, status = router.handle_request(path, payload)
        return res.json(response, status=status)

    except ValueError as e:
        # Handle cases where no route matches
        return res.json({
            "status": "error",
            "message": str(e)
        }, status=404)
    
    except Exception as e:
        # Handle unexpected errors
        return res.json({
            "status": "error",
            "message": str(e)
        }, status=500)
