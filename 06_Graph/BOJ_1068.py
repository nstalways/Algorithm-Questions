import sys
from copy import deepcopy


def solution(tree_info, target_node):
    """
    1. tree를 만든다.
    2. target node를 지운다.
    3. leaf node의 개수를 세고, 반환한다.
    """
    # tree 만들기
    def mk_tree(tree_info):
        root_node = None
        tree = [[] for _ in range(len(tree_info))]
        for parent, child in tree_info:
            if parent == -1: # root인 경우
                root_node = child
                continue
            
            tree[parent].append(child)

        return tree, root_node
    
    # target node와 연결된 node들을 찾기
    def search_subtree(tree, target_node):
        subtree = [target_node]
        stack = [target_node]

        while stack:
            parent = stack.pop()
            children = tree[parent]

            if not children:
                continue

            for child in children:
                if child not in subtree:
                    stack.append(child)
                    subtree.append(child)
        
        return subtree

    # target node 지우기
    def rm_node(tree, subtree):
        tree_cp = deepcopy(tree)

        # subtree에 담겨있는 node들을 tree에서 삭제
        for node in subtree:
            tree_cp[node] = []
        
        # tree의 남은 node 중 subtree에 포함되는 node가 있는 경우 삭제
        for parent, children in enumerate(tree_cp):
            for child in children:
                if child in subtree:
                    tree_cp[parent].remove(child)

        return tree_cp

    # leaf node 세기
    def cnt_leaf_node(tree, root_node):
        cnt = 0
        visited = [root_node]
        stack = [root_node]

        while stack:
            curr_node = stack.pop()

            if not tree[curr_node]: # 자식 노드가 없는 경우
                cnt += 1
                continue

            for child in tree[curr_node]:
                if child not in visited:
                    stack.append(child)
                    visited.append(child)
        
        return cnt
    
    orig_tree, root_node = mk_tree(tree_info)

    if root_node == target_node:
        print(0)
    else:
        subtree = search_subtree(orig_tree, target_node)
        removed_tree = rm_node(orig_tree, subtree)
        num_leaf_node = cnt_leaf_node(removed_tree, root_node)

        # print(f"Tree Info: {tree_info}")
        # print(f"original tree: {orig_tree}")
        # print(f"Subtree: {subtree}")
        # print(f"After removed target node: {removed_tree}")
        print(num_leaf_node)
    


if __name__ == "__main__":
    num_node = int(input()) # 1 이상 50 이하의 자연수

    tree_info = [(parent, child) for child, parent in enumerate(list(map(int, sys.stdin.readline().split())))]
    # tree_info.sort(key=lambda x: x[0])

    target_node = int(input())

    solution(tree_info, target_node)
