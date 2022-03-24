#! /home/toni/.pyenv/shims/python3
"""
Created on May 1, 2020

@author:toni

The class AnonymousSurvey is taken from Pytnon Crash Course. p. 223
There the method show_question just prints 'question' instead of
'self.question'

In show_results(self):

for response in responses:    ->    for response in self.responses:

The moral is: When you define class attributes, all class methods of this
particular class can use those attributes, but they have to be called with
'self.attribute'.
This means that those methods don't need to specify a parameter in their
definition and still can use the attributes freely.
"""


class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)


def main():
    pass


if __name__ == "__main__":
    main()
