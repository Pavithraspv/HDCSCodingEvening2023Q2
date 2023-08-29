#checking boundary values for r ,g,b values
def boundry_check(n):
    if n<0:
        n=0
    elif n>255:
        n=255
    return n    
#converting rgb to hex values
def rgb_to_hex(r,g,b):
    r=boundry_check(r)
    g=boundry_check(g)
    b=boundry_check(b)
    #:02X is for converting decimal to 2 digit hexdecimal with pading 0,if less than 2 digit.
    return '{:02X}{:02X}{:02X}'.format(r,g,b)

#unit test case to check the input and output values
def unit_test(r,g,b,answer,preDefinedAnswer):
    if answer == preDefinedAnswer:
        print("RGB("+str(r)+","+str(g)+","+str(b)+")="+str(answer)+" is Okay")
    elif answer != preDefinedAnswer:
        print("RGB("+str(r)+","+str(g)+","+str(b)+")="+str(answer)+" is not Okay")

answer=rgb_to_hex(255,255,255)
unit_test(255,255,255,answer,"FFFFFF")
answer=rgb_to_hex(255,255,300)
unit_test(0,0,300,answer,"FFFFFF")

answer=rgb_to_hex(0,0,0)
unit_test(0,0,0,answer,"000000")
answer=rgb_to_hex(148, 0, 211)
unit_test(148, 0, 211,answer,"9400D3")


