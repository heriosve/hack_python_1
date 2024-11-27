"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"

    caracteres = {'o': '0', 'i': '1', 'a': '@'}

    newResult = lambda out: ''.join(caracteres.get(c, c) for c in out)

    return newResult(result)

print("fn_hack_5: ", fn_hack_5())