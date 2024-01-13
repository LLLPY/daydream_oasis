export function decodeByteString(byteString) {
    // 解析byte
    const byteArray = new Uint8Array(byteString.match(/\\x[0-9a-f]{2}/g).map(x => parseInt(x.substring(2), 16)));
    const decoder = new TextDecoder('utf-8');
    return decoder.decode(byteArray);
}


export function get_cookie(key) {
    let val = ''
    let cookie_arr = document.cookie.split(';')
    for (let i = 0; i < cookie_arr.length; i++) {
        let item = cookie_arr[i].split('=')
        if (item[0].trim() === key) {
            val = item[1]
            break
        }
    }
    return val
}
