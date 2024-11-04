
class Router:
    def __init__(self):
        self.routes = {}
        
    def route(self, path):
        """Decorator to register a route."""
        def wrapper(func):
            self.routes[path] = func
            return func
        return wrapper

    def handle_request(self, path, *args, **kwargs):
        """Dispatch request to the correct route handler."""
        args[2].log(self.routes)
        if path in self.routes:
            return self.routes[path](*args, **kwargs)
        else:
            raise ValueError(f"No handler for route: {path}")

# Initialize router
router = Router()
