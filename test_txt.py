import unittest
from text_file import text_list


class Testtext_file(unittest.TestCase):
    def test_file(self):
        self.assertEqual(
            ['Sed tamen est aliquid',' quod nobis non liceat', ' liceat illis. Virtutis', ' magnitudinis animi', ' patientiae'],
            text_list('sample2.txt'))
