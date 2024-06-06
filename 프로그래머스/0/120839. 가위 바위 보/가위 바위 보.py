def solution(rsp):
    rsp_dict = {'2':'0','0':'5','5':'2'}
    result = ''
    for d in rsp:
        result += rsp_dict[d]
    
    return result