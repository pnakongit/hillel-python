# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python
"""
How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

"""


def rot13(message):
    result = ''
    for i in message:
        ord_i = ord(i)
        if 97 <= ord_i <= 109 or 65 <= ord_i <= 77:
            result += chr(ord_i + 13)
        elif 110 <= ord_i <= 122 or 78 <= ord_i <= 90:
            result += chr(ord_i - 13)
        else:
            result += i

    return result


assert (rot13("EBG13 rknzcyr.") == "ROT13 example.")
assert (rot13(
    "How can you tell an extrovert from an\n"
    "introvert at NSA? Va gur ryringbef,\n"
    "gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.") ==
        "Ubj pna lbh gryy na rkgebireg sebz na\n"
        "vagebireg ng AFN? In the elevators,\n"
        "the extrovert looks at the OTHER guy's shoes.")
assert (rot13("123") == "123")
assert (rot13(
    "Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)") ==
        "This is actually the first kata I ever made. Thanks for finishing it! :)")
assert (rot13("@[`{") == "@[`{")

print('SUCCESS')
