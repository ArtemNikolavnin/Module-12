import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
