import spacy

nlp = spacy.load("en_core_web_sm")

first = "The old man the boat."
second = "The horse raced past the fell."
third = "The complex houses married and single soldiers and their families."
fourth = "Until the police arrest the german drug dealers control the street."
fifth = "On the sunny spring evening of 7 May 2020, in the lethal first wave of the Covid pandemic, " \
        "the Conservative peer Michelle Mone and her husband, " \
        "Douglas Barrowman, had themselves filmed for Instagram. Standing between the stone pillars at the front door of their " \
        "mansion on the Isle of Man, they clapped for NHS staff, carers and other key workers, as they did weekly from different " \
        "parts of their Ballakew estate."


first_doc = nlp(first)
second_doc = nlp(second)
third_doc = nlp(third)
fourth_doc = nlp(fourth)
fifth_doc = nlp(fifth)

gardenpathSentences = [first_doc, second_doc, third_doc, fourth_doc, fifth_doc]

for sentance in gardenpathSentences:
    print([token.orth_ for token in sentance])
    print([(i, i.label_, i.label) for i in sentance.ents])

#Spacy didn't really seem to recognise any entaties until the last sentence.
#(the sunny spring, 'DATE', 391)
#(Covid, 'PERSON', 380)


