from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random
import time

# Configure Chrome to ignore SSL certificate errors
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(options=chrome_options)

driver.set_window_size(1550, 800)

driver.get("https://localhost/")

# TASK 1 ############################################################################################################

wait = WebDriverWait(driver, 10)
link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header .menu .container .top-menu #category-83 a")))
link.click()

# Wait for product list to load
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#js-product-list .products")))

visited_count = 0
product_index = 0

while visited_count < 5:
    # Re-fetch products on each iteration to avoid stale references
    products = driver.find_elements(By.CSS_SELECTOR, "#js-product-list .products .js-product")
    
    if product_index >= len(products):
        break
    
    product = products[product_index]
    
    # Check if product is out of stock
    out_of_stock = product.find_elements(By.CSS_SELECTOR, ".out_of_stock")
    
    if len(out_of_stock) == 0:  # Product is in stock
        # Find and click the product link
        product_link = product.find_element(By.TAG_NAME, "a")
        product_link.click()
        
        print(f"Visiting product {visited_count + 1}")
        
        # Wait for quantity input to be present
        quantity_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#quantity_wanted")))
        
        # Generate random quantity (1-3)
        random_quantity = random.randint(1, 3)
        driver.execute_script("arguments[0].value = arguments[1];", quantity_input, str(random_quantity))
        
        # Click add to cart button
        add_to_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-button-action="add-to-cart"]')))
        add_to_cart.click()
        
        # Go back to product list
        driver.back()
        
        # Wait for product list to reload
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#js-product-list .products")))
        
        visited_count += 1
        #time.sleep(1)
    
    product_index += 1

print(f"Visited {visited_count} products")

link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header .menu .container .top-menu #category-73 a")))
link.click()

# Wait for product list to load
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#js-product-list .products")))

visited_count = 0
product_index = 0

while visited_count < 5:
    # Re-fetch products on each iteration to avoid stale references
    products = driver.find_elements(By.CSS_SELECTOR, "#js-product-list .products .js-product")
    
    if product_index >= len(products):
        break
    
    product = products[product_index]
    
    # Check if product is out of stock
    out_of_stock = product.find_elements(By.CSS_SELECTOR, ".out_of_stock")
    
    if len(out_of_stock) == 0:  # Product is in stock
        # Find and click the product link
        product_link = product.find_element(By.TAG_NAME, "a")
        product_link.click()
        
        print(f"Visiting product {visited_count + 1}")
        
        # Wait for quantity input to be present
        quantity_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#quantity_wanted")))
        
        # Generate random quantity (1-3)
        random_quantity = random.randint(1, 3)
        driver.execute_script("arguments[0].value = arguments[1];", quantity_input, str(random_quantity))
        
        # Click add to cart button
        add_to_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-button-action="add-to-cart"]')))
        add_to_cart.click()
        
        # Go back to product list
        driver.back()
        
        # Wait for product list to reload
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#js-product-list .products")))
        
        visited_count += 1
        #time.sleep(1)
    
    product_index += 1

print(f"Visited {visited_count} products")

cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#cart-but")))
cart_button.click()

print("Task 1 completed. Press Enter to continue...")
#input()

# TASK 2 ############################################################################################################

# Find search input and enter "szczoteczka"
search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search_widget input[type='text'][name='s']")))
search_input.clear()
search_input.send_keys("szczoteczka")

# Click search button
search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_widget button.search-btn")))
search_button.click()

# Wait for product list to load
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#js-product-list .products")))

# Get all products
products = driver.find_elements(By.CSS_SELECTOR, "#js-product-list .products .js-product")

# Shuffle products to get random order
product_indices = list(range(len(products)))
random.shuffle(product_indices)

# Find a product that is in stock
selected_product = None
for index in product_indices:
    product = products[index]
    out_of_stock = product.find_elements(By.CSS_SELECTOR, ".out_of_stock")
    
    if len(out_of_stock) == 0:  # Product is in stock
        selected_product = product
        break

if selected_product:
    # Click the product link
    product_link = selected_product.find_element(By.TAG_NAME, "a")
    product_link.click()
    print("Selected random product in stock")
    
    # Wait for and click add to cart button
    add_to_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-button-action="add-to-cart"]')))
    add_to_cart.click()
    
    # Go back
    driver.back()
    
    # Click cart button
    cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#cart-but")))
    cart_button.click()
    
    print("Task 2 completed. Press Enter to continue...")
   #input()
else:
    print("No products in stock found")

# TASK 3 ############################################################################################################

for i in range(3):
    # Wait for page to be ready and find all remove buttons
    remove_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.remove-from-cart")))
    
    if len(remove_buttons) > 0:
        # Select random remove button
        random_button = random.choice(remove_buttons)
        random_button.click()
        
        print(f"Removed item {i + 1}")
        
        # Wait for page to reload/update
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
    else:
        print("No items to remove")
        break

print("Task 3 completed. Press Enter to continue...")
#input()

# TASK 4 ############################################################################################################

# Click register link
register_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.register-link")))
register_link.click()

# Select random gender radio button
gender_radios = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[name="id_gender"][type="radio"]')))
random.choice(gender_radios).click()

# Generate and enter random first name (6 letters)
firstname_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#field-firstname")))
random_firstname = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
firstname_input.send_keys(random_firstname)

# Generate and enter random last name (8 letters)
lastname_input = driver.find_element(By.CSS_SELECTOR, "#field-lastname")
random_lastname = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))
lastname_input.send_keys(random_lastname)

# Generate and enter random email
email_input = driver.find_element(By.CSS_SELECTOR, "#field-email")
random_email = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=16)) + "@mail.xyz"
email_input.send_keys(random_email)

