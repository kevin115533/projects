replacements = {"I":"you", "me":"you", "my":"your",
		"we":"you", "us":"you", "mine":"yours"}
def changePerson(sentence):
    words = sentence.split()
    replyWords = []
    for words in words:
        reply.Words.append(replacements.get(words, word))
    return " ".join(replywords)
