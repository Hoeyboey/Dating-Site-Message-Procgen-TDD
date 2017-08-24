from source_messages import source_messages
import nltk
import random

def select_base_tweet(source_messages):
	index_of_base_tweet = random.randint(0, len(source_messages)-1)
	base_tweet = source_messages[index_of_base_tweet]
	base_tweet = base_tweet.lower()
	return base_tweet

def check_length(tweet):
	return len(tweet) <= 140

def crop_tweet_to_under_140_characters(tweet):
	while len(tweet) > 140:
		tweet_list_of_words = tweet.split(" ")
		word_to_remove = random.randint(0, len(tweet_list_of_words)-1)
		tweet_list_of_words.remove(tweet_list_of_words[word_to_remove])
		tweet = tweet_list_of_words[0]
		for x in range(1, len(tweet_list_of_words)):
			tweet = tweet + " " + tweet_list_of_words[x]
	return tweet

def select_word_to_split_on(tweet, freq_words_in_tweet, blacklist):
	words_in_tweet = tweet.split(" ")
	unfinished = True
	blacklist_counter = 0
	tweet_split = tweet.split()
	for x in blacklist:
		if x in tweet_split:
			tweet_split.remove(x)
	if tweet_split == []:
		raise ValueError
	else:
		return random.choice(tweet_split)
	# while unfinished:
	# 	for x in words_in_tweet:
	# 		if x not in blacklist:
	# 			random_number_for_probability = random.random()
	# 			if freq_words_in_tweet[x]/freq_words_in_tweet["total_frequency_of_words_in_tweet"] > random_number_for_probability:
	# 				word_split_on = x
	# 				unfinished = False
	# 		else:
	# 			blacklist_counter = blacklist_counter + 1
	# 			if blacklist_counter == len(words_in_tweet):
					# raise ValueError
	return word_split_on


def create_freq_words_in_tweet(tweet, word_dictionary):
	words_in_tweet = tweet.split(" ")
	freq_words_in_tweet = {}
	total_freq = 0      
	for x in words_in_tweet:
		if freq_words_in_tweet.get(x) == None:
			freq_words_in_tweet[x] = word_dictionary[x]
			total_freq = total_freq + word_dictionary[x]
	freq_words_in_tweet["total_frequency_of_words_in_tweet"] = total_freq
	return freq_words_in_tweet

def create_source_messages_Text_object():
	source_messages_as_Text_object = nltk.text.Text(nltk.corpus.gutenberg.words('source_messages.txt'))
	return source_messages_as_Text_object

def find_similar_words(word_split_on, source_messages_as_Text_object):
	similar_words = source_messages_as_Text_object.similar(word_split_on).split()
	return similar_words

def find_tweets_including_word_split_on_and_similar(word_split_on_and_similar, source_messages):
	possible_messages = {}
	possible_messages_list = []
	for y in word_split_on_and_similar:
		possible_messages_list_for_comprehension = [x for x in source_messages if y in x.split() and x not in possible_messages_list]
		possible_messages_for_comprehension = {k:y for k in source_messages if y in k.split() and k not in possible_messages} # The value will always be the last matching word from word_split_on_and_similar
		possible_messages_list = possible_messages_list + possible_messages_list_for_comprehension
		possible_messages = {**possible_messages, **possible_messages_for_comprehension}
	return possible_messages, possible_messages_list

def choose_second_tweet(possible_messages_list, source_messages):
	if possible_messages_list == []:
		return random.choice(source_messages)
	else:
		return random.choice(possible_messages_list)

def split_chosen_second_tweet(chosen_second_tweet, possible_messages):
	#print(possible_messages)
	chosen_second_tweet_split = chosen_second_tweet.split(possible_messages[chosen_second_tweet])
	return chosen_second_tweet_split[1]

def split_base_tweet_on_word_split_on(tweet, word_split_on):
	tweet_split = tweet.split(word_split_on)
	return tweet_split[0] + word_split_on