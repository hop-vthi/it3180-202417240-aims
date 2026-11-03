def search_by_category(dvds, category):
    """Return DVDs whose categories contain the query, ignoring case."""
    query = category.strip().casefold()
    if not query:
        return []
    return [dvd for dvd in dvds if query in (dvd.category or "").casefold()]

def search_by_title(dvds, title):
    """Return DVDs whose titles contain the query, ignoring case."""
    query = title.strip().casefold()
    if not query:
        return []
    return [dvd for dvd in dvds if query in dvd.title.casefold()]



