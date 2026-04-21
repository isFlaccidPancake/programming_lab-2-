_1_val = int(input())
_2_val = int(input())
_3_val = int(input())

if (_1_val < _2_val and _1_val > _3_val) or (_1_val < _3_val and _1_val > _2_val):
    med_val = _1_val
elif (_2_val < _1_val and _2_val > _3_val) or (_2_val < _3_val and _2_val > _1_val):
    med_val = _2_val
elif (_3_val < _1_val and _3_val > _2_val) or (_3_val < _2_val and _3_val > _1_val):
    med_val = _3_val

print(med_val)
input()