import unittest
import main as app


class AddTwoNumbersTest(unittest.TestCase):
    "Basic Tests"

    def test_password_has_less_then_5_chars(self):
        self.assertEqual(app.validatePassword("abcd"),
                         "Password has to have 5 characters at least!")

    def test_password_has_no_digit(self):
        self.assertEqual(app.validatePassword("thisispassword"),
                         "Password has to contain one digit at least!")

    def test_password_is_valid(self):
        self.assertTrue(app.validatePassword("Password1"))

if __name__ == '__main__':
    unittest.main()
