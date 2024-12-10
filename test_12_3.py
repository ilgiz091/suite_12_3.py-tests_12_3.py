import unittest
from runner import Runner
from runner_and_tournament import Runner, Tournament

def skip_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_method(self, *args, **kwargs)
    return wrapper

class TestRunner(unittest.TestCase):
    is_frozen = False

    @skip_frozen
    def test_walk(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_frozen
    def test_run(self):
        runner = Runner("Test Runner 2")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_frozen
    def test_challenge(self):
        runner1 = Runner("Runner A")
        runner2 = Runner("Runner B")
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

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    @skip_frozen
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results[1] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

    @skip_frozen
    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[2] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

    @skip_frozen
    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[3] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

if __name__ == '__main__':
    unittest.main()