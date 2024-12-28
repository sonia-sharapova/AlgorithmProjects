[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/48u_gBeE)
# Square Meeting

You are given an $M$ by $M$ grid where each entry in the grid represents an intersection. You and your $N-1$ friends each live in a **different** intersection on this grid. You want to meet in one person's house for your favorite activity of the quarter: studying Algorithms. You can move only along the grid, so the distance from $(a, b)$ to $(c, d)$ is $|a - c| + |b - d|$. Being considerate, you suggest meeting at the house which minimizes the total distance travelled by all of you. Everyone agrees this is the best solution, but cannot decide which house achieves that. Write a program that computes the minimum total distance that all $N$ students need to travel.

## Testing

A number of test cases have been provided and you can test your implemenation by using the `pytest` library.

Install the required libraries by running the following command:

```
python3 -m pip install -r requirements.txt
```

Then, you can run all the tests at once with the following command:

```
python3 -m pytest test_meeting.py
```

The test cases and expected outputs are located in the `testcases` folder. If you want,
you may add additional test cases by adding to this folder (but please do not mess with
the test cases we've provided).

The input files start with a single line representing the number of students, and then each line
is a box in $(x_i, y_i)$ form.

The output files are a single integer, the minimum total distance that the students need to travel.

Note that you do not need to do any parsing of these files yourself—that is handled
for you by our tests.

You can invoke `pytest` in a number of ways. If you'd like, you can read up on that
[here](https://docs.pytest.org/en/6.2.x/usage.html). Most notably, you can run a single
test on its own with the `-k` flag. For instance:

```
python3 -m pytest -k input05
```

This command runs the test from `input05.txt`.

It can also be nice to see only first test that fails, which can be done with the `-x` flag.
Finally, the `-v` flag will make test output more verbose, which can help you diagnose if tests are failing.

## Limits and Notes

The number of students, $N$, will be at least $3$ and at most $500.000$.

The size of the grid $M$ will be at most $10^7$.

All coordinates in the input will be $0 \leq x_i, y_i \leq M$.

The time your code has to pass any one test is 2 seconds. The tests will timeout if
your code takes longer than this time. Different machines run at different speeds,
so the machine that matters here is the one that github uses when it tests your code
after a commit (this is the output we will read when we grade your submission). You can see
these tests run in the `actions` tab of your github repository, after you commit.


## Submission

Submit your code by commiting and pushing it to your github repository. This assignment is
due at the same time as the Homework 1 theory problems, and the same late penalty applies. We will
grade the code based off of the last commit before the deadline.

Note that the tests are mainly to help you confirm that your code is working—your
grade **is not** simply your score on the tests. We will read over your code as
well. *If the deadline is close and you are still not passing tests, you should
push your code anyway—you may get partial credit.*

