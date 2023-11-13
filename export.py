# Export functions
import sys
import reports


def export_count_games(file_name, target):
    count = reports.count_games(file_name)
    with open(target, 'w') as file:
        file.write(f"Jest {count} gier")


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python3 export.py source_file_name target_file_name input_year input_genre input_title")
        sys.exit(1)

    source_file_name = sys.argv[1]
    target_file_name = sys.argv[2]
    input_year = int(sys.argv[3])
    input_genre = sys.argv[4]
    input_title = sys.argv[5]

    # export_results(source_file_name, target_file_name, input_year, input_genre, input_title)
    export_count_games(source_file_name, target_file_name)

