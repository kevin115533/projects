replacements = {"I":"you", "me":"you", "my":"your",
		"we":"you", "us":"you", "mine":"yours"}
def changePerson(sentence):
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)
