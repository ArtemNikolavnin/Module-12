import logging
import unittest
from rt_with_exceptions import Runner, Tournament

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("Артем", speed=-5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            runner = Runner(123)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")

    def test_challenge(self):
        runner1 = Runner("Наташа")
        runner2 = Runner("Полина")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        TournamentTest.all_results["test_usain_and_nick"] = result
        self.assertEqual(list(result.values())[-1].name, 'Ник')

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results["test_andrey_and_nick"] = result
        self.assertEqual(list(result.values())[-1].name, 'Ник')

    def test_all_runners(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results["test_all_runners"] = result
        self.assertEqual(list(result.values())[-1].name, 'Ник')

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            formatted_result = {k: v.name for k, v in value.items()}
            print(formatted_result)


if __name__ == '__main__':
    unittest.main()