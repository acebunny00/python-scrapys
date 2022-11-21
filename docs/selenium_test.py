from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# WINDOW_SIZE = "1920,1080"
# chrome_options = Options()
# chrome_options.add_argument( "--headless" )		# 크롬창이 열리지 않음
# chrome_options.add_argument( "--no-sandbox" )		# GUI를 사용할 수 없는 환경에서 설정, linux, docker 등
# chrome_options.add_argument( "--disable-gpu" )	# GUI를 사용할 수 없는 환경에서 설정, linux, docker 등
# chrome_options.add_argument( f"--window-size={ WINDOW_SIZE }" )
# chrome_options.add_argument( "Content-Type=application/json; charset=utf-8" )
# driver = webdriver.Chrome( ChromeDriverManager().install(), chrome_options=chrome_options )

driver = webdriver.Chrome( ChromeDriverManager().install() )
driver.get( "https://quotes.toscrape.com" )
