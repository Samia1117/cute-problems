class Solution:
    
    def operate(self, num1, num2, token):
        if token == "+":
            return num1 + num2

        if token == "-":
            return num1 - num2

        if token == "/":
            return num1 / num2

        if token == "*":
            return num1 * num2
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))
        return stack.pop()
    
        '''
        st = deque()
        operators = ["+", "-", "/", "*"]
        result = None
        i=0
        while i<len(tokens):
            print ("stack is: ", st)
            print("result is: ", None)
            token = tokens[i]
            if token in operators:
                if len(st)==1:
                    num1 = int(st.popleft())
                    print("Num1: ", [num1])
                    result = self.operate(result, num1, token)
                    print("operation result with result: ", result)
                
                else:
                    num1 = int(st.popleft())
                    num2 = int(st.popleft())
                    print("Num1, num2: ", [num1, num2])
                    result = self.operate(num1, num2, token)
                    
                    print("operation result with result: ", result)
            else:
                st.append(token)
            
            i+=1
            
        return result
        '''
