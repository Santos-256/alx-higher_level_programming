#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    if sentence:
        length = len(sentence)
    return (length, sentence if not sentence else sentence[:1])
