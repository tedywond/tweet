from sklearn.feature_extraction.text import TfidfVectorizer
train_data = []
from collections import Counter
def enumerate_folder(fldr):
	import os
	return os.listdir(fldr)


def read_doc(doc_path):
	try:
		with open(doc_path,'r') as fp:
			content = fp.read()
			return content
	except:
		pass

def __test__():
	test_content = read_doc('uncle sam.txt')
	response = vectorizer.transform([test_content])

	tfidf_counter = Counter()

	for col in response.nonzero()[1]:
		tfidf_counter[feature_name[col]] = response[0,col]

	print tfidf_counter.most_common(10)





doc_list = enumerate_folder('samsung')
for doc in doc_list:
	content = read_doc('samsung/'+ doc)
	train_data.append(content)


# vectorizer = TfidfVectorizer(min_df=5,max_df=0.8, sublinear_tf=True, use_idf=True,stop_words='english')
# vectorizer.fit_transform(train_data)

# feature_name = vectorizer.get_feature_names()
# feature_idf = vectorizer.idf_

# samsung_idf = Counter()
# compiled_features = zip(feature_name,feature_idf)

# for feature in compiled_features:
# 	samsung_idf[feature[0]] = feature[1]

# for word,count in samsung_idf.most_common():
# 	print word,'\t',count

# __test__()



