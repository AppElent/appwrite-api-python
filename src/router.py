
class Router:
    def __init__(self, context):
        self.routes = {}
        self.context = context

    def route(self, path):
        """Decorator to register a route."""
        def wrapper(func):
            self.routes[path] = func
            return func
        return wrapper

    def handle_request(self, path, *args, **kwargs):
        """Dispatch request to the correct route handler."""
        context.log(self.routes)
        if path in self.routes:
            return self.routes[path](*args, **kwargs)
        else:
            raise ValueError(f"No handler for route: {path}")

# Initialize router
router = Router()
