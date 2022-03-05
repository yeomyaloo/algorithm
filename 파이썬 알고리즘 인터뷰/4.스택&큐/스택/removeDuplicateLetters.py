import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack =collections.Counter(s),set(),[]

        for i in s:
            counter[i] -= 1
            if i in seen:
                continue
            #현재 스택이 비어있지 않고 지금 비교하는 글자가 스택 맨 위의 글자보다 크고 문자가 뒤에 더 남아있다면
            while stack and i < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(i)
            seen.add(i)
        return ''.join(stack)