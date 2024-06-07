alpha_dict = {
    '0':'a','1':'b','2':'c','3':'d',
    '4':'e','5':'f','6':'g','7':'h',
    '8':'i','9':'j'
}
def solution(age):
    result = ''
    
    for a in str(age):
        result += alpha_dict[a]
    return result