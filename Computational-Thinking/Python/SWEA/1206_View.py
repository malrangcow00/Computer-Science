for T in range(1,11):
    result = 0
    nums = int(input())
    height = list(map(int , input().split()))
    for i in range(2, nums-2):
        close_build = [height[i-1],height[i-2],height[i+1],height[i+2]]
        viewer = max(close_build)
        if height[i] > viewer:
            result += ( height[i] - viewer )
  
    print(f'#{T} {result}')