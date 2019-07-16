import unittest
import mock

from dogAge import getWeight, getAge, youngDog, smallDog, medDog, lrgDog, giantDog, runAgain

class DogAgeTest(unittest.TestCase):
    def test_getWeight_returns_valid_value(self):
        with mock.patch('builtins.input', return_value=10):
            assert getWeight() == 10

    def test_getAge_returns__valid_value(self):
        with mock.patch('builtins.input', return_value=10):
            assert getAge() == 10

    def test_young_dog_returns_correct_age(self):
        self.assertEqual(youngDog(1),15)

    def test_smallDog_returns_correct_age(self):
        self.assertEqual(smallDog(10),56)

    def test_medDog_returns_correct_age(self):
        self.assertEqual(medDog(12),73)

    def test_lrgDog_returns_correct_age(self):
        self.assertEqual(lrgDog(12),82)

    def test_giantDog_returns_correct_age(self):
        self.assertEqual(giantDog(7),59)

    # TODO: negative value testing, integration test
