import unittest

from HTMLTestRunner import HTMLTestRunner

from cart_sauce_demo_unitest import CartTests
from login_sauce_demo_unitest import LoginTests


class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests(
            [
                unittest.defaultTestLoader.loadTestsFromTestCase(CartTests),
                unittest.defaultTestLoader.loadTestsFromTestCase(LoginTests)

            ]

        )
        runner = HTMLTestRunner(
            report_name='Sauce Demo Tests',
        )
        runner.run(teste_de_rulat)
