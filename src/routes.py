from .router import router
from .services.recipe_scraper_service import RecipeScraperService


@router.route("/recipes/scrape")
def scrape_recipe_handler(request, log):
    url = request.query.get('url')
    online = request.query.get("online", "true").lower() != "false"
    supported_only = request.query.get("supported_only", "false").lower() != "false"
    if not url:
        return {"status": "error", "message": "No URL provided in payload."}, 400

    try:
        # Use the RecipeScraperService to get recipe details
        scraper_service = RecipeScraperService(url, online=online, supported_only=supported_only)
        recipe_details = scraper_service.get_recipe_json()
        return {"status": "success", "data": recipe_details}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

@router.route("/health-check")
def health_check_handler(request, log):
    return {"status": "success", "message": "Health check passed!"}, 200

@router.route("/")
def health_check_handler(request, log):
    log('Base path reached')
    return {"status": "success", "message": "You reached Python API"}, 200

# You can define more routes and handlers here...
