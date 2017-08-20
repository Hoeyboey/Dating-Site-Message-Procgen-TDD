from tweetGeneration import *
from init import init
from source_messages import source_messages

blacklist = ["x", "total_frequency_of_words_in_tweet"]
word_dictionary = init(source_messages)
tweet = select_base_tweet(source_messages)
freq_words_in_tweet = create_freq_words_in_tweet(tweet, word_dictionary)
word_split_on = select_word_to_split_on(tweet, freq_words_in_tweet, blacklist)
source_messages_as_Text_object = create_source_messages_Text_object()