class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for st in tokens:
            if st in "+-*/":
                b=stack.pop()
                a=stack.pop()
                if st=="+":
                    stack.append(a+b)
                elif st=="-":
                    stack.append(a-b)
                elif st=="*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(st))
        return stack[0]

        