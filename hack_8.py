"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]

    return result[1:-1]  

print("fn_hack_8() ", fn_hack_8())