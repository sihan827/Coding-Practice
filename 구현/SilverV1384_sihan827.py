import sys

input = sys.stdin
group_idx = 1

while True:
    N = int(input.readline())
    if N == 0:
        break
    names = []
    bad_words = []
    for i in range(N):
        line = input.readline().rstrip().split()
        names.append(line[0])
        line = line[1:]
        bad_words.append(line)
    names = names * 2

    # 이름이 아래부터 위로 작성되지만 읽는거는 위에서 아래로 읽는 것에 주의
    print("Group", str(group_idx))
    chat_guys = 0
    for i in range(N):
        # 이름을 가져와서 순서를 거꾸로 뒤집음
        order = names[i+1:i+1+N]
        order = order[::-1]
        order.remove(names[i])
        #print(order, bad_words[i])

        # N이 있으면 바로 출력
        for j in range(N-1):
            if bad_words[i][j] == "N":
                print(order[j], "was nasty about", names[i])
                chat_guys += 1
        
    if chat_guys == 0:
        print("Nobody was nasty")
    
    group_idx += 1
    print()