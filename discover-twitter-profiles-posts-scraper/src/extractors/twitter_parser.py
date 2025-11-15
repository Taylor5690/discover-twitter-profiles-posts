import logging
from datetime import datetime
from .utils_time import utc_timestamp

class TwitterProfileScraper:
    """
    Simulated scraper that generates deterministic structured data.
    """

    def __init__(self, profile_url: str):
        self.profile_url = profile_url

    def scrape(self):
        logging.info(f"Simulating scrape for profile: {self.profile_url}")

        # Fake result mimicking expected structure
        data = [
            {
                "id": "1000000000000000001",
                "user_posted": "sampleuser",
                "name": "Sample User",
                "description": "Sample post for demonstration.",
                "date_posted": "2025-01-01T10:00:00.000Z",
                "photos": [],
                "url": f"{self.profile_url}/status/1000000000000000001",
                "quoted_post": {},
                "tagged_users": None,
                "replies": 10,
                "reposts": 5,
                "likes": 50,
                "views": 200,
                "external_url": None,
                "hashtags": ["#sample"],
                "followers": 12345,
                "biography": "Automation demo user.",
                "posts_count": 500,
                "profile_image_link": "https://example.com/profile.jpg",
                "following": 100,
                "is_verified": False,
                "quotes": 2,
                "bookmarks": 4,
                "parent_post_details": {},
                "external_image_urls": [],
                "videos": [],
                "external_video_urls": [],
                "timestamp": utc_timestamp(),
                "input": {"url": f"{self.profile_url}/status/1000000000000000001"},
                "discovery_input": {"url": self.profile_url, "start_date": "", "end_date": ""},
            }
        ]

        return data