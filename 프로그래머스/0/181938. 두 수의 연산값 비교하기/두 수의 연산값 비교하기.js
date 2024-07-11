function solution(a, b) {
    r1 = Number(String(a) + String(b))
    r2 = 2 * a * b
    
    return Math.max(r1, r2)
}