function solution(n) {
    const arr = Array(n).fill().map((v, i) => i+1)
    console.log(arr)
    let sum = 0
    
    if (n % 2 == 1){
        // 홀수인 경우에
        const newArr = arr.filter((num) => num % 2 == 1)
        newArr.forEach((num)=> sum += num)
        return sum
    }else{
        const newArr = arr.filter((num) => num % 2 == 0)
        newArr.forEach((num)=> sum += num**2)
        return sum
    }
    
    
}