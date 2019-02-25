import math

num = '9625635'

def find_min(num):
    final_str = ''
    x = None
    if len(num) == 1:
        return num
    else:
        temp_st = num
        for i in range(len(num)):
            if min(temp_st) != temp_st[0]:
                x = temp_st.rfind(min(temp_st))
                temp_0 = temp_st[0]
                temp_x = temp_st[x]
                break
            else:
                final_str += temp_st[0]
                temp_st = temp_st[1:]
        if x is not None:
            final_str += temp_st[x]
            final_str += temp_st[1:x]
            final_str += temp_st[0]
            final_str += temp_st[x+1:]
    return final_str


print(find_min('811111111112'))





