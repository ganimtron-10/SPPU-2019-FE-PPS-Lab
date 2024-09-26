"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q10
To input binary number from user and convert it into decimal number.

Explaination Video Link: https://www.youtube.com/watch?v=yRnb482gdiI&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=11&pp=iAQB
"""

# decimal base - 10

# 00
# 01
# 02
# 03
# 04
# 05
# 06
# 07
# 08
# 09
# 10
# 11
# 12
# 13
# 14


# 19
# 20
# 21
# 22
# 23


# 29
# 30
# ....

# binary base - 2

# 0  # -> 0V -> off 0
# 1  # -> 5V -> on 1

# 10  2
# 11  3

# 100  4
# 101  5

# 110  6
# 111  7

# 1000  8
# 1001  9

# 1010  10
# 1011  11

# 3210 - base -> 2

# 0000
# 0001

# 0010
# 0011

# 0100
# 0101

# 0110
# 0111

# 1000
# 1001

# 1010
# 1011

# summation cv * 2 ^ cn


# 0 * 2 ^ 3(8) + 0 * 2 ^ 2(4) + 0 * 2 ^ 1(2) + 0 * 2 ^ 0(1)
# 0 + 0 + 0 + 0 = 0 -> decimal

# 0 * 2 ^ 3(8) + 0 * 2 ^ 2(4) + 0 * 2 ^ 1(2) + 1 * 2 ^ 0(1)
# 0 + 0 + 0 + 1 = 1 -> decimal

# 0 * 2 ^ 3(8) + 0 * 2 ^ 2(4) + 1 * 2 ^ 1(2) + 0 * 2 ^ 0(1)
# 0 + 0 + 2 + 0 = > 2 _ > decimal

# 0 * 2 ^ 3(8) + 0 * 2 ^ 2(4) + 1 * 2 ^ 1(2) + 1 * 2 ^ 0(1)
# 0 + 0 + 2 + 1 = > 3 -> decimal

# 0 * 2 ^ 3(8) + 1 * 2 ^ 2(4) + 0 * 2 ^ 1(2) + 0 * 2 ^ 0(1)
# 0 + 4 + 0 + 0 = > 4

# 0 * 2 ^ 3(8) + 1 * 2 ^ 2(4) + 0 * 2 ^ 1(2) + 1 * 2 ^ 0(1)
# 0 + 4 + 0 + 1 = > 5

# left -> least significant bit
# right -> more significant bit


# summation  of columnval * 2 ^ columnnum


def binarytodecimal(binaryval):
    decimalnum = 0
    for columnnum in range(len(binaryval)):
        columnnum = int(columnnum)
        columnval = int(binaryval[-(columnnum+1)])

        # print(f"{columnval} * 2^{columnnum}")

        decimalnum += (columnval * (2 ** columnnum))
    return decimalnum
# 0101 -> 4 -> 0123


# binarynumfromuser = input("Enter binary number: ")
# print(binarytodecimal(binarynumfromuser))
# print(int(binarynumfromuser, 2))

print(bin(5458)[2:] == "1010101010010")
# 1010101010010
