import rearrange
import unittest

class test(unittest.TestCase):
    def test_arrange(self):
        testcase = "ahamed ibrahim"
        expected = "ibrahim ahame d"
        self.assertEqual(rearrange.rearrange_name(testcase),expected)
        
unittest.main()