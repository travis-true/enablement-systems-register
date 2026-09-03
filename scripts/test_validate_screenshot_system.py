import unittest
from scripts.validate_screenshot_system import validate

class ScreenshotSystemValidationTests(unittest.TestCase):
    def test_package_validates(self):
        self.assertEqual(validate(), [])

if __name__ == "__main__":
    unittest.main()
