::::::::::::::::::::::::::::::::
:::: 파이썬 업데이터 업그레이드
:::: py = python
:::: pip = package installer for Python
::::::::::::::::::::::::::::::::
py -m pip install --upgrade pip

::::::::::::::::::::::::::::::::
:::: 가상 환경 만들기 / 활성화 / 비활성화 / 제거
::::::::::::::::::::::::::::::::
py -m venv %HomePath%\venv\scrapy
:: %HomePath%\venv\scrapy\scripts\activate.bat
:: %HomePath%\venv\scrapy\scripts\deactivate.bat
:: rmdir /s /q %HomePath%\venv\scrapy

::::::::::::::::::::::::::::::::
:::: 가상 환경에 크롤링 모듈 설치
::::::::::::::::::::::::::::::::
%HomePath%\venv\scrapy\scripts\activate
py -m pip install --upgrade pip
py -m pip install scrapy-playwright
py -m pip install scrapy-fake-useragent
py -m pip install beautifulsoup4
py -m pip install selenium
py -m pip install webdriver-manager

::::::::::::::::::::::::::::::::
:::: 크롤러 실행 파일
::::::::::::::::::::::::::::::::
:: C:\Users\Admin\venv\scrapy\scripts\python.exe
:: C:\Users\Admin\venv\scrapy\scripts\scrapy.exe

::::::::::::::::::::::::::::::::
:: 모듈 리스트 만들기 / 초기화
::::::::::::::::::::::::::::::::
py -m pip freeze > requirements.txt
:: py -m pip uninstall -y -r requirements.txt
