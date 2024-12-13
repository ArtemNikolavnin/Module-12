import unittest
import tests_12_3

#создание TestSuite
suite = unittest.TestSuite()

#добавление тестов
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

#запуск тестов
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)