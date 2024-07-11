function solution(a, b) {
    r1 = Number(String(a) + String(b))
    r2 = Number(String(b) + String(a))
    // console.log(String(a)+String(b))
    return Math.max(r1, r2)
}