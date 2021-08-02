import collections


def solution(str1: str, str2: str):
    l_1 = make_set(str1)
    l_2 = make_set(str2)

    if len(l_1) == 0 and len(l_2) == 0:
        return 65536

    print(l_1, l_2)

    num = set(l_1) & set(l_2)
    denum = set(l_1) | set(l_2)

    print(num, denum)

    if len(num) == 1 and len(denum) == 1:
        num = min(len(l_1), len(l_2))
        denum = max(len(l_1), len(l_2))
        J = num / denum
    else:

        instance_1 = collections.Counter(l_1)
        for item in instance_1.items():
            if item > 1:
                dup = item
        instance_2 = collections.Counter(l_2)
        intersection_num = min(instance_1[list(num)[0]], instance_2[list(num)[0]])
        union_num = len(l_1) + len(l_2) - intersection_num
        print(union_num)

        J = intersection_num/union_num

    return int(J * 65536)


def make_set(str: str):
    l = []
    p1, p2 = 0, 1

    while p2 < len(str):
        word = str[p1] + str[p2]
        if word.isalpha():
            l.append(word.lower())
        p1 += 1
        p2 += 1
    return l


if __name__ == '__main__':
    str1 = 'FRANCE'
    str2 = 'FRENCH'

    str3 = 'aa1+aa2'
    str4 = 'AAAA12'

    str5 = 'abcccc'
    str6 = 'cccdefff'
    # a = []
    # p1, p2 = 0, 1
    # while p2 < len(str4):
    #     word = str4[p1] + str4[p2]
    #     if word.isalpha():
    #
    #         a.append(word.lower())
    #     p1 += 1
    #     p2 += 1
    print(solution(str1, str2))
