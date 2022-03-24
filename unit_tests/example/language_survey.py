#! /home/toni/.pyenv/shims/python3
"""
Created on May 1, 2020

@author:toni
"""

from survey import AnonymousSurvey


def language_survey():
    """
    Ask a question and get answers.
    """
    # Define a question, and make a survey.
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    # Show the question, and store responses to the question.
    my_survey.show_question()
    print("Enter 'q' at any time to quit.\n")
    while True:
        response = input("Language: ")
        if response == 'q':
            break
        my_survey.store_response(response)
    # Show the survey results.
    print("\nThank you to everyone who participated in the survey!")
    my_survey.show_results()


def main():
    language_survey()


if __name__ == "__main__":
    main()
