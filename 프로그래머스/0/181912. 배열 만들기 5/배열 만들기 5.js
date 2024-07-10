function solution(intStrs, k, s, l) {
    var answer = [];
    
    intStrs.forEach((str)=>{
        let num = str.split('')
        let result = Number(num.slice(s, s+l).join(''))
        
        if (result > k){
            answer.push(result)
        }
        

    })
    
    
    return answer;
}