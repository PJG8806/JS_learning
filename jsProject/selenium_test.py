import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 옵션
options = Options()
options.add_argument("--start-mine")  # 창 최대화
# options.add_argument("--headless")       # 창 안 보이게 실행 (서버용)

driver = webdriver.Chrome(options=options)

driver.get("https://kream.co.kr/")


wait = WebDriverWait(driver, 10)
time.sleep(1.5)

search_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin"))).click()

time.sleep(1.5)


list_value = ["상의", "하의", "신발", "패션잡화"]
for i in list_value:
    time.sleep(1.5)
    search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus")))

    search_input.clear()
    print(i)
    search_input.clear()
    search_input.send_keys(i)
    search_input.send_keys(Keys.ENTER)

    time.sleep(1.5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    for _ in range(20):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

    select = soup.select(".product_card")

    for i in select:
        tab = i.select(".text_body")
        print(tab[1].get_text(strip=True))
        print()

# 종료
driver.quit()
