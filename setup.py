from setuptools import setup

APP = ['pomodoro.py']
OPTIONS = {
    'argv_emulation': False,  # 关键：避免后台进程被阻塞
    'plist': {
        'LSUIElement': True,  # 关键：隐藏 Dock 图标，纯菜单栏应用
    }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)

# terminal:
# $ python setup.py py2app -A

