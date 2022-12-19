# peak hell sounds familiar ?
# 피크 지옥이 친숙하게 들리나요?
# pronounce it
# 발음해보세요
# peekhell => 피클 pickle
# 피클 자료형 사용

import pickle

with open("./data/banner.p", "rb") as f:
    data = pickle.load(f)
print(type(data)) # type : list

for i in data :
    for x,y in i :
        print(x*y, end="")
    print()

# ans = channel