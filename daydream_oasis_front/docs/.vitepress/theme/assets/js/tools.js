export function decodeByteString(byteString) {
  // 解析byte
  const byteArray = new Uint8Array(
    byteString
      .match(/\\x[0-9a-f]{2}/g)
      .map((x) => parseInt(x.substring(2), 16)),
  );
  const decoder = new TextDecoder("utf-8");
  return decoder.decode(byteArray);
}

export function get_cookie(key) {
  let val = "";
  let cookie_arr = document.cookie.split(";");
  for (let i = 0; i < cookie_arr.length; i++) {
    let item = cookie_arr[i].split("=");
    if (item[0].trim() === key) {
      val = item[1];
      // 判断是否是字符串
      if (val.startsWith('"') && val.endsWith('"')) {
        val = val.slice(1, item[1].length - 1);
      }
      break;
    }
  }
  return val;
}

export function goBackOrRedirect(url) {
  if (document.referrer === "" || document.referrer === window.location.href) {
    // 如果没有上一页或者上一页是当前页面，则跳转到指定页面
    window.location.href = url;
  } else {
    // 如果有上一页，则返回上一页
    window.history.back();
    window.location.reload();
  }
}

export function get_url_params() {
  // 获取博客id
  let params = {};
  let params_arr = window.location.search.replace("?", "").split("&");
  params_arr.forEach(function (param) {
    let kv = param.split("=");
    params[kv[0]] = kv[1];
  });
  return params;
}

export function ord2char(ord) {
  let ord_list = ord.split(" ");
  let res = "";
  ord_list.forEach(function (o) {
    res += String.fromCharCode(parseInt(o));
  });
  return res;
}

export function get_user_info() {
  let user_id = get_cookie("user_id");
  let username = get_cookie("username");
  let avatar = get_cookie("avatar");
  console.log(user_id);
  console.log(username);
  console.log(avatar);
  if (user_id && username && avatar) {
    return {
      user_id: user_id,
      username: ord2char(username),
      avatar: ord2char(avatar),
    };
  } else {
    return {};
  }
}
