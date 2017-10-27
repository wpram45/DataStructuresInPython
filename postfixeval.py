def postfix_evaluation(s):
    s=s.split()
    n=len(s)
    stack =[]
    for i in range(n):
        if s[i].isdigit():
          #append function is equivalent to push
            stack.append(int(s[i]))
        elif s[i]=="+":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)+int(b))
        elif s[i]=="*":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)*int(b))
        elif s[i]=="/":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)/int(a))
        elif s[i]=="-":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)-int(a))
             
    return stack.pop()
 
#space separtor is required , for solving 2 or more digits .
s=" 5 3 2 - / 4 7 * +"
val=postfix_evaluation(s)
print(val)