import requests


class POISearch:
    def __init__(self, amap_key: str = "", baidu_key: str = ""):
        self.amap_key = amap_key
        self.baidu_key = baidu_key

    def search_amap(self, keyword: str, city: str = "", radius: int = 2000, page_size: int = 10):
        if not self.amap_key:
            raise ValueError("AMAP_KEY is missing")

        url = "https://restapi.amap.com/v3/place/text"
        params = {
            "key": self.amap_key,
            "keywords": keyword,
            "city": city,
            "citylimit": "true",
            "offset": page_size,
            "page": 1,
            "extensions": "all",
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        pois = data.get("pois", [])
        result = []
        for poi in pois:
            result.append(
                {
                    "name": poi.get("name"),
                    "address": poi.get("address"),
                    "location": poi.get("location"),
                    "tel": poi.get("tel"),
                    "type": poi.get("type"),
                }
            )
        return result

    def search_nearby_pois(self, keyword: str, city: str, radius: int = 2000):
        return self.search_amap(keyword=keyword, city=city, radius=radius)
