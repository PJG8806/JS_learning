import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import sqlite3

# (TODO)데이터베이스 테이블 생성 함수
def create_table():
    # TODO: SQLite에 연결하고 products 테이블 생성
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS products(id INTEGER primary key AUTOINCREMENT, category VARCHAR(40), brand VARCHAR(40), product_name VARCHAR(40), price VARCHAR(40))")
    conn.commit()
    conn.close()
        

# (TODO)데이터 저장 함수 
def save_to_db(category, brand, product_name, price):
    # TODO: DB 연결 -> 커서 생성 -> INSERT 실행 -> 커밋 및 종료
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products(category, brand, product_name, price) VALUES(?,?,?,?)", (category, brand, product_name, price))
    conn.commit()
    conn.close()

# 드라이버 설정 함수
def setup_driver():
    header_user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    options_ = Options()
    options_.add_argument(f"User-Agent={header_user}")
    # options_.add_argument("--headless=new")
    # options_.add_experimental_option("detach", True)  # 브라우저 종료 안함 (디버깅용)
    options_.add_experimental_option('excludeSwitches', ["enable-logging"])  # 불필요한 로그 제거
    return webdriver.Chrome(options=options_)

# 상품 검색 함수
def search_product(driver, keyword):
    driver.get("https://kream.co.kr/")
    
    time.sleep(1.5)

    # 1. 검색 버튼 클릭
    wait = WebDriverWait(driver, 15)
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin")))
    search_button.click()

    time.sleep(1.5)

    # 2. 검색어 입력
    search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus")))
    search_input.clear()
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.ENTER)

    # 3. 페이지 다운 20번 반복
    for _ in range(20):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

# (TODO)상품 정보 추출 함수
def extract_product_info(soup, category):
    # TODO: 제품 정보 추출 (브랜드, 제품명, 가격) 후 카테고리, 브랜드, 제품명, 가격 print -> DB 저장
    select = soup.select(".product_card")
    for i in select:
        tab = i.select(".text_body p")
        
        product_name = tab[1].get_text(strip=True)
        brand = tab[0].get_text(strip=True)
        price = tab[2].get_text(strip=True)
        save_to_db(str(category), brand, product_name, price)

#저장한 데이터 전체 출력
def select_all():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def main():
    create_table()
    categories = ["상의", "하의", "신발", "패션잡화"]
    driver = setup_driver()

    for category in categories:
        print(f"===== '{category}' 카테고리 검색 시작 =====")
        search_product(driver, category)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        extract_product_info(soup, category)
        print()

    driver.quit()
    
if __name__ == "__main__":
    main()