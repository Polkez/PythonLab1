import unittest
import correctme

class correctme_tests(unittest.TestCase):
   def test_sumValues0(self):
      self.assertEqual(correctme.sumValues(2,4), 6)
   def test_sumValues1(self):
      self.assertEqual(correctme.sumValues(2,10), 12)
   def test_sumValues2(self):
      self.assertEqual(correctme.sumValues(24,16), 40)

   def test_divdeValues0(self):
      self.assertEqual(correctme.divdeValues(4,2), 2)
   def test_divdeValues1(self):
      self.assertEqual(correctme.divdeValues(12,4), 3)
   def test_divdeValues2(self):
      self.assertEqual(correctme.divdeValues(120,4), 30)

   def test_checkEven0(self):
      self.assertTrue(correctme.checkEven(4))
   def test_checkEven1(self):
      self.assertTrue(correctme.checkEven(12))
   def test_checkEven2(self):
      self.assertTrue(correctme.checkEven(420))
   def test_checkEven3(self):
      self.assertFalse(correctme.checkEven(69))

   def test_checkValue0(self):
      self.assertEqual(correctme.checkValues(1,2), 2)
   def test_checkValue1(self):
      self.assertEqual(correctme.checkValues(12, 16), 16)
   def test_checkValue2(self):
      self.assertEqual(correctme.checkValues(12,12), 144)
   def test_checkValue3(self):
      self.assertEqual(correctme.checkValues(0, -1), 0)