from .recipe_scraper_service import RecipeScraperService


@router.route("/recipe")
def scrape_recipe_handler(payload):
    url = payload.get("url")
    if not url:
        return {"status": "error", "message": "No URL provided in payload."}, 400

    try:
        # Use the RecipeScraperService to get recipe details
        scraper_service = RecipeScraperService(url)
        recipe_details = scraper_service.get_recipe_json()
        return {"status": "success", "data": recipe_details}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

@router.route("/health-check")
def health_check_handler(payload):
    return {"status": "success", "message": "Health check passed!"}, 200

# You can define more routes and handlers here...
