import unittest
from runner_and_tournament import Runner, Tournament

def run_if_not_frozen(func):
    def wrapper(self, *args, **kwargs):
        if not self.is_frozen:
            return func(self, *args, **kwargs)
        else:
            return unittest.skip("Тесты в этом кейсе заморожены")(func)(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @run_if_not_frozen
    def test_walk(self):
        runner = Runner("Артем")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @run_if_not_frozen
    def test_run(self):
        runner = Runner("Игорь")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @run_if_not_frozen
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

    @run_if_not_frozen
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        TournamentTest.all_results["test_usain_and_nick"] = result
        self.assertEqual(list(result.values())[-1].name, 'Ник')

    @run_if_not_frozen
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results["test_andrey_and_nick"] = result
        self.assertEqual(list(result.values())[-1].name, 'Ник')

    @run_if_not_frozen
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

