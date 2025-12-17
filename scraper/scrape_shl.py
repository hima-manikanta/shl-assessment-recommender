from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

URL = "https://www.shl.com/solutions/products/product-catalog/"

def scroll_page(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(URL)
    time.sleep(5)

    # Force-load all cards
    scroll_page(driver)
    time.sleep(3)

    cards = driver.find_elements(
        By.XPATH,
        "//a[contains(@href,'/products/') and contains(@class,'card')]"
    )

    data = []
    seen = set()

    for c in cards:
        link = c.get_attribute("href")
        name = c.text.strip()

        if not name:
            continue
        if "job" in name.lower():
            continue
        if link in seen:
            continue

        seen.add(link)
        data.append({
            "assessment_name": name,
            "url": link,
            "description": "",
            "test_type": "K",
            "category": "General"
        })

    driver.quit()

    df = pd.DataFrame(data)
    df = df.drop_duplicates(subset=["assessment_name"])
    df.to_csv("data/shl_catalog.csv", index=False)

    print("✅ Total assessments:", len(df))


if __name__ == "__main__":
    main()
