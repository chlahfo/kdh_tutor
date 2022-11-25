#양꼬치
def solution(n, k):
    yang = 12000 * n
    um = 2000 * (k - (n//10))

    answer = yang + um
    return answer