import pytest
from reconstruct import likely_reconstruct
from utils import remove_whitespace, reconstruct_sentences, remove_punctuation


erdos = "a mathematician is a device for turning coffee into theorems"


ctci = " ".join("""
Although he was quite intelligent, he struggled to solve the interview problems.
Most successful candidates could fly through the first question, which was a twist on a known problem,
but he had trouble developing an algorithm.
When he came up with one, he failed to consider solutions that optimized for
other scenarios. Finally, when he began coding, he flew through the code with an initial solution, but it
was riddled with mistakes that he failed to catch. Though he was not the worst candidate we had seen by any
measure, he was far from meeting the "bar". Rejected.
""".split("\n"))


zen = " ".join("""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases are not special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you are Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it is a bad idea.
If the implementation is easy to explain, it could be a good idea.
Namespaces are one honking great idea --let us do more of those!
""".split("\n"))


hamlet = " ".join("""
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die to sleep,
No more; and by sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: it's a consummation
Devoutly to be wished. To die, to sleep;
To sleep, perchance to dream ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause there's the respect
That makes calamity of so long life.
""".split("\n"))


@pytest.mark.parametrize("text", [erdos, ctci, zen, hamlet])
def test_likely(text):
    original = remove_punctuation(text).strip()
    garbled = remove_whitespace(original)
    result = likely_reconstruct(garbled)
    assert result == original
