"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]

    new_result = [elemento for dupla in [[x, '@'] for x in result] for elemento in dupla]

    return new_result 

print("fn_hack_9() ", fn_hack_9())
