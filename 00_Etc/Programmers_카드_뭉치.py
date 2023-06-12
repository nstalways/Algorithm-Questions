from collections import deque

def solution(cards1, cards2, goal):
    cards1, cards2, goal = deque(cards1), deque(cards2), deque(goal)
    
    flag = True
    while goal:
        ch = goal.popleft()
        
        if cards1 and ch == cards1[0]:
            cards1.popleft()
        elif cards2 and ch == cards2[0]:
            cards2.popleft()
        else:
            flag = False
            break
            
    return "Yes" if flag else "No"


if __name__ == "__main__":
    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # Yes
    print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # No