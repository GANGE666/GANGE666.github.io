target =[
    0x17e8ba3b95cb36e9,
    0x5eb83e8108340e27,
    0x298bb3acedff4e49,
    0xed57a654e66e84c5,
]

import gmpy2
e = 9533
fi_n = 2**63
print gmpy2.invert(e, fi_n)
# 3149278923734637077

key = 3149278923734637077

for i in range(4):
    print pow(target[i], key, 1 << 64)

"""
9997764242830658953
13181961895445880007
10486649486922394729
13099406429414088373

bytectf{3c508d1b7ecf514e2442609ba1bb72dc}
"""