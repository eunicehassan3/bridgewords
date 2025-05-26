import random
import requests

with open("words/Collins Scrabble Words (2019).txt") as f:
    VALID_WORDS = set(word.strip().lower() for word in f if word.strip())

with open("words/common_words.txt") as f:
    COMMON_WORDS = [word.strip().lower() for word in f if word.strip()]

def get_random_word_pair():
    start = random.choice(COMMON_WORDS)
    target = random.choice(COMMON_WORDS)
    while target == start:
        target = random.choice(COMMON_WORDS)
    return start, target

def is_valid_word(word):
    return word in VALID_WORDS

def get_related_words(word):
    rt_url = f"https://api.datamuse.com/words?rel_trg={word}&max=500"
    ml_url = f"https://api.datamuse.com/words?ml={word}&max=500"
    
    rt_response = requests.get(rt_url)
    ml_response = requests.get(ml_url)

    if rt_response.status_code != 200 or ml_response.status_code != 200:
        print("Error fetching data from Datamuse.")
        return []

    # Parse JSON responses
    rel_trg_words = [entry["word"] for entry in rt_response.json()]
    ml_words = [entry["word"] for entry in ml_response.json()]

    # Combine and deduplicate
    combined = list(set(rel_trg_words + ml_words))
    return combined

def is_related(word1, word2):
    return word2 in get_related_words(word1)

def is_in_datamuse(word):
    resp = requests.get(f"")
def play_game():
    found_target = False
    start_word, target_word = get_random_word_pair()
    current_word = start_word
    word_arr = "" + start_word
    # word_arr = [start_word]
    print("BRIDGEWORDS")
    print("\n")
    print("\n")

    print("Start Word: " + start_word)
    print("Target Word: " + target_word)
    print("\nTry to build a bridge of related words from start to target!\n")

    while not found_target:
       guess = ""
       guess = input(f"Current Word: {current_word}\nEnter your next word: ").strip().lower()
    #    guess = input("Enter a word \n")

       if not is_valid_word(guess):
            print("Not a real word. Try again")
            continue
       
       if not is_related(current_word, guess):
           print("Not close enough in relation. Try again\n")
           continue
       
       print("✅ Good bridge!\n")
       current_word = guess
       word_arr += (" --> " + current_word)

       print(word_arr)
       
       if current_word == target_word:
            found_target = True
            print("🎉 You reached the target word! Well done!")
           
           
         

play_game()
# print(get_related_words("bird"))
# print(is_related("bird", "feathers"))
# print(is_related("bird", "jolhuo"))

# print(is_valid_word("jkdaslfj;"))
# print(is_valid_word("cheese"))