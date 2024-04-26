import sys

N = int(sys.stdin.readline())
nodes_par = list(map(int, sys.stdin.readline().split()))
root_idx = nodes_par.index(-1)
del_node = int(sys.stdin.readline())
cnt = 0

# 트리 객체 정의
class Tree():
    def __init__(self, num):
        self.num = num
        self.childs = []

    def add_child(self, child):
        self.childs.append(child)

# 탐색 (깊이 우선탐색)
def traversal(node):
    global cnt, del_node
    # 삭제할 노드 있으면 바로 삭제하고 탐색 시작
    for child in node.childs:
        if child.num == del_node:
            node.childs.remove(child)
    if node.num == del_node:
        return
    if not node.childs:
        cnt += 1
        return
    for child in node.childs:
        traversal(child)

nodes = [Tree(i) for i in range(len(nodes_par))]

# 노드별로 부모노드에 연결해줌
for i in range(len(nodes_par)):
    if nodes_par[i] == -1:
        continue
    else:
        nodes[nodes_par[i]].add_child(nodes[i])

traversal(nodes[root_idx])
print(cnt)