# Enter your code here. Read input from STDIN. Print output to STDOUT
class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        self.in_stack.append(value)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            return self.out_stack.pop()
        return None

    def front(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            return self.out_stack[-1]
        return None

def process_queries(queries):
    queue = Queue()
    
    for query in queries:
        query_type = query[0]
        if query_type == 1:
            queue.enqueue(query[1])
        elif query_type == 2:
            queue.dequeue()
        elif query_type == 3:
            print(queue.front())

n = int(input())
queries = []

for _ in range(n):
    query = list(map(int, input().split()))
    queries.append(query)

process_queries(queries)
