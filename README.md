# scrapy tutorial

## 스크래피 도움말의 모든 코드 크롤링 하기

- 서핑을 통해 학습하는 것도 좋지만 도움말 페이지를 통해 학습하는 게 더 좋다.
- [스크래피 문서](https://docs.scrapy.org/en/latest/index.html)에 나온 코드를 실행 및 학습 후 매커니즘을 어느정도 파악했다.
- 한 프로젝트에 크롤러를 여러개 만들 수 있으며 이는 스크래피에서 스파이더라 한다.
- 데이터형 파일(csv, xml, json, jsonl, ...)을 settings.py에서 쉽게 만들 수 있다.
- 기타 파일(html, md, ...)은 pipelines.py에서 클래스를 만들어서 만들 수 있다.

---

## 스크래피 사용환경 준비

### 파이썬 설치

- [파이썬 설치](https://www.python.org/downloads) 3.10 권장(3.11 scrapy 설치 불안정 2022-11-15 확인)
- 파이썬 환경변수 등록
- 파이썬 설치 위치 파악
- [윈도우 + S]: 환경 변수(시스템 환경 변수 편집)
- 시스템 속성 - 고급 - [환경 변수]
- 시스템 변수 - "Path"(선택) - [편집] - [새로 만들기]
- (아래와 유사한 경로를 추가)
- C:\Program Files\Python310
- C:\Users\Admin\AppData\Roaming\Python\Python310\Scripts
- %AppData%\Python\Python310\Scripts

### 스크래피 설치

```shell
:: [윈도우 + S]: cmd(명령 프롬프트) + [Enter]

:: 현재 설치된 모듈 보기
py -m pip freeze

:: 모듈 기록
py -m pip freeze > requirements.txt

:: 설치 모듈 업그레이드
py -m pip install --upgrade pip

:: 모듈 초기화
py -m pip uninstall -y -r requirements.txt

:: 모듈 설치
py -m pip install scrapy
py -m pip install scrapy-fake-useragent
py -m pip install scrapy-playwright
py -m pip install beautifulsoup4
py -m pip install selenium
py -m pip install webdriver-manager
py -m pip freeze > requirements.txt

:: 모듈 확인
py --version
py -m pip --version
py -m pip list
```

### 스크래피 프로젝트 생성 및 스파이더(크롤러) 템플릿 생성

```shell
:: [윈도우 + S]: cmd(명령 프롬프트) + [Enter]

c:
cd\
mkdir scrapys
cd scrapys

scrapy startproject tutorial
cd tutorial

scrapy genspider -t basic Basic quotes.toscrape.com
scrapy genspider -t crawl CrawlJs quotes.toscrape.com/js
scrapy genspider -t crawl CrawlPage quotes.toscrape.com/page/1
scrapy genspider -t crawl CrawlScroll quotes.toscrape.com/scroll
:: scrapy genspider -t csvfeed Csvfeed quotes.toscrape.com
:: scrapy genspider -t xmlfeed Xmlfeed quotes.toscrape.com
code .
```

### 파이썬 부록_가상환경

```shell
:: 파이썬 가상환경 설치 - 이름: projects
py -m venv projects

:: 가상환경 들어가기
projects\Scripts\activate.bat

:: 가상환경 나오기
projects\Scripts\deactivate.bat
```
