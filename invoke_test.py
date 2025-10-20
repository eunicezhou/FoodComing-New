import unittest

if __name__ == "__main__":
    tests = unittest.TestLoader().discover("tests")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests)