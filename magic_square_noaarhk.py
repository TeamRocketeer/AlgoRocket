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

    def solution_3(self, dir: str) -> int:
        # visited에 점이 아닌 경로 (두 점의 조합 ) 를 추가한다.
        visited = set()
        x, y = 0, 0
        for p in dir:
            # 아래코드는 ((좌표1) -> (좌표2) ) != ((좌표2) -> (좌표1)) 로 인식하지만 문제조건상 같도록 인식해야 하기때문에
            # 출발 -> 도착이 아닌 (작은수) -> (큰수) 로 설정한다.
            if p == 'U' and y < 5:
                visited.add(((x, y), (x, y + 1)))
                y += 1
            elif p == 'D' and y > -5:
                visited.add(((x, y - 1), (x, y)))
                y -= 1
            elif p == 'L' and x > -5:
                visited.add(((x - 1, y), (x, y)))
                x -= 1
            elif p == 'R' and x < 5:
                visited.add(((x, y), (x + 1, y)))
                x += 1

        print(visited)
        return len(visited)


if __name__ == '__main__':
    # dir = "LULLLLLLU"
    # dir = "ULURRDLLU"
    dir = "UDU"
    answer = 7
    sol = Solution()
    print(sol.solution_3(dir) == answer)
