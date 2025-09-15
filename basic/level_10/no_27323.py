# 유니온 파인드 (Disjoint Set Union)

# 대표(부모) 노드 찾기 (경로 압축)
def find_parent(parent, x):
    if parent[x] != x:             # 루트 노드가 아니라면
        parent[x] = find_parent(parent, parent[x])  # 재귀적으로 루트 찾아가기 + 경로 압축
    return parent[x]

# 두 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
