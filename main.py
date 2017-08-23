from tweetGeneration import *
from init import init
from source_messages import source_messages

blacklist = ["x", "total_frequency_of_words_in_tweet"]
word_dictionary = init(source_messages)
tweet = select_base_tweet(source_messages)
freq_words_in_tweet = create_freq_words_in_tweet(tweet, word_dictionary)
word_split_on = select_word_to_split_on(tweet, freq_words_in_tweet, blacklist)
source_messages_as_Text_object = create_source_messages_Text_object()
word_split_on_and_similar = find_similar_words(word_split_on, source_messages_as_Text_object)
find_tweets_including_word_split_on_and_similar(word_split_on_and_similar, source_messages)
# print(word_split_on_and_similar)