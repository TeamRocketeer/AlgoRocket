def binary(number) :
    binary_list = []
    # 문자열 인덱스 0, 1 제외하고 그 다음 2부터 1의 갯수 체크?
    b_n = str(bin(number))
    for i in range(2, len(b_n)):
        binary_list.append(b_n[i])

    return binary_list


def solution(n):
    answer = n
    n_list = binary(n)
    n_count = n_list.count('1')

    while True :
        answer += 1
        a_list = binary(answer)
        if n_count == a_list.count('1') :
            break

    return answer

if __name__ == '__main__' :
    n_1 = 78
    n_2 = 15
    n_3 = 3

    print(solution(n_3))