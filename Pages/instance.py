import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstancePage:

    def __init__(self,driver):
        self.driver = driver

    manage_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[2]"
    instance_button_xpath = "(//div[text()='Instance'])"
    instance_table_rows_xpath = "//table[@class='MuiTable-root css-s064k4']//tr"
    instance_table_columns_xpath = "//table[@class='MuiTable-root css-s064k4']//th"
    table_action_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr/td[@dataindex='action'])[1]"
    performance_button_xpath = "//span[text()='Performance']"
    performance_instance_button_xpath = "//button[text()='Instances']"

    select_instance_check_box_xpath = "(//input[contains(@type,'checkbox')])[4]"
    intervel_dropdown_xpath = "(//div[contains(@role,'button')])[3]"
    dropdown_listitems_xpath = "(//ul[contains(@role,'listbox')])//li"
    submit_button_xpath = "//button[text()='Submit']"
    service_button_xpath ="//div[@id='demo-select-small']"
    service_dropdown_list_xpath = "//ul[contains(@role,'listbox')]//li"

    warning_xpath = "//button[text()='Warnings']"
    warning_table_xpath = "//tbody[@class='MuiTableBody-root css-1xnox0e']//tr"

    criticals_xpath = "//button[text()='Criticals']"
    critical_table_xpath = "//tbody[@class='MuiTableBody-root css-1xnox0e']//tr"

    location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
    dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[1]"

    verify_instances_text_xpath = "//p[text()='Instances']"

    table_instance_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr[2]/td)[3]"
    table_instance_notification_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr[2]/td)[9]"

    instance_table_ok_button_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])"

    instance_table_warn_button_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])"

    instance_table_crit_button_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])"

    instance_warning_no_of_xpath = "//tbody[@class='MuiTableBody-root css-1xnox0e']//tr"


    def instance_no_of_criticals(self):
        warnings_data = self.driver.find_elements(By.XPATH, self.instance_warning_no_of_xpath)
        print(len(warnings_data))

    def instance_no_of_warnings(self):
        warnings_data = self.driver.find_elements(By.XPATH, self.instance_warning_no_of_xpath)
        print(len(warnings_data))


    def verify_total_service(self):
        data = self.driver.find_elements(By.XPATH, self.instance_table_crit_button_xpath)
        l = []
        # a = self.driver.find_element(By.XPATH, self.instance_table_crit_button_xpath).text
        # print(a)
        # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
        # print(sum(data))
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])[" + str(i) + "]").text
            l.append(int(s))
        print(sum(l))
        crit = sum(l)

        data = self.driver.find_elements(By.XPATH, self.instance_table_warn_button_xpath)
        l = []
        # a = self.driver.find_element(By.XPATH, self.instance_table_warn_button_xpath).text
        # print(a)
        # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
        # print(sum(data))
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])[" + str(i) + "]").text
            l.append(int(s))
        print(sum(l))
        warn = sum(l)

        data = self.driver.find_elements(By.XPATH, self.instance_table_ok_button_xpath)
        l=[]
        # a=self.driver.find_element(By.XPATH, self.instance_table_ok_button_xpath).text
        # print(a)
        # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
        # print(sum(data))
        for i in range(1, len(data)+1):
            s=self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])["+str(i)+"]").text
            l.append(int(s))
        print(sum(l))
        ok = sum(l)

        total = crit + warn + ok
        print("total instance is :", total)








    def instance_table_crit_button(self):
        data = self.driver.find_elements(By.XPATH, self.instance_table_crit_button_xpath)
        l = []
        a = self.driver.find_element(By.XPATH, self.instance_table_crit_button_xpath).text
        # print(a)
        # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
        # print(sum(data))
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])[" + str(i) + "]").text
            l.append(int(s))
        print(sum(l))
        print("success")

    def instance_table_warn_button(self):
        data = self.driver.find_elements(By.XPATH, self.instance_table_warn_button_xpath)
        l=[]
        a=self.driver.find_element(By.XPATH, self.instance_table_warn_button_xpath).text
        # print(a)
        # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
        # print(sum(data))
        for i in range(1, len(data)+1):
            s=self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])["+str(i)+"]").text
            try:
                l.append(int(s))
            except ValueError:
                print("value:", s)
            # l.append(int(s))
        print(sum(l))
        print("success")

    def instance_table_ok_button(self):
        data = self.driver.find_elements(By.XPATH, self.instance_table_ok_button_xpath)
        l=[]
        a=self.driver.find_element(By.XPATH, self.instance_table_ok_button_xpath).text
        # print(a)
        # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
        # print(sum(data))
        for i in range(1, len(data)+1):
            s=self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])["+str(i)+"]").text
            try:
                l.append(int(s))
            except ValueError:
                print("value:", s)
            # l.append(int(s))
        print(sum(l))
        print("success")

    def table_instance_notification_button(self):
        self.driver.find_element(By.XPATH, self.table_instance_notification_button_xpath).click()

    def table_instance_notification_data(self):
        tbody = self.driver.find_element(By.XPATH, "(//div[@class='MuiBox-root css-1fpff4c'])[2]//table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "(//div[@class='MuiBox-root css-1fpff4c'])[2]//table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "(//div[@class='MuiBox-root css-1fpff4c'])[2]//table//td")]
            data.append(row)
        print(data, end=' ')

    def table_instance_button(self):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.table_instance_button_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.table_instance_button_xpath).click()

    def table_instance_data(self):
        tbody = self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1l3xj4b']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1l3xj4b']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1l3xj4b']/table//td")]
            data.append(row)
        print(data, end=' ')



    def verify_instances_text(self):
        return self.driver.find_element(By.XPATH, self.verify_instances_text_xpath).text

    def location(self):
        self.driver.find_element(By.XPATH, self.location_xpath).click()

    def location_dropdown(self):

        element = self.driver.find_element(By.XPATH, self.dropdown_elements_xpath)
        element.click()
        # for location in element:
        #     if location.text == "India (Mumbai) IN-MUM-WEST-2":
        #         location.click()
        #         break

    def instance_criticals(self):
        self.driver.find_element(By.XPATH, self.criticals_xpath).click()

    def critical_table(self):
        data = self.driver.find_element(By.XPATH, self.critical_table_xpath).text
        print(data)

    def critical_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//td")]
            data.append(row)
        print(data, end=' ')



    def instance_warnings(self):
        self.driver.find_element(By.XPATH,self.warning_xpath).click()

    def warning_table(self):
        data = self.driver.find_element(By.XPATH,self.warning_table_xpath).text
        print(data)

    def warning_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//td")]
            data.append(row)
        print(data, end=' ')

    def service_button(self):
        self.driver.find_element(By.XPATH, self.service_button_xpath).click()

    def service_dropdown_list(self):
        list = self.driver.find_elements(By.XPATH, self.service_dropdown_list_xpath)
        print(list)
        for i in list:
            if i.text == 'CPU':
                i.click()
                break
    def dropdown_listitems(self):
        list = self.driver.find_elements(By.XPATH, self.dropdown_listitems_xpath)
        print(list)
        for i in list:
            if i.text == 'Today':
                i.click()
                break
    def submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()


    def select_instance_check_box(self):
        self.driver.find_element(By.XPATH, self.select_instance_check_box_xpath).click()

    def performance_instance_button(self):
        self.driver.find_element(By.XPATH, self.performance_instance_button_xpath).click()

    def intervel_dropdown(self):
        self.driver.find_element(By.XPATH, self.intervel_dropdown_xpath).click()

    def instances_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(5)

    def instance_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.instance_button_xpath)))
        element.click()

    def table_instance_action_performance(self):
        self.driver.find_element(By.XPATH, self.table_action_button_xpath).click()

    def action_performance(self):
        self.driver.find_element(By.XPATH,self.performance_button_xpath).click()

    def instance_total_rows(self):
        rows = self.driver.find_elements(By.XPATH,self.instance_table_rows_xpath)
        return print(len(rows))
    def instance_total_columns(self):
        columns = self.driver.find_elements(By.XPATH, self.instance_table_columns_xpath)
        return print(len(columns))

    def instance_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table)//td")]
            data.append(row)
        print(data, end=' ')

