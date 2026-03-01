
from instagram import Instagram
insta = Instagram()

try:
    insta.login()
    insta.search_page()
    insta.find_followers()
except Exception as e:
    print(f"{e}")
finally:
    insta.driver.quit()