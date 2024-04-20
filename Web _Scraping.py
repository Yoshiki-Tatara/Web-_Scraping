from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome WebDriverのセットアップ
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Webページにアクセス
driver.get('https://example.com/dynamic-content')

# JavaScriptがコンテンツをロードするのを待つ
time.sleep(5)  # 実際にはより堅牢な待機方法を使用するべきです（例: WebDriverWait）

# ページからデータを抽出
elements = driver.find_elements_by_class_name('dynamic-item')
for element in elements:
    print(element.text)  # または必要なデータを取得

# ブラウザを閉じる
driver.quit()
