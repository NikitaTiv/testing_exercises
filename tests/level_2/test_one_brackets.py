from functions.level_2.one_brackets import delete_remove_brackets_quotes

def test__delete_remove_brackets_quotes__processing_string_without_quotes():
    assert delete_remove_brackets_quotes('string') == 'string'


def test__delete_remove_brackets_quotes__processing_string_with_quotes():
    assert delete_remove_brackets_quotes("{'string'}") == 'string'
