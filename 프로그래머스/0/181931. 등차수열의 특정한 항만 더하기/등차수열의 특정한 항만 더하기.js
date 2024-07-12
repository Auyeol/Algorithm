function solution(a, d, included) {
    // 첫째항이 a, 공차가 d인 등차수열
    // 이 등차수열의 1항부터 n항까지 included가 ture인 항들만 더한 값을 return 
    let arr = Array(included.length).fill(a).map((num, idx)=>{
        return num + d * idx
    })
    let sum = 0
    
    for (let i=0;i<included.length;i++){
        included[i]? sum += arr[i] : null  
    }
    
    return sum 


    
}