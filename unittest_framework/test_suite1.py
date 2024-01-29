import unittest

from pack1.login import Testlogin
from pack1.signup import Testsignup
from pack2.payment import TestPayment
from pack2.refund import TestRefund

# to collect all test cases

tcs1=unittest.TestLoader().loadTestsFromTestCase(Testlogin)
tcs2=unittest.TestLoader().loadTestsFromTestCase(Testsignup)
tcs3=unittest.TestLoader().loadTestsFromTestCase(TestPayment)
tcs4=unittest.TestLoader().loadTestsFromTestCase(TestRefund)

# create test suite

master = unittest.TestSuite([tcs1, tcs2, tcs3,tcs4])
sanity = unittest.TestSuite([tcs1, tcs2])
func = unittest.TestSuite([tcs3, tcs4])

# to run the test suite

unittest.TextTestRunner(verbosity=2).run(master)

#https://docs.python.org/3/library/unittest.html
