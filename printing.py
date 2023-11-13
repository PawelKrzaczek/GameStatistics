# Printing functions
import reports


def print_count_games(file_name):
    count = reports.count_games(file_name)
    print(f"The number of games is: {count}")


def main():
    file_name = input("Enter the name of the data file: ")
    print_count_games(file_name)


if __name__ == "__main__":
    main()
