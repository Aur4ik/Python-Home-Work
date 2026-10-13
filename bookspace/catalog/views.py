import requests
from django.shortcuts import render

API_URL = "https://openlibrary.org/search.json"


def index(request):
    query = request.GET.get("q", "tolkien").strip()[:100] or "tolkien"
    books = []
    error = ""
    try:
        response = requests.get(API_URL, params={"q": query, "limit": 12,
            "fields": "key,title,author_name,first_publish_year,edition_count"},
            headers={"User-Agent": "BookspaceHomework/1.0"}, timeout=10)
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict) or not isinstance(data.get("docs"), list):
            raise ValueError("Неверный формат ответа API")
        for item in data["docs"]:
            if not isinstance(item, dict):
                raise ValueError("Неверный формат книги")
            books.append({"title": item.get("title") or "Без названия",
                          "authors": ", ".join(item.get("author_name") or []) or "Автор не указан",
                          "year": item.get("first_publish_year"),
                          "editions": item.get("edition_count", 0)})
    except (requests.RequestException, ValueError, TypeError):
        books = []
        error = "Не удалось загрузить книги. Попробуйте повторить запрос позже."
    return render(request, "catalog/index.html", {"books": books, "query": query, "error": error})
