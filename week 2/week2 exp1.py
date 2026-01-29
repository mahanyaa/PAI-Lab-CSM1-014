import heapq

def water_jug(A, B, target):
    start = (0, 0)

    h = lambda s: min(abs(target - s[0]), abs(target - s[1]))

    def neighbors(a, b):
        return [
            (A, b), (a, B),        # fill
            (0, b), (a, 0),        # empty
            (a - min(a, B - b), b + min(a, B - b)),  # A -> B
            (a + min(b, A - a), b - min(b, A - a))   # B -> A
        ]

    pq = [(h(start), 0, start, [start])]
    visited = set()

    while pq:
        _, g, (a, b), path = heapq.heappop(pq)

        if (a, b) in visited:
            continue
        visited.add((a, b))

        if a == target or b == target:
            return path

        for s in neighbors(a, b):
            if s not in visited:
                heapq.heappush(
                    pq, (g + 1 + h(s), g + 1, s, path + [s])
                )

    return None

for step in water_jug(4, 3, 2):
    print(step)


