# 여러개의 Module을 모아놓은 Tool
# Python 3.3 버전 이후엔 Package Directory의 __init__.py가 없어도 됨
# 구 버전과의 호환성을 위해 만들어도 무방

import Package.Sound.echo
# 각각의 경로를 모두 입력
Package.Sound.echo.echo_test()
print()

# 특정 함수만 import
from Package.Graphic import render
render.render_test()
print()

from Package.Sound.echo import echo_test
echo_test()
print()

# alias
from Package.Graphic.render import render_test as r
r()
print()

# *
# Directory내의 모든 파일을 import
# 해당 Directory __init__.py에 __all__ 선언해줘야 함

from Package.Sound import *
echo.echo_test()
print()
