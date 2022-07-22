class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a=="":
            return b
        if b== "":
            return a
        
        diffa = len(a) - len(b)
        diffb = len(b) - len(a)
        if diffa>0:
            b = ("0"*diffa) + b
        elif diffb>0:
            a = ("0"*diffb) + a
        
        carry = 0
        binarySum = ""
        
        while a and b:
            
            lastA = int(a[-1])
            lastB = int(b[-1])
            
            carryOver = (lastA + lastB + carry)//2
            nextDigit = (lastA + lastB + carry)%2
            
            carry = carryOver
            binarySum += str(nextDigit)
            # print("Binary sum: ", binarySum)
            
            a = a[:-1]
            b = b[:-1]
        
        if not a and not b and carry==1:
            binarySum += str(1)
        
#         elif a:
#             if carry==1:
#                 print("there's still carry left")
#                 while a:
#                     lastA = int(a[-1])
#                     carryOver = (lastA + carry)//2
#                     nextDigit = (lastA + carry)%2
                    
#                     carry = carryOver
#                     binarySum += str(nextDigit)
#                     print("Binary sum: ", binarySum)
#                     a = a[:-1]
#                 if carry==1:
#                     binarySum += str(1)
#                     print("Adding +1 to Binary sum: ", binarySum)
#             else:
#                 binarySum += a[::-1]
#                 print("Adding +a to Binary sum: ", binarySum)
#         elif b:
#             if carry==1:
#                 print("there's still carry left")
#                 while b:
#                     lastB = int(b[-1])
#                     carryOver = (lastB + carry)//2
#                     nextDigit = (lastB + carry)%2

#                     carry = carryOver
#                     binarySum += str(nextDigit)
#                     b = b[:-1]
#                 if carry==1:
#                     binarySum += str(1)
#                     print("Adding +1 to Binary sum: ", binarySum)
                    
#             else:
#                 binarySum += b[::-1]
#                 print("Adding +b to Binary sum: ", binarySum)
            
        return binarySum[::-1]
        
