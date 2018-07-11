"""
乱序字符串是指一个字符串只是另一个字符串的重新排列。例如，'heart' 和 'earth' 是乱序字符串。'python' 和 'typhon' 也是。为了简单起见，我们假设所讨论的两个字符串具有相等的长度，并且他们由 26 个小写字母集合组成。
"""

# 解法1:检查
def anagramSolution1(s1, s2):
    a_list = list(s2)
    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False

        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            a_list[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK


def anagramSolution2(s1, s2):
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    pos = 0
    matche = True

    while pos < len(s1) and matche:
        if list1[pos] == list2[pos]:
            pos = pos + 1
        else:
            matche = False
            return matche
    return matche





if __name__ == '__main__':
    s1 = 'abcd'
    s2 = 'dcbd'
    if anagramSolution2(s1, s2):
        print("YES")
    else:
        print("NO")