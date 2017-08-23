import unittest
import nltk
from tweetGeneration import *

class TestTweetGenerationFunctions(unittest.TestCase):

	def test_given_source_messages_select_base_tweet(self):
		source_messages = ["Testing source_messages"]
		expected_output = "testing source_messages"
		actual = select_base_tweet(source_messages)
		self.assertEqual(actual, expected_output)

	def test_given_tweet_check_length_under_141_characters(self):
		tweet = "Testing under 140 characters"
		expected_output = True
		actual = check_length(tweet)
		self.assertEqual(actual, expected_output)

	def test_given_tweet_check_length_over_140_characters(self):
		tweet = "Testing over 140 charactersTesting over 140 charactersTesting over 140 charactersTesting over 140 charactersTesting over 140 charactersTesting over 140 characters"
		expected_output = False
		actual = check_length(tweet)
		self.assertEqual(actual, expected_output)

	def test_given_tweet_over_140_characters_successfully_trimmed(self):
		tweet = "Testing over 140 charactersTesting over 140 charactersTesting over 140 charactersTesting over 140 charactersTesting over 140 charactersTesting over 140 characters"
		cropped_tweet = crop_tweet_to_under_140_characters(tweet)
		expected_output = True
		actual = len(cropped_tweet) <= 140
		self.assertEqual(actual, expected_output)

	def test_given_tweet_select_word_to_split_on(self):
		tweet = "testing not_testing"
		blacklist = []
		freq_words_in_tweet = {"testing": 3, "not_testing":0, "total_frequency_of_words_in_tweet":3}
		expected_output = "testing"
		actual = select_word_to_split_on(tweet, freq_words_in_tweet, blacklist)
		self.assertEqual(actual, expected_output)

	def test_given_tweet_and_all_words_blacklisted(self):
		tweet = "testing"
		blacklist = ["testing"]
		freq_words_in_tweet = {"testing": 3, "not_testing":0, "total_frequency_of_words_in_tweet":3}
		with self.assertRaises(ValueError):
			actual = select_word_to_split_on(tweet, freq_words_in_tweet, blacklist)

	def test_given_tweet_create_freq_words_in_tweet(self):
		tweet = "testing one two three"
		word_dictionary = {"testing":3, "one":1, "two":2, "three":3, "four":4}
		expected_output = {"testing":3, "one":1, "two":2, "three":3, "total_frequency_of_words_in_tweet":9}
		actual = create_freq_words_in_tweet(tweet, word_dictionary)
		self.assertEqual(actual, expected_output)

	def test_given_word_split_on_and_Text_object_find_similar_words(self):
		word_split_on = "I"
		test_source_messages_as_Text_object = nltk.text.Text(nltk.corpus.gutenberg.words("melville-moby_dick.txt"))
		expected_output = ['he','you','it','they','we','that','not','there','ye','to','and','then','ahab','this','she','queequeg','what','stubb','all','would']
		actual = test_source_messages_as_Text_object.similar(word_split_on).split()
		self.assertEqual(actual, expected_output)

	def test_given_word_split_on_and_similar_find_messages_with_word_split_on_and_similar_as_list(self):
		word_split_on_and_similar = ["hello", "there"]
		source_messages = ["hello", "this is the first test", "this is the second test hello there", "there"]
		expected_output = ["hello", "this is the second test hello there", "there"]
		not_used, actual = find_tweets_including_word_split_on_and_similar(word_split_on_and_similar, source_messages)
		self.assertEqual(actual, expected_output)

	def test_given_word_split_on_and_similar_find_messages_with_word_split_on_and_similar_as_dictionary(self):
		word_split_on_and_similar = ["hello", "there"]
		source_messages = ["hello there", "there is a message", "testing"]
		expected_output = {"hello there":"hello", "there is a message":"there"}
		actual, not_used = find_tweets_including_word_split_on_and_similar(word_split_on_and_similar, source_messages)
		self.assertEqual(actual, expected_output)

	def test_given_chosen_second_tweet_successfully_split_tweet_correct(self):
		chosen_second_tweet = "hello there this is a test"
		possible_messages = {"hello there this is a test":"this"}
		expected_output = " is a test"
		actual = split_chosen_second_tweet(chosen_second_tweet, possible_messages)
		self.assertEqual(actual, expected_output)

	def test_given_tweet_split_on_word_split_on(self):
		tweet = "testing one two three"
		word_split_on = "one"
		expected_output = "testing one"
		actual = split_base_tweet_on_word_split_on(tweet, word_split_on)
		self.assertEqual(actual, expected_output)

if __name__ == '__main__':
    unittest.main()
