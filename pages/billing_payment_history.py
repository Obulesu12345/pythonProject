import subprocess
import time
from openpyxl import Workbook
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentHistory:

    def __init__(self,driver):
        self.driver = driver

    billing_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[3]"
    verify_billing_payment_history_page_xpath = "//div[text()='Payment History']"
    payment_history_button_xpath = "//div[text()='Payment History']"

    verify_payment_history_page_xpath = "(//*[text()='Payment History'])[3]"
    right_arrow_button_xpath = "//*[contains(@data-testid,'KeyboardArrowRightIcon')]"

    invoices_button_xpath = "//*[text()='Invoices']"
    total_balance_check_box_xpath = "(//input[contains(@type,'checkbox')])[1]"
    total_balance_xpath = "(//*[contains(@varaint,'body2')])"

    table_dropdown_arrow_button_xpath = "(//div[contains(@role,'button')])[2]"
    dropdown_items_xpath = "//*[contains(@role,'listbox')]/li"

    verify_billing_invoices_text_xpath = "//p[contains(@varaint,'body2')]"

    def verify_billing_invoices_text(self):
        return self.driver.find_element(By.XPATH, self.verify_billing_invoices_text_xpath).text

    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)

    def dropdown_listitems(self):
        list = self.driver.find_elements(By.XPATH, self.dropdown_items_xpath)
        print(list)
        for i in list:
            if i.text == '100':
                i.click()
                break

    def table_dropdown_arrow_button(self):
        self.driver.find_element(By.XPATH, self.table_dropdown_arrow_button_xpath).click()

    def total_balance(self):
        data = self.driver.find_element(By.XPATH, self.total_balance_xpath).text
        print(data)

    def total_balance_check_box(self):
        self.driver.find_element(By.XPATH, self.total_balance_check_box_xpath).click()

    def invoice_table_data(self):
        thead = self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1fpff4c']/table/thead")
        data = []
        for tr in thead.find_elements(By.XPATH, "//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, ".//th")]
            data.append(row)
            import os
            directory = 'output'
            if not os.path.exists(directory):
                os.makedirs(directory)
            output_text = ['\t'.join(map(str, sublist)) for sublist in data]
            file_path = os.path.join(directory, 'payment_history_output.txt')
            with open(file_path, 'w') as file:
                file.write('\n'.join(output_text))
            subprocess.Popen(['notepad.exe', 'payment_history_output.txt'])

        tbody = self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1fpff4c']/table/tbody")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, ".//td")]
            data.append(row)
            import os
            # Check if the directory exists, if not create it
            directory = 'output'
            if not os.path.exists(directory):
                os.makedirs(directory)

            output_text = ['\t'.join(map(str, sublist)) for sublist in data]

            file_path = os.path.join(directory, 'payment_history_output.txt')
            with open(file_path, 'w') as file:
                file.write('\n'.join(output_text))
            subprocess.Popen(['notepad.exe', 'payment_history_output.txt'])



        # tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        # data = []
        # for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
        #     row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
        #     data.append(row)
        # print(data, end=' ')

    def table_invoice_data(self):
        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//th")
        columns = len(column)
        for r in range(1, rows+1):
            for c in range(1, columns+1):
                if r == 1:
                    data =self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr["+str(r)+"]//th["+str(c)+"]")
                    print(data.text, end='       ')
                else:
                    data = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr["+str(r-1)+"]//td["+str(c)+"]")
                    print(data.text, end='    ')
            print()




    def invoices_button(self):
        self.driver.find_element(By.XPATH, self.invoices_button_xpath).click()

    def right_arrow_button(self):
        self.driver.find_element(By.XPATH, self.right_arrow_button_xpath).click()

    def payment_history_table_data(self):
        thead = self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1fpff4c']/table/thead")
        data = []
        for tr in thead.find_elements(By.XPATH, "//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, ".//th")]
            data.append(row)
            import os
            directory = 'output'
            if not os.path.exists(directory):
                os.makedirs(directory)
            output_text = ['\t'.join(map(str, sublist)) for sublist in data]
            file_path = os.path.join(directory, 'payment_history_output.txt')
            with open(file_path, 'w') as file:
                file.write('\n'.join(output_text))
            subprocess.Popen(['notepad.exe', 'payment_history_output.txt'])

        tbody = self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1fpff4c']/table/tbody")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, ".//td")]
            data.append(row)
            import os
            # Check if the directory exists, if not create it
            directory = 'output'
            if not os.path.exists(directory):
                os.makedirs(directory)

            output_text = ['\t'.join(map(str, sublist)) for sublist in data]

            file_path = os.path.join(directory, 'payment_history_output.txt')
            with open(file_path, 'w') as file:
                file.write('\n'.join(output_text))
            subprocess.Popen(['notepad.exe', 'payment_history_output.txt'])

        # tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        # data = []
        # for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
        #     row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
        #     # self.driver.find_element(By.XPATH, self.right_arrow_button_xpath).click()
        #     data.append(row)
        #
        # print(data, end=' ')


    def table_data(self):
        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//th")
        columns = len(column)
        for r in range(1, rows+1):
            for c in range(1, columns+1):
                if r == 1:
                    data =self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr["+str(r)+"]//th["+str(c)+"]")
                    print(data.text, end='       ')
                else:
                    data = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr["+str(r-1)+"]//td["+str(c)+"]")
                    print(data.text, end='    ')
            print()


    def verify_payment_history_page(self):
        return self.driver.find_element(By.XPATH, self.verify_payment_history_page_xpath).text

    def verify_billing_payment_history_page(self):
        return self.driver.find_element(By.XPATH, self.verify_billing_payment_history_page_xpath).text

    def billing_button(self):
        self.driver.find_element(By.XPATH, self.billing_button_xpath).click()

    def billing_payment_page(self):
        self.driver.find_element(By.XPATH, self.billing_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.payment_history_button_xpath)))
        element.click()


