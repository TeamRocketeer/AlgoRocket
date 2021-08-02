import collections


class Solution:
    def solution(self, skill, skill_tree):

        answer = 0
        ans_list = []
        for k in range(len(skill) + 1):
            ans_list.append(skill[:k])

        for item in skill_tree:
            tmp = []
            for i in range(len(item)):
                if item[i] in skill:
                    tmp.append(item[i])

            if ''.join(tmp) in ans_list:
                answer += 1
        return answer

    def shorter_sol(self, skill, skill_tree):
        answer = 0
        for item in skill_tree:
            s = ""
            for i in item:
                if i in skill:
                    s += i
            if s == skill[:len(s)]:
                answer += 1
        return answer


if __name__ == '__main__':
    skill = 'CBD'
    skill_tree = ["BACDE", "CBADF", "AECB", "BDA"]
    # skill_tree = ["AEF", "ZJW"]
    sol = Solution()
    print(sol.solution(skill, skill_tree))
    print(sol.shorter_sol(skill, skill_tree))
