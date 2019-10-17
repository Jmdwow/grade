import unittest

from grade.mixins import *


class TestScoringMixin(ScoringMixin, unittest.TestCase):

    def test_score(self):
        """ Can we modify and recall a tests score? """
        class Test(ScoringMixin):
            def test_something(self):
                self.score = 10
                assert(self.score == 10)

        x = Test()
        x.test_something()
        self.assertEqual(x.test_something.__score__, 10)
        return

    def test_weight(self):
        """ Can we modify and recall a tests weight? """
        class Test(ScoringMixin):
            def test_something(self):
                self.weight = 10
                assert(self.weight == 10)

        x = Test()
        x.test_something()
        self.assertEqual(x.test_something.__weight__, 10)
        return

    def test_visibility(self):
        """ Can we modify and recall a tests visibility? """
        class Test(ScoringMixin):
            def test_something(self):
                self.visibility = 'invisible'
                assert(self.visibility == 'invisible')

        x = Test()
        x.test_something()
        self.assertEqual(x.test_something.__visibility__, 'invisible')
        return

    def test_leaderboard(self):
        """ Can we modify and recall a tests leaderboard standing? """
        class Test(ScoringMixin):

            def test_something(self):
                self.leaderboardTitle = 'Runtime'
                self.leaderboardOrder = 'desc'
                self.leaderboardScore = 100
                assert(self.leaderboard == {
                    'title': 'Runtime',
                    'order': 'desc',
                    'score': 100
                })
        
        x = Test()
        x.test_something()
        self.assertEqual(x.test_something.__leaderboard_title__, 'Runtime')
        self.assertEqual(x.test_something.__leaderboard_order__, 'desc')
        self.assertEqual(x.test_something.__leaderboard_score__, 100)
        return
