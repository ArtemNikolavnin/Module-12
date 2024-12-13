import unittest
from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner("Артем")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner("Игорь")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner("Наташа")
        runner2 = Runner("Полина")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    def tearDownClass():
        print("\nРезультаты всех тестов:")
        for key, value in TournamentTest.all_results.items():
            formatted_result = {k: v.name for k, v in value.items()}
            print(formatted_result)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_third_tournamen(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        TournamentTest.all_results["test_usain_and_nick"] = result
        self.assertEqual(list(result.values())[-1].name, 'Ник')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results["test_andrey_and_nick"] = result
        self.assertEqual(list(result.values())[-1].name, 'Ник')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results["test_all_runners"] = result
        self.assertEqual(list(result.values())[-1].name, 'Ник')

if __name__ == '__main__':
    unittest.main()
