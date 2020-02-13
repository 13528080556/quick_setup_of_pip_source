# @Time    : 2020/1/23 11:58
# @Author  : Hugh
# @Email   : 609799548@qq.com

import os
import sys

WIN = sys.platform.startswith('win')

mirrors = {

    "qinghua": ['[global]', 'index-url = https://pypi.tuna.tsinghua.edu.cn/simple',
                '[install]', 'trusted-host=pypi.tuna.tsinghua.edu.cn'],
    'aliyun': ['[global]', 'index-url = http://mirrors.aliyun.com/pypi/simple/',
               '[install]', 'trusted-host=mirrors.aliyun.com'],
    'douban': ['[global]', 'index-url = https://pypi.doubanio.com/simple/',
               '[install]', 'trusted-host=pypi.doubanio.com']
}


def main(mirror):
    user_home = os.path.expanduser('~')

    if WIN:
        pip_dir = os.path.join(user_home, 'pip')
        pip_ini = os.path.join(pip_dir, 'pip.ini')
    else:
        pip_dir = os.path.join(user_home, '.pip')
        pip_ini = os.path.join(user_home, 'pip.conf')

    if not os.path.exists(pip_dir):
        os.mkdir(pip_dir)

    with open(pip_ini, 'w') as f:

        raw_content = mirrors[mirror]
        content = [item + '\n' for item in raw_content]
        f.writelines(content)

    print('设置成功')


if __name__ == '__main__':
    print('请选择国内镜像源（输入序号）\n1、清华源\n2、阿里云源\n3、豆瓣源')
    while True:
        num = input('在这后面输入：')
        if num in '123':
            if num == '1':
                opt = 'qinghua'
            elif num == '2':
                opt = 'aliyun'
            else:
                opt = 'douban'
        else:
            print('由于你选择的序号不符合规格，默认为你设置为清华源，如需重新修改，请重新执行该文件')
            opt = 'qinghua'
        print('------------------------------------------------------------------------')
        break

    main(opt)
