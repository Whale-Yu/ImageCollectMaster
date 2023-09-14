from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'packages': ['PySide6', 'requests'],
        'include_files': ['bug.ico']
    }
}

# TARGET
executables = [
    Executable('../main.py', base='Win32GUI')
]

# SETUP CX FREEZE
setup(
    name="百度图片采集器",
    version="1.0",
    description="百度图片采集器-基于master分支添加了GUI界面",
    author="yujunyu",
    options=options,
    executables=executables
)
