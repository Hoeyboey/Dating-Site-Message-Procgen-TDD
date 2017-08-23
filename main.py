from tweetGeneration import *
from init import init
from source_messages import source_messages

number_of_runthroughs = 3
blacklist = ["x", "total_frequency_of_words_in_tweet"]
word_dictionary = init(source_messages)
tweet = select_base_tweet(source_messages)
print(tweet)
for runthrough_number in range(0, number_of_runthroughs):
	freq_words_in_tweet = create_freq_words_in_tweet(tweet, word_dictionary)
	word_split_on = select_word_to_split_on(tweet, freq_words_in_tweet, blacklist)
	tweet_split = split_base_tweet_on_word_split_on(tweet, word_split_on)
	source_messages_as_Text_object = create_source_messages_Text_object()
	word_split_on_and_similar = find_similar_words(word_split_on, source_messages_as_Text_object)
	possible_messages, possible_messages_list = find_tweets_including_word_split_on_and_similar(word_split_on_and_similar, source_messages)
	chosen_second_tweet = choose_second_tweet(possible_messages_list)
	print(chosen_second_tweet)
	chosen_second_tweet_split = split_chosen_second_tweet(chosen_second_tweet, possible_messages)
	tweet = tweet_split + chosen_second_tweet_split
print(tweet)