function solution(code) {
    let ret = ''
    // mode에 따라 문자열 ret을 만들어낸다.
    let mode = false
    for (let i=0;i<code.length;i++){
        if (code[i] == '1'){
            mode = !mode
            continue
        }
        
        if (mode == 0 && (i % 2 == 0)){
            ret = ret + code[i]
        }else if(mode == 1 && (i % 2 == 1)){
            ret = ret + code[i]
        }
        
    }
     
    if (ret.length == 0){
        return "EMPTY"
    }else{
        return ret
    }
}