from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Cấu hình Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Khởi tạo WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.flipkart.com/q/smart-watches?otracker=undefined_footer_footer&page=1")

# #Tìm Tất cả sản phầm 
# products = driver.find_elements(By.CSS_SELECTOR, "div._75nlfW.LYgYA3 > div[style*='width: 25%']")

# for product in products:
#     # print(product.text)
#     # for product in products:
#     try:
#         name = product.find_element(By.CLASS_NAME, "WKTcLC").text
#     except:
#         name = "N/A"

#     try:
#         price = product.find_element(By.CLASS_NAME, "Nx9bqj").text
#     except:
#         price = "N/A"

#     try:
#         mrp = product.find_element(By.CLASS_NAME, "yRaY8j").text
#     except:
#         mrp = "N/A"

#     try:
#         discount = product.find_element(By.CLASS_NAME, "UkUFwK").text
#     except:
#         discount = "N/A"

#     try:
#         delivery = product.find_element(By.CLASS_NAME, "yiggsN").text
#     except:
#         delivery = "N/A"

#     try:
#         ratings = product.find_element(By.XPATH, ".//span[contains(text(),'Ratings')]").text
#     except:
#         ratings = "N/A"

#     try:
#         reviews = product.find_element(By.XPATH, ".//span[contains(text(),'Reviews')]").text
#     except:
#         reviews = "N/A"

#     # Chỉ in nếu có ít nhất tên và giá
#     if name != "N/A" and price != "N/A":
#         print(f"{name} | {price} | {mrp} | {discount} | {delivery} | {ratings} | {reviews}")
#     else:
#         print("Thiếu dữ liệu quan trọng, bỏ qua 1 sản phẩm")
#         continue
#     # try:
#     #     name = product.find_element(By.CLASS_NAME, "WKTcLC").text
#     #     price = product.find_element(By.CLASS_NAME, "Nx9bqj").text
#     #     mrp = product.find_element(By.CLASS_NAME, "yRaY8j").text
#     #     discount = product.find_element(By.CLASS_NAME, "UkUFwK").text
#     #     delivery = product.find_element(By.CLASS_NAME, "yiggsN").text
#     #     ratings = product.find_element(By.XPATH, ".//span[contains(text(),'Ratings')]").text
#     #     reviews = product.find_element(By.XPATH, ".//span[contains(text(),'Reviews')]").text

#     #     print(f"{name} | {price} | {mrp} | {discount} | {delivery} | {ratings} | {reviews}")

#     # except Exception as e:
#     #     # Một số sản phẩm không có đủ thông tin (ví dụ không có discount hay reviews), nên bỏ qua
#     #     print("Thiếu dữ liệu, bỏ qua 1 sản phẩm")
#     #     continue

# # watch_name_element = driver.find_element(By.CLASS_NAME , "WKTcLC")
# # watch_name = watch_name_element.text

# # current_price = driver.find_element(By.CLASS_NAME, "Nx9bqj")
# # current_price = current_price.text

# # mrp_price_element = driver.find_element(By.CLASS_NAME , "yRaY8j")
# # mrp_price = mrp_price_element.text

# # discount_element = driver.find_element(By.CLASS_NAME , "UkUFwK")
# # discount = discount_element.text

# # delivery_charge_element = driver.find_element(By.CLASS_NAME , "yiggsN")
# # delivery_charge = delivery_charge_element.text 

# # #stars_element = driver.find_element(By.CLASS_NAME , "XQDdHH")
# # stars_element = driver.find_element(By.XPATH, "//span[contains(text(),'Ratings')]")
# # stars = stars_element.text 

# # review_element = driver.find_element(By.XPATH , "//span[contains(text(),'Reviews')]")
# # review = review_element.text
# # print("____________________________________________________")
# # print("Watch name = " , watch_name)
# # print("Current Price = ", current_price)
# # print("MRP Price = " , mrp_price)
# # print("Discount = " , discount)
# # print("delivery_charge = " , delivery_charge)
# # print("Stars= " , stars)
# # print("Review = " , review)

# # print("_____________________________________________________")
# #print(products)
# next_page_element = driver.find_element(By.XPATH , '//a[@class="_9QVEpD"]/span[text()="Next"]' )
# next_page = next_page_element.click()
# Khởi tạo danh sách để lưu dữ liệu
watch_name = []
current_price = []
mrp_price = []
discounts = []
delivery_charge = []
stars = []
rating = []
review = []

# Duyệt 8 trang đầu
for i in range(1, 9):
    print(f"\n--- Đang xử lý Trang {i} ---\n")
    
    try:
        products = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._75nlfW.LYgYA3 > div[style*='width: 25%']"))
        )
    except Exception as e:
        print(f"Lỗi khi tải sản phẩm trên trang {i}: {e}")
        break

    for idx, product in enumerate(products):
        try:
            name = product.find_element(By.CLASS_NAME, "WKTcLC").text
        except:
            name = "N/A"

        try:
            price = product.find_element(By.CLASS_NAME, "Nx9bqj").text
        except:
            price = "N/A"

        try:
            mrp = product.find_element(By.CLASS_NAME, "yRaY8j").text
        except:
            mrp = "N/A"

        try:
            dis = product.find_element(By.CLASS_NAME, "UkUFwK").text
        except:
            dis = "N/A"

        try:
            delivery = product.find_element(By.CLASS_NAME, "yiggsN").text
        except:
            delivery = "N/A"

        try:
            link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            link = None

        star = "N/A"
        rating_detail = "N/A"
        review_detail = "N/A"

        if name != "N/A" and price != "N/A" and link:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(link)
            time.sleep(2) 

            try:
                star = driver.find_element(By.CLASS_NAME, "XQDdHH").text
            except:
                star = "N/A"

            try:
                ratings = driver.find_element(By.XPATH, "//span[contains(text(), 'Ratings')]").text
                rating_detail = ratings
            except:
                rating_detail = "N/A"

            try:
                reviews = driver.find_element(By.XPATH, "//span[contains(text(), 'Reviews')]").text
                review_detail = reviews
            except:
                review_detail = "N/A"

            # Đóng tab chi tiết và quay lại tab chính
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            watch_name.append(name)
            current_price.append(price)
            mrp_price.append(mrp)
            discounts.append(dis)
            delivery_charge.append(delivery)
            stars.append(star)
            rating.append(rating_detail)
            review.append(review_detail)
        else:
            print(f"Bỏ qua sản phẩm {idx+1} vì thiếu dữ liệu hoặc link lỗi.")

    # Chuyển sang trang tiếp theo
    try:
        print("tìm nút Next")
        next_page_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="_9QVEpD" and span[contains(text(), "Next") or contains(text(), "next")]]'))
        )
        print(" tìm thấy nút Next, đang nhấn")
        next_page_element.click()
        time.sleep(3)  # Đợi trang mới tải
    except Exception as e:
        print("Không tìm thấy nút Next hoặc lỗi khi click:", str(e))
        break

# Đóng driver khi xong
driver.quit()

# Xuất dữ liệu ra CSV
data = {
    "Name": watch_name,
    "Current Price": current_price,
    "MRP": mrp_price,
    "Discount": discounts,
    "Delivery": delivery_charge,
    "Stars": stars,
    "Rating": rating,
    "Reviews": review
}

df = pd.DataFrame(data)
df.to_csv("flipkart_watches.csv", index=False)
print("Done")