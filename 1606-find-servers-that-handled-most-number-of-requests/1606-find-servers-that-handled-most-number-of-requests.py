
import heapq

class Solution:
    def busiestServers(self, k, arrival, load):

        # Segment tree: 1 means available, 0 means busy
        tree = [0] * (4 * k)

        def build(node, left, right):
            if left == right:
                tree[node] = 1
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        # Update server availability
        def update(node, left, right, idx, value):
            if left == right:
                tree[node] = value
                return

            mid = (left + right) // 2

            if idx <= mid:
                update(node * 2, left, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, right, idx, value)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        # Find first available server in a range
        def find_first(node, left, right, ql, qr):

            if ql > qr or tree[node] == 0:
                return -1

            if right < ql or left > qr:
                return -1

            if left == right:
                return left

            mid = (left + right) // 2

            result = find_first(
                node * 2, left, mid, ql, qr
            )

            if result != -1:
                return result

            return find_first(
                node * 2 + 1, mid + 1, right, ql, qr
            )

        build(1, 0, k - 1)

        # Min heap: (finish_time, server_id)
        busy = []

        # Count requests handled by each server
        count = [0] * k

        for i in range(len(arrival)):

            # Release servers that have finished
            while busy and busy[0][0] <= arrival[i]:

                finish, server = heapq.heappop(busy)

                update(1, 0, k - 1, server, 1)

            # Preferred server
            start = i % k

            # Search from start to k-1
            server = find_first(
                1, 0, k - 1, start, k - 1
            )

            # Wrap around if necessary
            if server == -1:
                server = find_first(
                    1, 0, k - 1, 0, start - 1
                )

            # All servers are busy
            if server == -1:
                continue

            # Assign request
            count[server] += 1

            update(1, 0, k - 1, server, 0)

            finish_time = arrival[i] + load[i]

            heapq.heappush(
                busy, (finish_time, server)
            )

        # Find maximum requests handled
        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]
