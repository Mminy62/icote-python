'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.
'''

def solution(p):
    answer = ''
    u, v = separate(p)

    if not p:
        return answer
    # u, v로 분리시킨 다음 u가 올바른 것인지 검사해야함.
    # u 올바른지 검사
    # u 에 관련되어서만 처리하고 v는 마지막에 solution(v)로 처리한다. v(빈문자열) -> u가 되는 것까지
    if correct(u): #올바른 것
        answer += u + solution(v)

    else:# 아닌 것
        answer += '(' + solution(v) + ')'

        # u 뒤바꾸기
        temp = ''
        u = list(u) ## list(u[1:-1])
        u.pop(0)
        u.pop()
        for i in range(len(u)):
            if u[i] == '(':
                temp += ')'
            else:
                temp += '('
        answer += temp
    return answer

def separate(w):
    padict = {'(': 1, ')': -1}

    utemp = 0
    u = ''
    for pa in w:
        utemp += padict[pa]
        u += pa
        if utemp == 0:
            break

    v = w[len(u):]

    return (u, v)

def correct(u):
    stack = []
    top = ''
    for pa in list(u):
        stack.append(pa)
        if pa == ')' and len(stack) > 1:
            if top == '(':
                stack.pop()
                stack.pop()

        if stack:
            top = stack[-1]

    if not stack:
        return True
    else:
        return False

print(solution(')('))