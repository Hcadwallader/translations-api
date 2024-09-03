from utilities import split_list, clean_word, clean_words

class TestUtilities():

    def test_split_list_into_chunks(self):
        my_list = [1,2,3,4,5,6,7,8,9]
        result = split_list(my_list, 2)
        assert result == [[1, 2], [3, 4], [5, 6], [7, 8], [9]]

    def test_split_list_empty_list(self):
        my_list = []
        result = split_list(my_list, 2)
        assert result == []

    def test_split_list_chunks_bigger_than_list(self):
        my_list = [1,2,3]
        result = split_list(my_list, 5)
        assert result == [[1, 2, 3]]


    def test_clean_word_nothing_dirty(self):
        original = "anagram"
        result = clean_word(original)
        assert result == original

    def test_clean_word_single_number(self):
        original = "anagram7"
        result = clean_word(original)
        assert result == "anagram"

    def test_clean_word_single_symbol(self):
        original = "anagram!"
        result = clean_word(original)
        assert result == "anagram"

    def test_clean_word_nothing_but_symbols(self):
        original = "!$@&@£@!!"
        result = clean_word(original)
        assert result == ""

    def test_clean_word_empty_word(self):
        original = ""
        result = clean_word(original)
        assert result == ""


    def test_clean_words(self):
        original = ["", "hello", "world!", "special999", "1tes2ter3", "c@t"]
        result = clean_words(original)
        assert result == ["", "hello", "world", "special", "tester", "ct"]