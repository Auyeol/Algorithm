function solution(num_str) {
    const arr = [...num_str]
    let sum = 0
    arr.forEach((num)=>{
        sum += Number(num)
    })
    
    return sum
}