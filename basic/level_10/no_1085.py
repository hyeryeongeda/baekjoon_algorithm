x,y,w,h = map(int, input().split())
#x나y 중에 0과 가깝거나 w,h와 가까운곳으로 이동하면 될 일
print(min(x, y, w-x, h-y))