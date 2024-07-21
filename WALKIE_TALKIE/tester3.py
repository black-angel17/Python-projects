from selenium import webdriver

# Create a WebDriver instance (e.g., Firefox)
driver = webdriver.Firefox()

# Open a webpage
driver.get("https://example.com")

# Add a new cookie
#new_cookie = {'name': 'my_cookie', 'value': '12345'}
#driver.add_cookie(new_cookie)

# Get all cookies
cookies = driver.get_cookies()

# Print the cookies
print("All Cookies:")
for cookie in cookies:
    print(f"{cookie['name']}: {cookie['value']}")

# Delete a cookie by name
#driver.delete_cookie('my_cookie')

# Get updated cookies after deletion
cookies = driver.get_cookies()

# Print the updated cookies
'''print("\nCookies after deletion:")
for cookie in cookies:
    print(f"{cookie['name']}: {cookie['value']}")'''

# Close the browser
#driver.quit()

