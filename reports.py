def count_games(file_name):
    with open(file_name, 'r') as file:
        return len(file.readlines())


def decide(file_name, year):
    with open(file_name, 'r') as file:
        for line in file:
            if str(year) in line:
                return True
        return False


def get_latest(file_name):
    with open(file_name, 'r') as file:
        latest_game = ''
        latest_year = 0
        for line in file:
            game_info = line.strip().split('\t')
            if int(game_info[2]) > latest_year:
                latest_year = int(game_info[2])
                latest_game = game_info[0]
        return latest_game


def count_by_genre(file_name, genre):
    count = 0
    with open(file_name, 'r') as file:
        for line in file:
            game_info = line.strip().split('\t')
            if game_info[3] == genre:
                count += 1
        return count


def get_line_number_by_title(file_name, title):
    with open(file_name, 'r') as file:
        for i, line in enumerate(file, start=1):
            if title in line:
                return i
        raise ValueError(f"{title} not found in {file_name}")


def sort_abc(file_name):
    with open(file_name, 'r') as f:
        titles = f.readlines()
    titles = [title.strip() for title in titles]
    titles.sort()
    return titles


def get_genres(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    genres = set()
    for line in lines:
        genre = line.split(',')[2].strip()
        if genre:
            genres.add(genre)
    return sorted(list(genres))


def when_was_top_sold_fps(file_name):
    pass
