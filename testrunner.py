from unittest import TestLoader, TextTestRunner

if __name__ == '__main__':
    testsuite = TestLoader().discover('.', pattern='*_test.py')
    TextTestRunner(verbosity=1).run(testsuite)
