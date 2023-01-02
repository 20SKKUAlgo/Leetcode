class Solution:
    def calPoints(self, operations: List[str]) -> int:
        i=0
        num=len(operations)
        res=[]
        while i < num:
            op = operations.pop(0) # first element
            if op ==  "C":
                res.pop()
            elif op == "D":
                res.append(int(res[-1])*2)
            elif op == "+":
                res.append(int(res[-1])+int(res[-2]))
            else:
                res.append(op)

            i=i+1

        return sum(map(int,res))
