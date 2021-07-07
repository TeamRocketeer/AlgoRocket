from collections import deque


class Solution:
    def solution_1(self, dir: str) -> int:
        visited = set()
        x, y = 0, 0
        visited.add((x, y))
        dq_dir = deque(dir)

        while dq_dir:

            tmp = dq_dir.popleft()

            # MOVE the point
            if -5 < x < 5:

                if tmp == 'L':
                    x -= 1
                elif tmp == 'R':
                    x += 1

            if -5 < y < 5:

                if tmp == 'U':
                    y += 1
                elif tmp == 'D':
                    y -= 1

            if -5 <= x <= 5 and -5 <= y <= 5:
                visited.add((x, y))
            else:
                continue

        return len(visited)

    def solution_2(self, dir: str) -> int:
        x, y = 0, 0
        answer = 0
        visited = set()
        dq_dir = deque(dir)

        while dq_dir:
            p = dq_dir.popleft()

            # 좌표 이동
            if p == 'L':
                if x == -5:
                    continue
                else:
                    if (x, y) not in visited:
                        visited.add((x, y))
                        answer += 1
                    x -= 1

            elif p == 'R':
                if x == 5:
                    continue
                else:
                    if (x, y) not in visited:
                        visited.add((x, y))
                        answer += 1
                    x += 1
            elif p == 'U':
                if y == 5:
                    continue
                else:
                    if (x, y) not in visited:
                        visited.add((x, y))
                        answer += 1
                    y += 1
            elif p == 'D':
                if y == -5:
                    continue
                else:
                    if (x, y) not in visited:
                        visited.add((x, y))
                        answer += 1
                    y -= 1


        return answer



if __name__ == '__main__':
    # dir = "LULLLLLLU"
    dir = "ULURRDLLU"
    answer = 7
    sol = Solution()
    print(sol.solution_2(dir) == answer)
