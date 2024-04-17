from  lemmy.main  import lemmatize_corpus, count_verbs_string, count_verbs
import pytest




def test_lemmatize_corpus():
    test_input = "That is why I believe that we need to help.Tajikistan on its difficult way ahead"
    expected = ["believe", "need", "help"]
    assert lemmatize_corpus(test_input) == expected





def test_count_verbs_string():
    test_input = ["believe", "need", "help", "help", "help", "need"]
    expected_output = "3 help\n2 need\n1 believe" 
    assert count_verbs_string(test_input) == expected_output



def test_count_verbs_string_2():
    test_input = ["run", "twice", "once", "run", "run", "run"]
    expected_output = "4 run\n1 twice\n1 once" 
    assert count_verbs_string(test_input) == expected_output




def test_count_verbs():
    test_input = ["run", "go", "go", "study", "run", "play", "play", "go", "go", "run"]
    expected_output = {"go": 4, "run": 3, "play": 2, "study": 1}
    assert count_verbs(test_input) == expected_output