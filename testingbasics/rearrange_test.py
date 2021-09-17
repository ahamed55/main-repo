import rearrange
import unittest

class test(unittest.TestCase):
    def test_arrange(self):
        testcase = "ahamed ibrahim"
        expected = "ibrahim ahamed"
        self.assertEqual(rearrange.rearrange_name(testcase),expected)

    def test_emptystr(self):
        TestCase = ""
        expected = ""
        self.assertEqual(rearrange.rearrange_name(TestCase),expected)
    
    def test_double_word(self):
        testcase = "ahamed, ibrahim.A"
        expected = "ibrahim.A ahamed"
        self.assertEqual(rearrange.rearrange_name(testcase),expected)

    def test_erroe(self):
        self.assertRaises(ValueError,rearrange.rearrange_name,1)
         
unittest.main()