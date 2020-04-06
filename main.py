from src.scrape import search_jisho, get_user_input, SUCCESS, FAILURE

def main():
    while True:
        result = search_jisho(get_user_input())
        if result == FAILURE:
            break 
    return 0

if __name__ == "__main__":
    main()