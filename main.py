from src.scrape import search_jisho, get_user_input, SUCCESS, FAILURE, search_again

def main():
    result = search_jisho(get_user_input(0))
    while (result == SUCCESS):
        result = search_again()

if __name__ == "__main__":
    main()