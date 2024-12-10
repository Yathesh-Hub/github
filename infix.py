def prec(c):
    if c in ("+","-"):
        return 1
    elif c in ("*","/"):
        return 2
    elif c=="^":
        return 3
    else:
        return 0
def infix_to_postfix(exp):
    stack=[]
    postfix=[]

    for i in range(len(exp)):
        c=exp[i]

        if ("a"<=c<="z") or ("A"<= c <="Z") or ("0"<=c<="9"):
            postfix.append(c)
        elif c=="(":
            stack.append(c)
        elif c==")":
            while stack and stack[-1]!="(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and prec(exp[i])<prec(stack[-1]):
                postfix.append(stack.pop())
            stack.append(c)
    while stack:
        postfix.append(stack.pop())
    print("".join(postfix))

exp="a+b-c*d"
infix_to_postfix(exp)