"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []

    for i in range(5, -1, -1):
        result.append(i)

    return result  

print("fn_hack_7() ",fn_hack_7())