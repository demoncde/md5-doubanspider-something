from PIL import Image
import pytesseract
import requests


cookies = {
    "bid":"krcnFrbL9dw",
    "douban-fav-remind":"1",
    "__gads":"ID=851f9d3bc3f7e01f:T=1574288062:S=ALNI_MZHUww8i58N2tk8bFxbD_Xp9zOYkA",
    "ll":"\"118123\"",
    "__yadk_uid":"9VmZTFStieakW9L7nf0AXH0FOtxCnLc0",
    "_vwo_uuid_v2":"D9D09EBB03960548BBD50C7DC9E34823E|ae3bc3b5e57f2bef36baaa95e88fe5e6",
    "push_doumail_num":"0",
    "__utmv":"30149280.5695",
    "douban-profile-remind":"1",
    "__utmz":"30149280.1599142153.6.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
    "__utmc":"30149280",
    "ck":"VxIE",
    "ap_v":"0,6.0",
    "push_noty_num":"1",
    "_pk_ref.100001.8cb4":"%5B%22%22%2C%22%22%2C1601911139%2C%22https%3A%2F%2Fsite.douban.com%2F150757%2Froom%2F1603912%2F%22%5D",
    "_pk_ses.100001.8cb4":"*",
    "__utma":"30149280.983759122.1574288063.1601907534.1601911141.10",
    "__utmt":"1",
    "__utmb":"30149280.1.10.1601911141",
    "_pk_id.100001.8cb4":"3071abd5f9eac3cd.1574288062.9.1601911143.1601908387.",
    "dbcl2":"\"56952656:9vCTEApXqf4\""
}

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}



# 容错最大的有色判断
MAX_RGB_VALUE = 20
# 噪点大小
MAX_NOISY_COUNT = 25

# RGBA白色定义
WHITE_COLOR = (255, 255, 255, 255)
# RGBA黑色定义
BLACK_COLOR = (0, 0, 0, 255)


def print_char_pic(width, height, s_data):
    """
    画出字符图, 空格为白色, 点为黑色
    """
    _pic_str = ''
    for y in range(0, height):
        for x in range(0, width):
            _point = s_data[y * width + x]
            if _point == WHITE_COLOR:
                _pic_str += ' '
            else:
                _pic_str += '*'
        _pic_str += '\n'

    print(_pic_str)


def gen_white_black_points(image):
    """
    根据点阵颜色强制转换黑白点
    """
    data = image.getdata()
    new_data = []
    for item in data:
        if item[0] > MAX_RGB_VALUE and item[1] > MAX_RGB_VALUE and item[2] > MAX_RGB_VALUE:
            new_data.append(WHITE_COLOR)
        else:
            new_data.append(BLACK_COLOR)
    return new_data


def reduce_noisy(width, height, points):
    """
    横向扫描, 获取最大边界大小. 除去小于最大噪点大小的面积.
    """
    # 标记位置, 初始化都是0, 未遍历过
    flag_list = []
    for i in range(width * height):
        flag_list.append(0)

    # 遍历
    for index, value in enumerate(points):
        _y = index // width
        _x = index - _y * width
        # print _x, _y
        if flag_list[index] == 0 and value == BLACK_COLOR:
            flag_list[index] = 1
            _tmp_list = [index]
            recursion_scan_black_point(_x, _y, width, height, _tmp_list, flag_list, points)
            if len(_tmp_list) <= MAX_NOISY_COUNT:
                for x in _tmp_list:
                    points[x] = WHITE_COLOR

        else:
            flag_list[index] = 1


def recursion_scan_black_point(x, y, width, height, tmp_list, flag_list, points):
    # 左上
    if 0 <= (x - 1) < width and 0 <= (y - 1) < height:
        _x = x - 1
        _y = y - 1
        _inner_recursion(_x, _y, width, height, tmp_list, flag_list, points)

    # 上
    if 0 <= (y - 1) < height:
        _x = x
        _y = y - 1
        _inner_recursion(_x, _y, width, height, tmp_list, flag_list, points)

    # 右上
    if 0 <= (x + 1) < width and 0 <= (y - 1) < height:
        _x = x + 1
        _y = y - 1
        _inner_recursion(_x, _y, width, height, tmp_list, flag_list, points)

    # 左
    if 0 <= (x - 1) < width:
        _x = x - 1
        _y = y
        _inner_recursion(_x, _y, width, height, tmp_list, flag_list, points)

    # 右
    if 0 <= (x + 1) < width:
        _x = x + 1
        _y = y
        _inner_recursion(_x, _y, width, height, tmp_list, flag_list, points)

    # 左下
    if 0 <= (x - 1) < width and 0 <= (y + 1) < height:
        _x = x - 1
        _y = y + 1
        _inner_recursion(_x, _y, width, height, tmp_list, flag_list, points)

    # 下
    if 0 <= (y + 1) < height:
        _x = x
        _y = y + 1
        _inner_recursion(_x, _y, width, height, tmp_list, flag_list, points)

    # 右下
    if 0 <= (x + 1) < width and 0 <= (y + 1) < height:
        _x = x + 1
        _y = y + 1
        _inner_recursion(_x, _y, width, height, tmp_list, flag_list, points)


def _inner_recursion(new_x, new_y, width, height, tmp_list, flag_list, points):
    _index = new_x + width * new_y
    if flag_list[_index] == 0 and points[_index] == BLACK_COLOR:
        tmp_list.append(_index)
        flag_list[_index] = 1
        recursion_scan_black_point(new_x, new_y, width, height, tmp_list, flag_list, points)
    else:
        flag_list[_index] = 1

def recognize_url(url):
    # group_info = requests.get(url, headers=headers, cookies = cookies)
    # with open("tmp.png", 'wb') as fd:
    #     for chunk in group_info.iter_content(chunk_size=128):
    #         fd.write(chunk)
    # img = Image.open('tmp.png')
    # img = img.convert('RGBA')
    # w, h = img.size[0], img.size[1]
    # print(w, h)
    # point_list = gen_white_black_points(img)
    # # print_char_pic(w, h, point_list)
    # reduce_noisy(w, h, point_list)
    #
    # img.putdata(point_list)
    # img.save("rebuild.png")

    return pytesseract.image_to_string(Image.open('tmp.png'))

if __name__ == '__main__':
    # img = Image.open('imgs/captcha-1.jpg')
    # img = img.convert('RGBA')
    # w, h = img.size[0], img.size[1]
    # print w, h
    # point_list = gen_white_black_points(img)
    # print_char_pic(w, h, point_list)
    # reduce_noisy(w, h, point_list)
    # print_char_pic(w, h, point_list)
    #
    #
    # img.putdata(point_list)
    # img.save("imgs/rebuild.jpg")
    #
    # print pytesseract.image_to_string(Image.open('imgs/rebuild.jpg')

    print(recognize_url('https://www.douban.com/misc/captcha?id=JtYtZnuw31nOQ1LQZfZ07Ki0:en'))