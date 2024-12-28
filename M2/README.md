## Document Reconstruction

Given a string *S[1..n]* with no whitespace, your goal is to reconstruct the 
string by splitting it into valid words separated by spaces (if possible).

For example, 
`"it was the best of times"` is a reconstruction of `"itwasthebestoftimes"`.
Words may also contain punctuation: `"I'llhavewhatshe'shaving"` can be 
reconstructed as `"I'll have what she's having"`.
Some strings cannot be reconstructed, such as`"qwertyuiop"`.

#### Install dependencies
We need an English frequency dictionary, so install the 
[wordfreq](https://pypi.org/project/wordfreq/) library by running 
`python3 -m pip install -r requirements.txt`.

#### Part A

The first part of your assignment is to complete the `naive_reconstruct` 
function in `reconstruct.py`, which  should take a string with no whitespace and 
return a reconstruction if possible, or `None` if not.
Your algorithm should run in *O(nk)*, where *k* is the length 
of the longest word in the dictionary. This is provided as `max_word_length`.

**Use the provided `is_valid` function to check if a word is in the dictionary.
This will ignore whitespace and leading / trailing punctuation.**
```pydocstring
>>> is_valid("the")
True
>>> is_valid("end.")
True
>>> is_valid("en.d")
False
>>> is_valid("zxcvbnm")
False
>>> is_valid("not a word")
Traceback (most recent call last):
ValueError: Invalid argument: 'not a word'
Words cannot contain whitespace
```

A second signature is provided for `backtrack`, a helper function which uses
information about the starting positions of words in the string to reconstruct 
the document.
Implementing this function is not required - you may also define your own 
backtracking function, or include all backtracking code in your 
`reconstruct` function - but you may find it helpful.

Note: Certain strings may become ambiguous when the spaces are removed. For 
example, `"listentoyourheart"` can be reconstructed in several ways, including
`"listen to your heart"` and `"listen toy our he art"`.

For this part of the problem, don't worry about finding the "correct" 
reconstruction - any sequence of dictionary words is fine.


#### Part B

There is actually a fairly easy way to improve the output of this naive 
algorithm. Rather than settling for any reconstruction of the string, we 
can look for the *most likely* reconstruction. 

To do this, we assume that each word *w* is picked independently with 
probability *P(w)*. The probability of some reconstruction is the product 
of the probabilities of the individual words. 
For example, the probability of the sentence `"This is good"` is equal to 
`P("This") * P("is") * P("good")`. We compute the reconstruction with the 
maximum probability.

Implement this strategy in the `likely_reconstruct` function in `reconstruct.py`.
Once again, your algorithm should run in *O(nk)* time. 

**Use the provided `word_prob` function to compute a word's probability,
as shown below. It will ignore whitespace and leading / trailing punctuation.**
```pydocstring
>>> word_prob("the")
0.05370317963702527
>>> word_prob("end.'")
0.00047863009232263854
>>> word_prob("zxcvbnm")
0.0
>>> word_prob("not a word")
Traceback (most recent call last):
ValueError: Invalid argument: not a word
Words cannot contain whitespace
```
Words with zero probability are considered invalid (not in the dictionary).

Multiplying probabilities is not a great idea, because it leads to underflow:
```pydocstring
>>> .00001 ** 60
1.0000000000000048e-300
>>> (.00001 ** 60) * (.00003 ** 10)
0.0
>>> from sys import float_info
>>> float_info.min
2.2250738585072014e-308
```
To avoid this, you can use the following trick:
```pydocstring
>>> from math import log
>>> -log(.00001 ** 60 * .00003 ** 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> -log(.00001 ** 60)
690.7755278982137
>>> -log(.00003 ** 10)
104.14313176302119
>>> -log(.00001 ** 60) + -log(.00003 ** 10)
794.9186596612349
```
Note that this function increases in value as the probability of an event 
decreases. The most likely reconstruction is the one which minimizes this 
cost function.

#### Unit tests

A  number of unit tests are provided for guidance in the `/tests` folder. 
It can be run with the `pytest` command.
You can specify a single test with `pytest tests/test_basic.py`.
You can exclude a test with `pytest --ignore tests/test_random_100000.py`
(this largest test may take up to 1 minute).

If you choose to implement `backtrack` some other way, then it's 
fine if `test_backtrack.py` doesn't pass. 

As always, you are welcome to write your own test cases, but please do not 
modify the existing ones.
