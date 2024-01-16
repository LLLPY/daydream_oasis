import requests


def transform_link():
    '''替换文章中的外链图片'''
    headers = {
        'cookie': 'auth_token=310a8eab2346e3004fe0dc37765de31754f8e6890ab406ba4edbab94ce2cf155:1rPYWL:Tecy87to3sbJ1AzzImmHDkmknHAMRuRl0dhkMmtZNZ8; expires=Tue, 23 Jan 2024 01:45:41 GMT; Max-Age=604800; Path=/'
                  'content'
    }

    url = 'http://www.lll.plus/api/file/upload/'
    f = open('../media/image/2023/12/23/Snipaste_2023-12-23_17-25-36.443288b6a1a411ee971faa46512614f5.png', 'rb')
    res = requests.post(url, files={'file': ('a.png', f, 'image')}, headers=headers)
    print(res.json())


if __name__ == '__main__':
    transform_link()
