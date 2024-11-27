"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"

    caracteres = {'o': '0', 'i': '1', 'a': '@'}
    newResult = lambda out: ''.join(caracteres.get(c, c) for c in out)

    return list(newResult(result).upper())


print("fn_hack_10(): ", fn_hack_10())