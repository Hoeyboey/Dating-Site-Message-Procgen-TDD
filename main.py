from tweetGeneration import *
from init import init
from source_messages import source_messages
import tweepy
import sys


number_of_runthroughs = 3
blacklist = ["x", "total_frequency_of_words_in_tweet"]
word_dictionary = init(source_messages)
tweet = select_base_tweet(source_messages)
source_messages_as_Text_object = create_source_messages_Text_object()
for runthrough_number in range(0, number_of_runthroughs):
	freq_words_in_tweet = create_freq_words_in_tweet(tweet, word_dictionary)
	word_split_on = select_word_to_split_on(tweet, freq_words_in_tweet, blacklist)
	tweet_split = split_base_tweet_on_word_split_on(tweet, word_split_on)
	word_split_on_and_similar = find_similar_words(word_split_on, source_messages_as_Text_object)
	possible_messages, possible_messages_list = find_tweets_including_word_split_on_and_similar(word_split_on_and_similar, source_messages)
	while possible_messages_list == []:
		word_split_on = select_word_to_split_on(tweet, freq_words_in_tweet, blacklist)
		tweet_split = split_base_tweet_on_word_split_on(tweet, word_split_on)
		word_split_on_and_similar = find_similar_words(word_split_on, source_messages_as_Text_object)
		possible_messages, possible_messages_list = find_tweets_including_word_split_on_and_similar(word_split_on_and_similar, source_messages)
	chosen_second_tweet = choose_second_tweet(possible_messages_list, source_messages)
	chosen_second_tweet_split = split_chosen_second_tweet(chosen_second_tweet, possible_messages)
	tweet = tweet_split + chosen_second_tweet_split
	tweet = tweet.lower()

print(tweet)
auth = tweepy.OAuthHandler(sys.argv[1], sys.argv[2])
auth.set_access_token(sys.argv[3], sys.argv[4])

api = tweepy.API(auth)

api.update_status(tweet)