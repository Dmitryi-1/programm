import unittest

from mod2.task3.decrypt import decrypt_efficient


class TestDecrypt(unittest.TestCase):
    def setUp(self):
        self.decrypt = decrypt_efficient

    def test_no_removal_for_no_dots(self):
        self.assertEqual(decrypt_efficient('абра-кадабра'), 'абра-кадабра')

    def test_ignore_single_dot(self):
        self.assertEqual(decrypt_efficient('абра.-кадабра'), 'абра-кадабра')

    def test_remove_character_for_double_dots(self):
        self.assertEqual(decrypt_efficient('абра..-кадабра'), 'абр-кадабра')

    def test_remove_characters_for_several_dots(self):
        self.assertEqual(decrypt_efficient('абра...--..кадабра.....'), 'абр-кадаб')

    def test_return_empty_string_for_single_dot(self):
        self.assertEqual(decrypt_efficient('.'), '')

    def test_return_empty_string_for_many_dots(self):
        self.assertEqual(decrypt_efficient('1...2......3..4.........'), '')

    def test_return_empty_string_for_empty_string(self):
        self.assertEqual(decrypt_efficient(''), '')