# Enter password
password_input = driver.find_element(By.CSS_SELECTOR, "#field-password")
password_input.send_keys("12345")

# Check all checkboxes
optin_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[name="optin"][type="checkbox"]')
if not optin_checkbox.is_selected():
    optin_checkbox.click()

customer_privacy_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[name="customer_privacy"][type="checkbox"]')
if not customer_privacy_checkbox.is_selected():
    customer_privacy_checkbox.click()

newsletter_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[name="newsletter"][type="checkbox"]')
if not newsletter_checkbox.is_selected():
    newsletter_checkbox.click()

psgdpr_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[name="psgdpr"][type="checkbox"]')
if not psgdpr_checkbox.is_selected():
    psgdpr_checkbox.click()

# Click submit button
submit_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.form-control-submit.float-xs-right[data-link-action="save-customer"][type="submit"]')
submit_button.click()

print("Task 4 completed. Press Enter to continue...")
#input()

# TASK 5 ############################################################################################################

# Click cart button
cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#cart-but")))
cart_button.click()

# Click order link
order_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="https://localhost/zamówienie"]')))
order_link.click()

# Enter random address (8 letters)
address_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#field-address1")))
random_address = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))
address_input.send_keys(random_address)

# Enter random postcode (2 digits - 3 digits)
postcode_input = driver.find_element(By.CSS_SELECTOR, "#field-postcode")
random_postcode = f"{random.randint(10, 99)}-{random.randint(100, 999)}"
postcode_input.send_keys(random_postcode)

# Enter random city (6 letters)
city_input = driver.find_element(By.CSS_SELECTOR, "#field-city")
random_city = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
city_input.send_keys(random_city)

# Click confirm addresses button
confirm_addresses_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].continue.btn.btn-primary.float-xs-right[name="confirm-addresses"]')
confirm_addresses_button.click()

# Select random delivery option
delivery_options = driver.find_elements(By.CSS_SELECTOR, '#delivery_option_3, #delivery_option_4')

if len(delivery_options) == 0:
    print("Too heavy. Picking up at store")
else:
    # Select random from available options (3 or 4)
    random.choice(delivery_options).click()


# Click confirm delivery option button
confirm_delivery_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].continue.btn.btn-primary.float-xs-right[name="confirmDeliveryOption"]')
confirm_delivery_button.click()

# Select payment option 2
payment_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#payment-option-2')))
driver.execute_script("arguments[0].click();", payment_option)

# Check terms and conditions checkbox
terms_checkbox = driver.find_element(By.CSS_SELECTOR, '#conditions_to_approve\\[terms-and-conditions\\]')
if not terms_checkbox.is_selected():
    terms_checkbox.click()

# Click final submit button
final_submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary.center-block')
final_submit_button.click()

print("Task 5 completed. Press Enter to continue...")
#input()

# TASK 6 ############################################################################################################
driver.execute_script("window.open('https://localhost/adminportal', '_blank');")

# Switch to the new window
driver.switch_to.window(driver.window_handles[1])

# Wait for admin login page to load and enter credentials
email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="email"][type="email"]#email')))
email_input.send_keys("john.doe@example.com")

# Enter password
password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="passwd"][type="password"]#passwd')
password_input.send_keys("admin1234")

# Click login button
login_button = driver.find_element(By.CSS_SELECTOR, 'button#submit_login')
login_button.click()


# Find and click the orders link (token will be dynamic) - select second one
orders_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "/adminportal/index.php/sell/orders/")]')))
orders_link = orders_links[1]  # Get second link (index 1)
driver.execute_script("arguments[0].scrollIntoView(true);", orders_link)
time.sleep(1)
driver.execute_script("arguments[0].click();", orders_link)

# Find tbody, first tr, and third td, then click it
order_form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#order_filter_form')))
tbody = order_form.find_element(By.CSS_SELECTOR, 'tbody')
first_tr = tbody.find_element(By.CSS_SELECTOR, 'tr:first-child')
third_td = first_tr.find_element(By.CSS_SELECTOR, 'td:nth-child(3)')

# Try to find a link inside the td and click it
link_in_td = first_tr.find_element(By.CSS_SELECTOR, 'a.btn.tooltip-link.js-link-row-action.dropdown-item.inline-dropdown-item.grid-zobacz-row-link')
driver.execute_script("arguments[0].scrollIntoView(true);", link_in_td)
time.sleep(1)
driver.execute_script("arguments[0].click();", link_in_td)

# Find the status select dropdown
status_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#update_order_status_new_order_status_id')))

# Select option with value="17"
driver.execute_script("arguments[0].value = '3';", status_select)

# Find and click the update status button
update_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.update-status.ml-3')
driver.execute_script("arguments[0].click();", update_button)

# Switch back to first window
driver.switch_to.window(driver.window_handles[0])

print("Task 6 completed. Press Enter to continue...")
#input()

# Click account link
account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.account')))
driver.execute_script("arguments[0].click();", account_link)

# Click history link
history_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.col-lg-4.col-md-6.col-sm-6.col-xs-12#history-link')))
driver.execute_script("arguments[0].click();", history_link)

# Find tbody, first tr, second to last td, and click the link inside
tbody = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody')))
first_tr = tbody.find_element(By.CSS_SELECTOR, 'tr:first-child')
second_to_last_td = first_tr.find_element(By.CSS_SELECTOR, 'td:nth-last-child(2)')
link_in_td = second_to_last_td.find_element(By.TAG_NAME, 'a')
driver.execute_script("arguments[0].click();", link_in_td)

input()