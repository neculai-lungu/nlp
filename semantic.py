import spacy

nlp = spacy.load('en_core_web_md')

w1 = nlp("cat")
w2 = nlp("monkey")
w3 = nlp("banana")
w4 = nlp("baboon")

print(w1.similarity(w2))
print(w2.similarity(w3))
print(w3.similarity(w1))
print(w2.similarity(w4))


tokens = nlp("cat monkey banana hamster dog wolf")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["I am walking the dog", "Daniel bought a fast car", "I\ 've lost my car in my car",
             "I\ 'd like my boat back"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence, "+", similarity)

#Spacy will find similarities between words that have connections, although it is not always accurate
#Using the "en_core_web_sm" language model, you get a warning, informing that the model has no word vectors loaded and might not give yhe best result