from texting import CO

from pyspare.enum.brackets import BRK
from pyspare.lines import liner

candidates = {
    'cities': ['paris', 'london', 'tokyo', 'delhi', 'vienna']
}


def test():
    for key, vec in candidates.items():
        print(key)
        joined = liner(vec, delim=CO, level=0, bracket=BRK, discrete=False)
        print('result:', joined)
        # print(LF.join(['\'' + word + '\'' for word in padded]))


test()
