import json

# with open('trend.json','r') as fp:
# 	line = fp.readline()
# 	tweet = json.loads(line)
	# print json.dumps(tweet,indent=4)

from nltk.tokenize import word_tokenize

tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print word_tokenize(tweet)