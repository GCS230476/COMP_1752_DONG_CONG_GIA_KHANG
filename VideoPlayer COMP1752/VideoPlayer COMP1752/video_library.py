from library_item import LibraryItem

library = {}
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2)
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1)
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3)

next_key = 6

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None

def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return

def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return

def add_video(name, director, rating=0):
    global next_key
    key = f"{next_key:02}"
    library[key] = LibraryItem(name, director, rating)
    next_key += 1

def update_video(key, name=None, director=None, rating=None):
    if key in library:
        if name is not None:
            library[key].name = name
        if director is not None:
            library[key].director = director
        if rating is not None:
            if 0 <= rating <= 5:
                library[key].rating = rating
            else:
                raise ValueError("Rating must be between 0 and 5")
    else:
        raise KeyError(f"No video found with key {key}")

def filter_by_director(director_name):
    filtered = {}
    for key, item in library.items():
        if item.director.lower() == director_name.lower():
            filtered[key] = item
    return "\n".join([f"{key}: {item.name} by {item.director} (Rating: {item.rating}, Plays: {item.play_count})"
                      for key, item in filtered.items()])

def search_by_name(search_term):
    results = []
    for key, item in library.items():
        if search_term.lower() in item.name.lower() or search_term.lower() in item.director.lower():
            results.append(f"{key}: {item.name} by {item.director} (Rating: {item.rating}, Plays: {item.play_count})")
    return "\n".join(results)

def search_by_rating(min_rating, max_rating):
    results = []
    for key, item in library.items():
        if min_rating <= item.rating <= max_rating:
            results.append(f"{key}: {item.name} by {item.director} (Rating: {item.rating}, Plays: {item.play_count})")
    return "\n".join(results)
