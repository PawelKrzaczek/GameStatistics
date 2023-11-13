
def load_data(file_name):
    with open(file_name, 'r') as file:
        return [line.strip().split('\t') for line in file]


def count_games(file_name):
    lines = load_data(file_name)
    return len(lines)


def decide(file_name, year):
    lines = load_data(file_name)
    for line in lines:
        if str(year) in line:
            return True
    return False


def get_latest(file_name):
    lines = load_data(file_name)
    latest_game = ""
    latest_year = 0
    for line in lines:
        if int(line[2]) > latest_year:
            latest_year, latest_game = int(line[2]), line[0]
    return latest_game


def count_by_genre(file_name, genre):
    lines = load_data(file_name)
    count = 0
    for line in lines:
        if line[3] == genre:
            count += 1
    return count


def get_line_number_by_title(file_name, title):
    lines = load_data(file_name)
    for i, line in enumerate(lines, 1):
        if title in line:
            return i
    raise ValueError(f"{title} found not in {file_name}")


def sort_abc(file_name):
    lines = load_data(file_name)
    titles = [line[0] for line in lines]
    titles.sort()
    return titles


def get_genres(file_name):
    lines = load_data(file_name)
    genres = set(line[3] for line in lines)
    return sorted(list(genres))


def when_was_top_sold_fps(file_name):
    lines = load_data(file_name)
    fps_games = [line for line in lines if line[3] == "First-person shooter"]
    if not fps_games:
        raise ValueError("FPS genre is not found in the given data file")
    top_game = max(fps_games, key=lambda x: float(x[1]))
    return int(top_game[2])
