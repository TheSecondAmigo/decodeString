#!/usr/bin/env python3

"""

Medium

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example,
the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""

encoded = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
           '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j',
           '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o',
           '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't',
           '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y',
           '26': 'z'}


def decode(countlist, msg):
    # print(f"In decode, {countlist =}, {msg = }")
    if msg == '':
        countlist[0] += 1
        return
    if msg[0] in encoded:
        decode(countlist, msg[1:])

        # only if substring of length 2 exists ...
        if msg[0] != msg[:2] and msg[:2] in encoded:
            decode(countlist, msg[2:])


def decode_msg(msg):
    countlist = [0]
    decode(countlist, msg)
    return countlist[0]


if __name__ ==  "__main__":

    tests = [('1234', 3),   # 'abcd', 'awd', 'lcd',
             ('111', 3), # 'aaa', 'ka', and 'ak'.
             ('1226', 5),   # 'abbf', 'lbf', 'avf', 'lz', 'abz'
            ]
    for msg, exp in tests:
        rc = decode_msg(msg)
        print(f"{msg = }, {exp = }, {rc = }, {exp == rc}")
