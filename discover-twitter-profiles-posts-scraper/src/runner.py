import json
import logging
from pathlib import Path

from extractors.twitter_parser import TwitterProfileScraper
from outputs.exporters import export_to_json

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def load_settings():
    config_path = Path(__file__).resolve().parent / "config" / "settings.example.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    settings = load_settings()
    profile_url = settings.get("profile_url")

    if not profile_url:
        raise ValueError("profile_url missing in settings.example.json")

    logging.info(f"Starting scrape for: {profile_url}")

    scraper = TwitterProfileScraper(profile_url)
    results = scraper.scrape()

    output_path = Path.cwd() / "output.json"
    export_to_json(results, output_path)

    logging.info(f"Scraping complete. Output written to {output_path}")

if __name__ == "__main__":
    main()