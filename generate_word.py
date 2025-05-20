import spacy


nlp = spacy.load("en_core_web_md")
print("Model loaded:", nlp.meta["name"])

# Build set of common words based on frequency and type
common_words = set()

for lex in nlp.vocab:
    if lex.is_alpha and lex.is_lower and lex.prob >= -15.0:
        common_words.add(lex.text)

# Test results
print("injury" in common_words)  # Should be True
print("xqztr" in common_words)   # Should be False
print("Total common words:", len(common_words))  # Should be > 0



# all_words = set(nlp.vocab.strings)

# def is_valid_word(word):
#     return word.isalpha() and len(word) > 3 and word.islower()

# # def is_common(word):
# #     lex = nlp.vocab[word]
# #     return lex.is_alpha and lex.prob >= -15.0 and lex.is_lower

# def is_common(word):
#     lex = nlp.vocab[word]
#     return lex.is_alpha and lex.is_lower and lex.prob >= -15.0

# common_words = set(word for word in nlp.vocab.strings if is_common(word))

# valid_words = set(word for word in nlp.vocab.strings if is_valid_word(word))
# # common_words = set(word for word in nlp.vocab.strings if is_common(word))

# print(len(valid_words))
# print(len(common_words))



# print("injury" in common_words)  
# print("xqztr" in common_words)   


