import unittest
import tests_12_3
#
test123 = unittest.TestSuite()
test123.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test123.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
#
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test123)
#
