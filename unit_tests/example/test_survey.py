#! /home/toni/.pyenv/shims/python3
"""
Created on May 1, 2020

@author:toni

The method setUp() does two things: it creates a survey instance and it
creates a list of responses. Each of these is prefixed by self, so
they can be used anywhere in the class. This makes the two test methods
simpler, because neither one has to make a survey instance or a response.

Before setUp() was defined, you had to initialize an instance of the class
AnonymousSurvey within each test method that tested some specific part of
the mentioned class.
"""

import unittest

from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Portuguese', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that a three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
