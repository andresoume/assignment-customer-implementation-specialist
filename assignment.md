# Assignment: Luhn Validator

## Intro

Hello there! First of all, congratulations - if you're asked to complete this assessment,
it means we believe you're a promising candidate for the _Customer Implementation Skills_. However, the technical
skills you'll need in your role are hard to judge by talking, so we would like to ask you to complete this small
programming challenge.

## General instructions

We would like to ask you to complete this assignment using the [Python](https://docs.python.org/3/) language,
since this is one of our main application development and data analysis languages at Source.

To get started, please make a private fork of this [Git](https://git-scm.com/) repository, and commit + push
your code to the fork.

To help you out, we have provided a set of test cases to validate your implementation.
To run these tests, you will need a Python 3 interpreter installed. Then, assuming your implementation script is called `luhn.py`, just run:

```bash
$ python tests.py
```

### Functional Requirements

For this assignment, please create a command line application implementing the algorithm described
in the next section. This application should:

- print a message asking for the user to input a credit card number
- accept a single string of text on STDIN (read until the end)
- exit with status 0 _if_ the provided string is valid according to the algorithm
- exit with status **42** otherwise

### Non-functional requirements

- Use Python 3.10 or higher
- Do not use any additional modules outside of the Python standard library. That should be more than enough for this script.
- Maintainability is favoured over performance. No complex performance optimizations should be needed. Another team member should be able to continue where you left off
- It should be possible to run the script on any machine with a Python 3.10 interpreter
- This assignment was designed to be completed in 2-3h. The evaluation will take into account the choices you make and what you focus on given the time you have. However, it's up to you if you spend less or more time on it.
- Please make sure the final commit to your repository is done at least 24 hours before the start of your interview

## Algorithm description

Given a number determine whether or not it is valid per the Luhn formula.

The [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) is
a simple checksum formula used to validate a variety of identification
numbers, such as credit card numbers and Canadian Social Insurance
Numbers.

The task is to check if a given string is valid.

## Validating a Number

Strings of length 1 or less are not valid. Spaces are allowed in the input,
but they should be stripped before checking. All other non-digit characters
are disallowed.

## Example 1: valid credit card number

```text
4539 1488 0343 6467
```

The first step of the Luhn algorithm is to double every second digit,
starting from the right. We will be doubling

```text
4_3_ 1_8_ 0_4_ 6_6_
```

If doubling the number results in a number greater than 9 then subtract 9
from the product. The results of our doubling:

```text
8569 2478 0383 3437
```

Then sum all of the digits:

```text
8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80
```

If the sum is evenly divisible by 10, then the number is valid. This number is valid!

## Example 2: invalid credit card number

```text
8273 1232 7352 0569
```

Double the second digits, starting from the right

```text
7253 2262 5312 0539
```

Sum the digits

```text
7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57
```

57 is not evenly divisible by 10, so this number is not valid.

## Deliverables

This assignment should be delivered in the following way:

- All code is pushed to your private copy of this repository.
- Any additional information/documentation you would like to share is included in the README.md file.
- Our recruiter will provide you with the Github usernames of your reviewers; they should be added as collaborators to your fork of this repository.

## Assessment Criteria

The solution will be assessed on the following criteria:

- How is your code structured? Is it easy to read and follow?
- How clear is the documentation?
- Are there any clear bugs in your code?
- Can you clearly and concisely describe the process you have followed and the choices you have made?
