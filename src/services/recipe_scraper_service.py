from typing import Dict, Optional

import requests
from recipe_scrapers import __version__, scrape_html

# Setting the headers to include the current version of recipe-scrapers
HEADERS = {
    "User-Agent": f"Mozilla/5.0 (compatible; Windows NT 10.0; Win64; x64; rv:{__version__}) recipe-scrapers/{__version__}"
}

class RecipeScraperService:
    def __init__(self, url: str, html: Optional[str] = None, online: bool = False, supported_only: Optional[bool] = None):
        self.url = url
        self.html = html
        self.online = online
        self.supported_only = supported_only
        self.scraper = self._initialize_scraper()

    def _initialize_scraper(self):
        # Attempt to use scrape_html with provided or fetched HTML
        try:
            if not self.html and self.online:
                self.html = self._fetch_html_content()  # Fetch HTML if online is True and no HTML is provided

            # Initialize the scraper with scrape_html
            return scrape_html(
                html=self.html,
                org_url=self.url,
                online=self.online,
                supported_only=self.supported_only
            )
        except Exception as e:
            raise ValueError(f"Could not scrape the provided URL: {e}")

    def _fetch_html_content(self) -> Optional[str]:
        """Fetches HTML content from the URL if required."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch HTML content: {e}")
            return None

    def get_recipe_json(self) -> Dict:
        """Uses to_json method of scraper to return recipe data as JSON."""
        try:
            return self.scraper.to_json()
        except Exception as e:
            print(f"Error retrieving recipe data: {e}")
            return {}


# Example usage
# url = "https://thespiceadventuress.com/2015/12/10/gosht-durbari/"
# # url = "https://www.ah.nl/allerhande/recept/R-R1200481/regenbooglasagne"
# # url = "https://www.leukerecepten.nl/aanrader-gevulde-pastaschelpen-met-gorgonzola-dop-in-spinaziesaus/"
# scraper_service = RecipeScraperService(url, online=True, supported_only=False)
# recipe_details = scraper_service.get_recipe_json()
# print(recipe_details)