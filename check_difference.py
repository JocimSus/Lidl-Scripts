# Check for difference
# Use case:
# 1. Check for hash file sums
from difflib import ndiff as _a
def _1():
    _2=type('',(),{})()
    _2._3=[lambda _4:setattr(_2,'_5',_4) or _4]
    _2._6=[lambda _7:setattr(_2,'_8',_7) or _7]
    _2._9=[lambda _10,_11:setattr(_2,'_12',_10==_11) or setattr(_2,'_13',_10) or setattr(_2,'_14',_11)]
    _2._15=[lambda:_2._13 if _2._12 else print(f'{_2._14}=>{_2._13}') or list(map(lambda _16:_17(_16[0],_16[1],_2._13,_2._14),enumerate(_a(_2._13,_2._14))))]
    _2._18=[lambda:input("return")]
    def _19(_20,_21):
        while True:
            _22=input(_20).strip()
            if _22:return _21[0](_22)
            print("null")
    def _17(_23,_24,_25,_26):
        if _24[0]==' ':return
        elif _24[0]=='-':print(f'del "{_24[-1]}" from {_23}')
        elif _24[0]=='+':print(f'add "{_24[-1]}" to {_23}')
    _19("target ",_2._3)
    _19("base ",_2._6)
    _2._9[0](_2._5,_2._8)
    _2._15[0]()
    _2._18[0]()
_1()
