def solution(id_pw, db):
    answer = 'fail'
    
    id = id_pw[0]
    password = id_pw[1]
        
    for d in db:
        if d[0] == id:
            if d[1] == password:
                answer = 'login'
            else:
                answer = 'wrong pw'
    
    return answer