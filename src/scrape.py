import sys, re
import bs4, requests

SUCCESS = 1
FAILURE = 0

def get_user_input(flag):
    """
    Returns a string containing user provided movie/tv title

    Parameters
    ----------
    flag : int
        flag is set to changed to 1 if we are searching again.
        Otherwise the flag is 0.

    Returns
    -------
    str
        User input

    """
    if (len(sys.argv) > 1) and (flag == 0):
        return " ".join(sys.argv[1:])
    else:
        return input("Enter the japanese word you would like to look for: ")

def get_soup(link):
    """
    Gets the HTML for a link. Throws error if it does not connect to website.

    Parameters
    ----------
    link : str
        URL to the webpage

    Returns
    -------
    str
        HTML of the link

    """
    page = requests.get(link)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    return soup

def search_jisho(word):
    """
    Searches the word on the jisho website and returns the link

    Parameters
    ----------
    word : str
        Word one wants to look up

    Returns
    -------
    int 
        SUCCESS if results found or FAILURE otherwise
    """
    if word == "":
        print("\nWord not provided. Exiting...")
        return FAILURE
    
    link = "https://jisho.org/search/{}"
    search_soup = get_soup(link.format(word))
    search_results = search_soup.findAll('span', class_='result_count')
    
    if search_results:
        print("\nWords" + search_results[0].text)
        # Words and definitions
        words_dict = words(search_soup)
        for key in words_dict:
            for item in words_dict[key]:
                print(item)
        # Kanji with onyomi and kunyomi
        print("\nKanji" + search_results[1].text)
        kanji_dict = kanji(search_soup)
        for key in kanji_dict:
            for item in kanji_dict[key]:
                print(item[1])
        return SUCCESS
    else:
        return FAILURE


def words(soup):
    """
    Takes the soup and gets all of the words and their informaiton.

    Parameters
    ----------
    soup : str
        The HTML from a webpage.
    
    Returns
    -------
    words : dict
        Dictionary of each word and the words information.
    """
    words = dict()
    result_num = 1
    
    for result in soup.findAll('div', class_='concept_light clearfix'):
        words[str(result_num)] = []
        for text in result.findAll('span', class_='text'):
            words[str(result_num)].append("(" + str(result_num) + "). " + text.text.strip())
            #print(text.text.strip())
        for meaning in result.findAll('span', class_='meaning-meaning'):
            words[str(result_num)].append(" - " + meaning.text.strip())
            #print(meaning.text.strip())
        result_num += 1
    
    return words

def kanji(soup):
    """
    Takes the soup and gets all of the words and their informaiton.

    Parameters
    ----------
    soup : str
        The HTML from a webpage.
    
    Returns
    -------
    words : dict
        Dictionary of each word and the words information.
    """
    kanji = dict()
    result_num = 1

    for result in soup.findAll('div', class_='kanji_light_content'):
        kanji[str(result_num)] = []
        for kan in result.findAll('span', class_='character literal japanese_gothic'):
            kanji[str(result_num)].append(("kanji", "(" + str(result_num) + "). " + kan.text.strip()))
            #print(kan.text.strip())
        for english in result.findAll('div', class_='meanings english sense'):
            kanji[str(result_num)].append(("english", "English: " + english.text.strip().replace('\n', '')))
            #print(english.text.strip().replace('\n', ''))
        for kun in result.findAll('div', class_='kun readings'):
            kanji[str(result_num)].append(("kun", kun.text.strip().replace('\n', '')))
            #print(kun.text.strikan.text.strip()p().replace('\n', ''))
        for on in result.findAll('div', class_='on readings'):
            kanji[str(result_num)].append(("on", on.text.strip().replace('\n', '')))
            #print(on.text.strip().replace('\n', ''))
        result_num += 1
    
    return kanji

def search_again():
    """
    Asks if user wants to search again.

    Parameters
    ----------
    None
    
    Returns
    -------
    SUCCESS | FAILURE : int
        SUCCESS if one does want to search again or
        FAILURE if one does not want to search again.
    """
    answer = input("\nWould you like to search another word (Y/N)? ")
    answer = answer.lower()
    if (answer == 'y'):
        answer = get_user_input(1)
        search_jisho(answer)
        return SUCCESS
    else:
        print("Exiting...")
        return FAILURE