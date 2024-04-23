import time
# from utilities.logger import logger
# import traceback
# import logging
# import json
# import xlsxwriter
# from tabulate import tabulate

import os
import pandas as pd
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
# from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import subprocess
url = 'https://dev.zybisys.com/login'
email_address = "abdul@gmail.com"
email_password = "Tulasi@123"

class Test_Login:
    def __init__(self, driver):
        self.driver = driver
    enter_email_ID = "login-email"
    enter_password_id = "login-password"
    click_button_xpath = "//button[contains(@type,'submit')]"
    home_link_text = "Home"
    dashboard_xpath = "//div[text()='Dashboard']"
    dashboard_sym_xpath = "(//*[contains(@stroke-linejoin,'round')])[3]"
    location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
    location_arrow_xpath = "(//*[contains(@data-testid,'ArrowDropDownIcon')])[1]"
    dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[1]"
    dashboard_search_button_xpath = "(//button[contains(@type,'button')])[1]"
    search_ipaddress_xpath = "//input[@id='search-autocomplete-instance']"

    instance_button_xpath = "//p[text()='Instances']"
    instance_total_xpath = "//p[text()='Instances']/parent::div/descendant::div[6]"
    instance_up_xpath = "//p[text()='Instances']/parent::div/descendant::div[9]"
    instance_down_xpath = "//p[text()='Instances']/parent::div/descendant::div[12]"

    services_xpath = "//p[text()='Services']"
    services_total_xpath = "//p[text()='Services']/parent::div/descendant::div[6]"
    services_ok_xpath = "//p[text()='Services']/parent::div/descendant::div[9]"
    services_warn_xpath = "//p[text()='Services']/parent::div/descendant::div[12]"
    services_crit_xpath = "//p[text()='Services']/parent::div/descendant::div[15]"

    tickets_xpath = "//p[text()='Tickets']"
    pending_tickets_xpath = "//p[text()='Tickets']/parent::div/descendant::div[4]"
    closed_tickets_xpath = "//p[text()='Tickets']/parent::div/descendant::div[5]"

    billing_xpath = "//p[text()='Billing']"
    billing_total_xpath = "//div[@class='MuiBox-root css-w95nqi']//span[text()='Total']"

    # table_state_button_xpath = "(//tr[@class='MuiTableRow-root css-10shlfe']/td/div)["+str(a)+"]"

    # dashboard_instance_xpath = "//*[contains(@class,'service_cards_div')]/a/parent::div/descendant::div[1]"
    # dashboard_instance_xpath = "//*[contains(@class,'service_cards')]/a[1]"
    dashboard_instance_xpath = "(//div[contains(text(), 'Instance')])[3]"
    verify_instance_xpath = "//p[text()='Instances']"


    backup_xpath = "(//div[contains(text(), 'Backup')])[2]"
    verify_backup_xpath = "//h6[text()='Jobs History']"


    monitoring_link_xpath = "(//div[contains(text(), 'Monitoring')])"
    verify_monitoring_xpath = "//button[text()='Services']"


    dashboard_billing_xpath = "(//div[text()='Billing'])[2]"
    # verify_billing_xpath = "//p[text()='Total Balance | ₹0']"
    verify_billing_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 css-4xlsup']"

    report_link_xpath = "(//div[contains(text(), 'Report')])[4]"
    verify_report_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 css-4xlsup']"

    api_link_text = "API"
    storage_link_text = "Storage"

    actions_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td)[11]"
    actions_edit_tag_linktext = "Edit Tags"
    verify_actions_edit_xpath = "//div[@class='MuiBox-root css-jnfgxv']/p[1]"

    actions_edit_instance_link_text = "Edit Instance"
    verify_edit_instance_id = "mui-46-label"

    actions_performance_xpath = "//span[text()='Performance']"
    verify_performance_xpath = "//button[text()='Graphs']"


    table_rows_xpath = "//table[@class='MuiTable-root css-1udbzah']//tr"
    table_column_xpath = "//table[@class='MuiTable-root css-1udbzah']//th"

    dashboard_actions_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[1]/td)[11]"
    dashboard_action_removePartner_xpath = "//span[text()='Remove Partner']"
    verify_remove_Partner_xpath = "//div[@class='MuiBox-root css-1ua32lw']"
    verify_remove_partner_ok_xpath = "//button[text()='Yes']"
    verify_remove_partner_no_xpath= "//button[text()='No']"

    dashboard_actions_second_row_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[2]/td)[11]"
    actions_assign_partner_xpath = "//span[text()='Assign Partner']"
    verify_assigned_partner_xpath = "//span[text()='Assigned Instances for Partner']"
    add_instance_xpath = "(//button[contains(@type,'button')])[3]"
    assigned_instance_checkbox_xpath = "(//input[contains(@type,'checkbox')])[3]"
    assigned_instance_update_button_xpath = "(//button[contains(@type,'button')])[6]"

    service_warn_table_rows_xpath = "(//table[@class='MuiTable-root css-s064k4'])//tr"
    service_warn_table_columns_xpath = "(//table[@class='MuiTable-root css-s064k4'])//th"
    service_warn_table_data_xpath = "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)"

    report_xpath = "(//div[text()= 'Report'])"
    report_data_from_input_xpath = "(//input[contains(@aria-invalid,'false')])[3]"
    report_data_to_input_xpath = "(//input[contains(@aria-invalid,'false')])[4]"
    report_button_xpath = "//button[text()='Submit']"

    report_table_rows_xpath = "(//table[@class='MuiTable-root css-s064k4'])//tr"
    report_table_columns_xpath = "(//table[@class='MuiTable-root css-s064k4'])//th"
    report_table_data_xpath = "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)"



    actions_edit_instance_xpath = "//span[text()='Edit Instance']"
    # actions_edit_instance_enter_xpath = "//input[@id='input-with-icon-textfield']"
    verify_edit_instance_xpath = "//label[text()='Current Instance Name']"

    dashboard_actions_list_xpath = "//ul[contains(@role,'menu')]/div"
    dashboard_edit_tags_xpath = "//span[text()='Edit Tags']"
    edit_manage_tags_xpath = "(//button[contains(@type,'button')])[6]"
    edit_manage_tags_button = "(//button[text()='Submit'])"
    verify_tags_xpath = "//p[text()='MANAGE TAGS']"
    edit_tags_send_keys_xpath = "(//input[@type='text'])[2]"

    service_warn_click_xpath = "//p[text()='Services']/parent::div/descendant::div[12]"
    verify_warn_service = "//div[text()='Total Warning Services']"

    table_search_xpath = "(//div[@class='MuiBox-root css-1ny94l6']/div/div)[1]"
    table_search_input_xpath = "(//input[@type='text'])[2]"

    table_search_pdf_xpath = "//div[contains(@aria-label,'CXO Report')]"
    cxo_report_xpath = "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng')]"
    table_month= "//div[@class='MuiCalendarPicker-root css-1brzq0m']"

    csv_report_xpath = "//div[contains(@aria-label,'Download CSV')]"

    actions_remove_partner = "//span[text()='Remove Partner']"

    state_data = "(//tr[@class='MuiTableRow-root css-10shlfe']/td/div)"

    rows_per_page_xpath = "(//div[contains(@role,'button')])[2]"
    rows_per_page_dropdown_xpath = "(//ul[contains(@role,'listbox')])/li"

    performance_instance_button_xpath = "//button[text()='Instances']"
    select_instance_check_box_xpath = "(//input[contains(@type,'checkbox')])[4]"
    intervel_dropdown_xpath = "(//div[contains(@role,'button')])[3]"
    dropdown_listitems_xpath = "(//ul[contains(@role,'listbox')])//li"
    submit_button_xpath = "//button[text()='Submit']"
    service_button_xpath ="//div[@id='demo-select-small']"
    service_dropdown_list_xpath = "//ul[contains(@role,'listbox')]//li"
    instance_table_rows_xpath = "//table[@class='MuiTable-root css-s064k4']//tr"
    instance_table_columns_xpath = "//table[@class='MuiTable-root css-s064k4']//th"
    table_action_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr/td[@dataindex='action'])[1]"

    dashboard_question_mark_xpath = "//*[contains(@data-testid,'HelpIcon')]"
    verify_question_mark_page_xpath = "//p[@class='text-lg text-justify font-normal py-3']"

    shutdown_state_button_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])//*[@aria-label='Shutdown']"
    running_state_button_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])//*[@aria-label='Running ']"
    total_state_button_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])"

    table_action_xpath_state = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[11])"

    verify_reports_page_xpath = "//*[contains(@varaint,'body2')]"

    verify_dashboard_page_xpath = "(//*[text()='Instances'])[2]"

    verify_location_xpath = "//label[text()='Location']"

    verify_instances_xpath = "(//p[@class='MuiBox-root css-1dfxzqk'])[1]"
    verify_service_xpath = "(//p[@class='MuiBox-root css-1dfxzqk'])[2]"
    verify_service_text_xpath = "//p[text()='Services']"

    verify_table_actions_add_tags_page_xpath = "//p[text()='MANAGE TAGS']"
    verify_table_actions_edit_instance_xpath="//label[text()='Current Instance Name']"
    verify_table_actions_performance_xpath= "//*[text()='Graphs']"

    graphs_instance_button_xpath = "//button[text()='Instances']"
    graph_service_button_xpath = "//div[@id='demo-select-small']"
    interval_dropdown_xpath = "(//div[contains(@role,'button')])[2]"
    verify_graph_instance_page_xpath = "(//div[@class='MuiBox-root css-f0kha9'])[1]"

    def graph_instance_button(self):
        self.driver.find_element(By.XPATH,self.graphs_instance_button_xpath).click()

    def graph_select_instance_check_box(self):
        self.driver.find_element(By.XPATH, self.select_instance_check_box_xpath).click()

    def graph_service_button(self):
        self.driver.find_element(By.XPATH, self.graph_service_button_xpath).click()

    def graph_service_dropdown_list(self):
        list = self.driver.find_elements(By.XPATH, self.service_dropdown_list_xpath)
        # print(list)
        for i in list:
            if i.text == 'CPU':
                i.click()
                break

    def intervel_dropdown(self):
        self.driver.find_element(By.XPATH, self.interval_dropdown_xpath).click()

    def graph_dropdown_listitems(self):
        list = self.driver.find_elements(By.XPATH, self.dropdown_listitems_xpath)
        # print(list)
        for i in list:
            if i.text == 'Today':
                i.click()
                break

    def graph_submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def verify_graph_instance(self):
        data = self.driver.find_element(By.XPATH,self.verify_graph_instance_page_xpath).text
        print(data)


    def verify_actions_remove_Partner(self):
        assert self.driver.find_element(By.XPATH,self.verify_remove_Partner_xpath)

    def check_verify_dashboard_table_actions_remove_partner_page(self):
        data = self.driver.find_element(By.XPATH, self.verify_remove_Partner_xpath).text
        if data == "Are you sure want to remove Partner ?":
            print("successfully displayed message is Are you sure want to remove Partner ?")
        else:
            print("not displayed dashboard page")


    def verify_assigned_partner(self):
        return self.driver.find_element(By.XPATH, self.verify_assigned_partner_xpath).text

    def check_verify_dashboard_table_actions_assigned_partner_page(self):
        data = self.driver.find_element(By.XPATH, self.verify_assigned_partner_xpath).text
        if data == "Assigned Instances for Partner":
            print("successfully displayed message is Assigned Instances for Partner")
        else:
            print("not displayed dashboard page")

    def check_verify_dashboard_table_actions_performance_page(self):
        data = self.driver.find_element(By.XPATH, self.verify_table_actions_performance_xpath).text
        if data == "Graphs":
            print("successfully displayed message is Graphs")
        else:
            print("not displayed dashboard page")

    def verify_table_actions_performance(self):
        return self.driver.find_element(By.XPATH, self.verify_table_actions_performance_xpath).text

    def check_verify_dashboard_table_actions_edit_instance_page(self):
        data = self.driver.find_element(By.XPATH, self.verify_table_actions_edit_instance_xpath).text
        if data == "Current Instance Name":
            print("successfully displayed message is Current Instance Name")
        else:
            print("not displayed dashboard page")

    def verify_table_actions_edit_instance(self):
        return self.driver.find_element(By.XPATH, self.verify_table_actions_edit_instance_xpath).text

    def check_verify_dashboard_table_actions_add_tags_page(self):
        data = self.driver.find_element(By.XPATH, self.verify_table_actions_add_tags_page_xpath).text
        if data == "MANAGE TAGS":
            print("successfully displayed message is MANAGE TAGS")
        else:
            print("not displayed dashboard page")

    def verify_table_actions_add_tags_page(self):
        return self.driver.find_element(By.XPATH, self.verify_table_actions_add_tags_page_xpath).text


    def verify_services_text(self):
        return self.driver.find_element(By.XPATH, self.verify_service_text_xpath).text

    def verify_services(self):
        return self.driver.find_element(By.XPATH, self.verify_service_xpath).text

    def check_verify_dashboard_services(self):
        data = self.driver.find_element(By.XPATH, self.verify_service_xpath).text
        if data == "SERVICES":
            print("successfully displayed message is SERVICES")
        else:
            print("not displayed dashboard page")


    def verify_instances(self):
        return self.driver.find_element(By.XPATH, self.verify_instances_xpath).text

    def check_verify_dashboard_instance(self):
        data = self.driver.find_element(By.XPATH, self.verify_instances_xpath).text
        # return data
        if data == "INSTANCES":
            print("successfully displayed message is INSTANCES")
        else:
            print("not displayed dashboard page")


    def verify_location(self):
        try:
            return self.driver.find_element(By.XPATH, self.verify_location_xpath).text
        except NoSuchElementException:
            print("Element not found")

        # return self.driver.find_element(By.XPATH, self.verify_location_xpath).text

    def check_verify_dashboard_location(self):
        data = self.driver.find_element(By.XPATH, self.verify_location_xpath).text
        # return data
        if data == "Location":
            print("successfully displayed message is Location")
        else:
            print("not displayed dashboard page")

    def verify_dashboard_page(self):
        try:
            element = self.driver.find_element(By.XPATH, self.verify_dashboard_page_xpath).text
            return element
        except NoSuchElementException:
            print("Element not found")

        # return self.driver.find_element(By.XPATH, self.verify_dashboard_page_xpath).text
    def check_verify_dashboard_page(self):
        data = self.driver.find_element(By.XPATH, self.verify_dashboard_page_xpath).text
        # import logging
        #
        # import logging
        # # import mylib
        # logging.basicConfig(filename="C:/Users/zcsu058/PycharmProjects/pythonProject/dashboard.txt", level=logging.INFO, force=True)
        # testlogger = logging.getLogger(__name__)

            # return data
        if data == "Instances":
                # testlogger.info("successfully displayed message is Instances")
            print("successfully displayed message is Instances")
        else:
                # testlogger.info("not successfully displayed message is Instances")
            print("not displayed dashboard page")\



    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)

    def verify_reports_page(self):
        return self.driver.find_element(By.XPATH, self.verify_reports_page_xpath).text

    def running_state_button(self):
        running = self.driver.find_elements(By.XPATH, self.running_state_button_xpath)
        print(len(running))

    def shutdown_state_button(self):
        shutdown = self.driver.find_elements(By.XPATH, self.shutdown_state_button_xpath)
        print(len(shutdown))

    def verify_total_state(self):
        data = self.driver.find_elements(By.XPATH, self.total_state_button_xpath)
        total = len(data)
        print("total instance is:", total)
        running = self.driver.find_elements(By.XPATH, self.running_state_button_xpath)
        b = len(running)
        print("total running state:", b)
        shutdown = self.driver.find_elements(By.XPATH, self.shutdown_state_button_xpath)
        c = len(shutdown)
        print("total shutdown state:", c)
        totals = b + c
        print("total running and shutdown state:",totals)
        if total == totals:
            print("successfully matched:", totals)
        else:
            print("not matched")


    def report_page(self):
        self.driver.find_element(By.XPATH, self.report_xpath).click()
    def report_from_date(self,from_date):
        self.driver.find_element(By.XPATH, self.report_data_from_input_xpath).click()
        self.driver.find_element(By.XPATH, self.report_data_from_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.report_data_from_input_xpath).send_keys(from_date)

    def report_to_date(self,to_date):
        self.driver.find_element(By.XPATH, self.report_data_to_input_xpath).click()
        self.driver.find_element(By.XPATH, self.report_data_to_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.report_data_from_input_xpath).send_keys(to_date)

    def report_submit(self):
        self.driver.find_element(By.XPATH, self.report_button_xpath).click()

    def report_table_total_rows(self):
        rows = self.driver.find_elements(By.XPATH,self.service_warn_table_rows_xpath)
        return print(len(rows))
    def report_table_total_columns(self):
        columns = self.driver.find_elements(By.XPATH, self.service_warn_table_columns_xpath)
        return print(len(columns))
    def report_table_data(self):
        body = self.driver.find_element(By.XPATH, self.service_warn_table_data_xpath)
        data = []
        for tr in body.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)/tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)//td")]
            data.append(row)
        print(data)






    def service_warn_table_total_rows(self):
        rows = self.driver.find_elements(By.XPATH,self.service_warn_table_rows_xpath)
        return print(len(rows))
    def service_warn_table_total_columns(self):
        columns = self.driver.find_elements(By.XPATH, self.service_warn_table_columns_xpath)
        return print(len(columns))
    def service_warn_table_data(self):
        row = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])//th")
        columns = len(column)
        for r in range(1, rows + 1):
            for c in range(1, columns + 1):
                if r == 1:
                    data = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])//tr[" + str(
                        r) + "]//th[" + str(c) + "]")
                    print(data.text, end='       ')
                else:
                    data = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])//tr[" + str(
                        r - 1) + "]//td[" + str(c) + "]")
                    print(data.text, end='    ')
                    # l.append(data.text)
            print()

        # body = self.driver.find_element(By.XPATH, self.service_warn_table_data_xpath)
        # data = []
        # for tr in body.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)/tr"):
        #     row = [item.text for item in tr.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)//td")]
        #     data.append(row)
        # print(data)

    def add_instance(self):
        self.driver.find_element(By.XPATH, self.add_instance_xpath).click()
    def assigned_instance_checkbox(self):
        self.driver.find_element(By.XPATH, self.assigned_instance_checkbox_xpath).click()

    def assigned_instance_update(self):
        self.driver.find_element(By.XPATH, self.assigned_instance_update_button_xpath).click()


    def dashboard_question_mark(self):
        self.driver.find_element(By.XPATH, self.dashboard_question_mark_xpath).click()

    def verify_question_mark_page(self):
        assert self.driver.find_element(By.XPATH, self.verify_question_mark_page_xpath).is_displayed()


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

    def intervel_dropdown(self):
        self.driver.find_element(By.XPATH, self.intervel_dropdown_xpath).click()

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

    def rows_per_page(self):
        self.driver.find_element(By.XPATH, self.rows_per_page_xpath).click()

    def rows_per_page_dropdown(self):
        list = self.driver.find_elements(By.XPATH, self.rows_per_page_dropdown_xpath)
        # print(list)
        for i in list:
            if i.text == '100':
                i.click()
                break

    def table_pdf(self):
        self.driver.find_element(By.XPATH, self.table_search_pdf_xpath).click()

        element = self.driver.find_element(By.XPATH, "(//input[contains(@aria-invalid,'false')])[4]")
        element.click()
        mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
        print(mon_yy)
        while True:
            if mon_yy == "April 2024":
                break
            else:
                self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()

        dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
        print(len(dates))
        for ele in dates:
            print(ele.text)
            if ele.text == "1":
                ele.click()
                break

        # self.driver.find_element(By.XPATH, self.cxo_report_xpath).click()
        # self.driver.find_element(By.XPATH, self.cxo_report_xpath).clear()
        # self.driver.find_element(By.XPATH, self.cxo_report_xpath).send_keys(dates)
        # time.sleep(5)
        element = self.driver.find_element(By.XPATH, "//button[text()='Generate Report']")
        element.click()

        # mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
        # while True:
        #     if (mon_yy == "February 2024"):
        #         break
        #     else:
        #         self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()
        #         mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
        #
        # self.driver.find_elements(By.XPATH,"//button[text()='12']").click()
        # time.sleep(3)
        # element = self.driver.find_element(By.XPATH, "//button[text()='Generate Report']")
        # element.click()









        # month_year = "February"
        # # year = "2024"
        # date = "23"
        # self.driver.find_element(By.XPATH,self.table_search_pdf_xpath).click()
        # self.driver.find_element(By.XPATH, self.cxo_report_xpath).click()
        # while True:
        #     # mon_yy = self.driver.find_element(By.XPATH, "//div[contains(@class,'MuiPickersCalendarHeader-label css-1v994a0')]").text
        #     mon_yy = self.driver.find_element(By.XPATH,"//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
        #     str1 = mon_yy.split()
        #     # print(str1)
        #     i = [str(s) for s in str1 if s.isalpha()]
        #     # print(i)
        #     mystring = "".join(str(element) for element in i)
        #     print(mystring)
        #     # yy = self.driver.find_elements(By.XPATH,"//div[@class='MuiYearPicker-root css-f09ynp']")
        #     if mystring == month_year:
        #         break
        #     else:
        #         self.driver.find_element(By.XPATH,"//button[contains(@title,'Previous month')]").click()
        #
        # dates= self.driver.find_elements(By.XPATH,"(//div[contains(@role,'presentation')])[4]//button")
        # print(len(dates))
        # print(dates)
        # for element in dates:
        #     if element.text == date:
        #         element.click()
        #         break

        # element =self.driver.find_element(By.XPATH,"//button[text()='Generate Report']")
        # element.click()

    def dashboard_report(self):
        element = self.driver.find_element(By.XPATH, self.report_link_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        # self.driver.find_element(By.XPATH, self.report_link_xpath).click()
    def dashboard_verify_report(self):
        return self.driver.find_element(By.XPATH, self.verify_report_xpath).text
    def table_second_row(self):
        self.driver.find_element(By.XPATH, self.dashboard_actions_second_row_xpath).click()
    def action_assigned_partner(self):
        self.driver.find_element(By.XPATH, self.actions_assign_partner_xpath).click()
    def verify_assigned_partner(self):
        return self.driver.find_element(By.XPATH, self.verify_assigned_partner_xpath).text

    def actions_performance(self):
        self.driver.find_element(By.XPATH, self.actions_performance_xpath).click()

    def actions_verify_performance(self):
        return self.driver.find_element(By.XPATH, self.verify_performance_xpath).text

    def table_csv_report(self):
        self.driver.find_element(By.XPATH, self.csv_report_xpath).click()


    def table_search_ipaddress(self):

        element = self.driver.find_element(By.XPATH, self.table_search_xpath)
        element.click()
        # self.driver.find_element(By.XPATH, self.table_search_xpath)
    def table_search_enter_ipaddress(self,ip_address):

        self.driver.find_element(By.XPATH, self.table_search_input_xpath).send_keys(ip_address)


    def dashboard_service_page(self):
        self.driver.find_element(By.XPATH,"(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiCard-root css-1hyex18'])[2]").is_displayed()
    def dashboard_service_warn_button(self):

        # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Services']/parent::div/descendant::div[12]")))

        warn_button = self.driver.find_element(By.XPATH, self.service_warn_click_xpath)
        warn_button.click()

        element = self.driver.find_element(By.XPATH, self.service_warn_click_xpath)
        self.driver.execute_script("arguments[0].click();", element)
    def verify_service_warn_page(self):

         return self.driver.find_element(By.XPATH, self.verify_warn_service).text


    def actions_edit_instance(self):
        # self.driver.switch_to.frame("Edit Instance")
        # time .sleep(5)
        element = self.driver.find_element(By.XPATH,self.actions_edit_instance_xpath)
        element.click()
        # self.driver.switch_to.frame("Edit Instance")

        # try:
        #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.actions_edit_instance_xpath)))
        # except TimeoutException:
        #     print("Element not found within the specified timeout.")
    def action_edit_instance_enter_page(self):
        return self.driver.find_element(By.XPATH, self.verify_edit_instance_xpath).text

    def dashboard_instance(self):
        element = self.driver.find_element(By.XPATH, self.dashboard_instance_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        element = self.driver.find_element(By.XPATH, self.dashboard_instance_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # element = self.driver.find_element(By.LINK_TEXT,self.dashboard_instance_link_text)
        # element.click()

    def dashboard_verify_instance_page(self):
        return self.driver.find_element(By.XPATH, self.verify_instance_xpath).text



    def dashboard_backup(self):
        element = self.driver.find_element(By.XPATH,self.backup_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()


        # element = self.driver.find_element(By.XPATH,self.backup_xpath)
        # element.click()


        # self.driver.find_element(By.XPATH, self.backup_xpath).click()


    def dashboard_verify_backup_page(self):
        return self.driver.find_element(By.XPATH, self.verify_backup_xpath).text

    def dashboard_monitoring_page(self):
        element = self.driver.find_element(By.XPATH, self.monitoring_link_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # self.driver.find_element(By.XPATH, self.monitoring_link_xpath).click()

    def dashboard_monitoring_verify_page(self):
        return self.driver.find_element(By.XPATH, self.verify_monitoring_xpath).text

    def dashboard_billing(self):
        element = self.driver.find_element(By.XPATH, self.dashboard_billing_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        # element = self.driver.find_element(By.XPATH, self.billing_xpath)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.billing_xpath)))
        # element.click()
        # self.driver.find_element(By.XPATH, self.billing_xpath).click()
        # self.driver.switch_to.frame("Billing")

    def dashboard_billing_verify_page(self):
         return self.driver.find_element(By.XPATH, self.verify_billing_xpath).text
        # self.driver.back()

    def dashboard_report_page(self):
        self.driver.find_element(By.LINK_TEXT, self.report_link_text).click()

    def dashboard_report_verify_page(self):
        assert self.driver.find_element(By.XPATH, self.verify_report_xpath).is_displayed()
        self.driver.back()



    def dashboard_action_list(self):
        lists = self.driver.find_elements(By.XPATH,self.dashboard_actions_list_xpath)
        print(len(lists))
        for ele in lists:
            if ele.text == "Edit Tags":
                ele.click()
                break

    def dashboard_edit_tag(self):
        self.driver.find_element(By.XPATH,self.dashboard_edit_tags_xpath).click()
    def edit_manage_tags(self):
        self.driver.find_element(By.XPATH,self.edit_manage_tags_xpath).click()
    def edit_manage_tag_button(self):
        self.driver.find_element(By.XPATH,self.edit_manage_tags_button).click()
    def dashboard_verify_edit_tag(self):
        # elements = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.verify_tags_xpath)))
        # assert elements.text
        return self.driver.find_element(By.XPATH,self.verify_tags_xpath).text

    def dashboard_action_remove_partner(self):
        self.driver.find_element(By.XPATH,self.dashboard_action_removePartner_xpath).click()

    def dashboard_table_action_button(self):
        element = self.driver.find_element(By.XPATH, self.dashboard_actions_xpath)
        element.click()



    def verify_remove_Partner(self):
        assert self.driver.find_element(By.XPATH,self.verify_remove_Partner_xpath)

    def remove_Partner_ok(self):
        return self.driver.find_element(By.XPATH, self.remove_partner_ok_xpath).text
    def remove_Partner_no(self):
        return self.driver.find_element(By.XPATH,self.remove_partner_no_xpath).text



    def email_enter(self,email_address):
        # self.driver.find_element(By.ID,self.enter_email_ID).click()
        # self.driver.find_element(By.ID, self.enter_email_ID).clear()
        self.driver.find_element(By.ID, self.enter_email_ID)
    def email_password(self,email_password):
        # self.driver.find_element(By.ID, self.enter_password_id).click()
        # self.driver.find_element(By.ID, self.enter_password_id).clear()
        self.driver.find_element(By.ID, self.enter_password_id).send_keys(email_password)

    def login_button(self):
        self.driver.find_element(By.XPATH, self.click_button_xpath).click()

    # def home_page(self):
        self.driver.find_element(By.LINK_TEXT, self.home_link_text)

    def dashboard_main_search_button(self):
        self.driver.find_element(By.XPATH,self.dashboard_search_button_xpath).click()

    def search_ip_address(self, search_ipaddress):
        self.driver.find_element(By.XPATH,self.search_ipaddress_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_ipaddress_xpath).send_keys(search_ipaddress)

    def dashboard(self):
        try:
            # Wait for the element to be present on the page
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.dashboard_sym_xpath)))

            # Now that the element is present, you can interact with it
            element.click()  # For example, click on the element
        except TimeoutException:
            print("Element not found within the specified time.")


        # try:
        #     element = self.driver.find_element(By.XPATH, self.dashboard_xpath)
        #     element.click()
        # except TimeoutException:
        #     print("Element not found within the specified time.")


        # self.elemet_to_hover = self.driver.find_element(By.XPATH, self.dashboard_xpath)
        # if self.elemet_to_hover:
        #     actions = ActionChains(self.driver)
        #     actions.move_to_element(self.elemet_to_hover).perform()
        # else:
        #     print("Cannot perform hover action. Element is not available")

    def location(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.location_xpath)))
            # element = self.driver.find_element(By.XPATH, self.location_arrow_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

            # Click on the element
            element.click()
        except ElementClickInterceptedException:
            print("Click intercepted by another element.")
        except TimeoutException:
            print("Element not clickable within the specified time.")
        # except TimeoutException:
        #     print("Element not found within the specified time.")

    def location_dropdown(self):
        # self.driver.find_element(By.XPATH, self.dropdown_elements_xpath).click()
        # element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_elements_xpath)))
        # element.click()
        try:
            element = self.driver.find_element(By.XPATH,self.dropdown_elements_xpath)
            element.click()
        except TimeoutException:
            print("Element not found within the specified time.")
        # for location in element:
        #     if location.text == "IN-MUM-WEST-1":
        #         location.click()
        #         break
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # element.click()

        # print(locations)
        # for router in locations:
        #     if router.text() == 'India (Mumbai) IN-MUM-WEST-1':
                # break
    def dashboard_search_private_ip_address(self):
        self.driver.find_element(By.XPATH, self.dashboard_search_button_xpath).click()

    def select_search_ip_address(self):
        self.driver.find_element(By.XPATH, self.search_ipaddress_xpath).click()

    # def dashboard_instance(self):
    #     return self.driver.find_element(By.XPATH, self.instance_button_xpath).is_displayed()


    def dashboard_instance(self):
        assert self.driver.find_element(By.XPATH,self.instance_button_xpath).is_displayed()
    def dashboard_total_intances(self):
        total = self.driver.find_element(By.XPATH, self.instance_total_xpath).text
        print("total instance:", total)
        # total = self.driver.find_element(By.XPATH,self.instance_total_xpath)
        # print(total)
    def dashboard_up_instances(self):
        up = self.driver.find_element(By.XPATH,self.instance_up_xpath).text
        print("total instance up", up)

    def dashword_down_instance(self):
        down = self.driver.find_element(By.XPATH,self.instance_down_xpath).text
        print("total instance down:", down)

    def verify_dashboard_instances(self):
        total = int(self.driver.find_element(By.XPATH, self.instance_total_xpath).text)
        up = int(self.driver.find_element(By.XPATH, self.instance_up_xpath).text)
        down = int(self.driver.find_element(By.XPATH, self.instance_down_xpath).text)
        total_instance = up + down
        print("total instance:",total_instance)
        if total==total_instance:
            print("total instance values matched")
        else:
            print("not matched instance")

    def services(self):
        assert self.driver.find_element(By.XPATH, self.services_xpath).is_displayed()
    def service_total(self):
        total = self.driver.find_element(By.XPATH,self.services_total_xpath).text
        print("total_service:", total)
    def service_ok(self):
        ok = self.driver.find_element(By.XPATH,self.services_ok_xpath).text
        print("service ok:", ok)
    def service_warn(self):
        warn = self.driver.find_element(By.XPATH,self.services_warn_xpath).text
        print("service warns:", warn)
    def service_crit(self):
        crit = self.driver.find_element(By.XPATH,self.services_crit_xpath).text
        print("service critical:", crit)
    def verify_total_service(self):
        total = int(self.driver.find_element(By.XPATH, self.services_total_xpath).text)
        ok = int(self.driver.find_element(By.XPATH, self.services_ok_xpath).text)
        warn = int(self.driver.find_element(By.XPATH, self.services_warn_xpath).text)
        crit = int(self.driver.find_element(By.XPATH, self.services_crit_xpath).text)
        total_service = ok + warn + crit
        print("total services is:",total_service)
        if total==total_service:
            print("successfully matched")
        else:
            print("not matched service")


    def tickets(self):
        assert self.driver.find_element(By.XPATH, self.tickets_xpath).is_displayed()
    def pending_tickets(self):
        pending_tickets = self.driver.find_element(By.XPATH,self.pending_tickets_xpath).text
        print("pending tickets:", pending_tickets)
    def closed_tickets(self):
        closed_tickets = self.driver.find_element(By.XPATH,self.closed_tickets_xpath).text
        print("closed tickets:", closed_tickets)

    def billing(self):
        assert self.driver.find_element(By.XPATH, self.billing_xpath).is_displayed()
    def billing_total(self):
        return self.driver.find_element(By.XPATH, self.billing_total_xpath)


    def dashboard_instance_state_button(self):
        total_instance = self.driver.find_element(By.XPATH, self.instance_total_xpath).text
        str1 = total_instance.split()
        i = [int(s) for s in str1 if s.isdigit()]
        print(i)
        for n in i:
            print(n)
            for a in range(1,n+1):
                xpath_state = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])["+str(a)+"]"
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath_state)))
                self.driver.execute_script("arguments[0].click();", element)
                print("successfully displayed state button data")
                state_data = "(//*[contains(@class,'MuiTable-root css-1udbzah')]/tbody/tr/descendant::td[1])[" + str(a) + "]"
                data = self.driver.find_element(By.XPATH, state_data).text
                print(data)


                # print("xpath_state:", xpath_state)
        # move_element = "(//button[contains(@type,'button')])[5]"
        # move_element.click()
        # move_element = self.driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[5]")
        # move_element.click()
    def dashboard_table_state(self):


        total_instance = self.driver.find_element(By.XPATH, self.instance_total_xpath).text
        str1 = total_instance.split()
        i = [int(s) for s in str1 if s.isdigit()]
        print(i)
        for n in i:
            print(n)
            for a in range(1, n + 1):
                state_data = "(//*[contains(@class,'MuiTable-root css-1udbzah')]/tbody/tr/descendant::td[1])["+str(a)+"]"

                data = self.driver.find_element(By.XPATH, state_data).text
                print(data)
        # return data.text
        # print(data)
                # print(data)
                # state =data.strip()
                # for info in state:
                #     print(info)
                #     out=''.join(info)
                #     print(out)



                # element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, state_data))).text
                # # ActionChains(self.driver).move_to_element(element).perform()
                # # data =element.text
                # self.driver.execute_script("arguments[0].click();", element)
                # time.sleep(5)
                # print("successfully displayed state button data")
                # print("xpath_state:", element)
                # time.sleep(5)
                # data = self.driver.find_element(By.XPATH, state_data).text
                # print(data)




        # instance_up = self.driver.find_element(By.XPATH,self.instance_up_xpath).text
        # str1 = instance_up.split()
        # i = [int(s) for s in str1 if s.isdigit()]
        # print(i)
        # for n in i:
        #     print(n)
        #     for a in range(1, n+1):
        #         state_data = "(//tr[@class='MuiTableRow-root css-10shlfe']/td/div)"
        #         time.sleep(5)
        #
        #         try:
        #             element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, state_data)))
        #             self.driver.execute_script("return document.readyState") == "complete"
        #         except TimeoutException:
        #             print("Element not found within the specified timeout.")
        #         finally:
        #             self.driver.quit()
        #         # table_state = "(//tr[@class='MuiTableRow-root css-10shlfe']/td/div)["+str(a)+"]"
        #         print("table state data:", element.text)

        # state_data = "(//tr[@class='MuiTableRow-root css-10shlfe']/td/div)
        # self.driver.find_element(By.XPATH,self.table_state_button_xpath).text
        # for i in range(state_data):



                # self.driver.execute_script("arguments[0].scrollIntoView();", element)
                # element.click()
                # self.driver.find_element(By.XPATH,xpath_state).click()
                # self.driver.implicitly_wait(10)
                # capture_data.click()

                # print(capture_data)
                # self.driver.back()
        # self.driver.implicitly_wait(20)
        # self.driver.quit()

        # n = int(self.driver.find_element(By.XPATH, self.intsance_button_xpath).is_displayed())
        # for i in range(1, n + 1):
        # xpath_state = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])"
        # for element in xpath_state:
        #     if isinstance(element, webdriver.remote.webelement.WebElement):
        #     # if element.click():
        #         print(element)

        #    capture_data = self.driver.find_element(By.XPATH, xpath_state)
        # self.driver.implicitly_wait(10)
            # element = driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])["+str(i)+"]")

            # self.driver.execute_script("arguments[0].scrollIntoView();", capture_data)
            # data = capture_data.click()
            # self.driver.implicitly_wait(10)
            # # print(data)
            # # capture_data.click()
            # time.sleep(5)
            # self.driver.back()



    def dashboard_total_rows(self):
        rows= self.driver.find_elements(By.XPATH,self.table_rows_xpath)
        print(len(rows))
    def dashboard_total_columns(self):
        columns = self.driver.find_elements(By.XPATH, self.table_column_xpath)
        print(len(columns))

    def dashboard_table_data(self):
        tbody =self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-jf8bk']/table/tbody")
        data= []
        for tr in tbody.find_elements(By.XPATH, "//tr"):
            row =[item.text for item in tr.find_elements(By.XPATH, ".//td")]
            data.append(row)
            # print(data, end='')
            output_text = ['\t'.join(map(str, sublist)) for sublist in data]

            # Write the output to a temporary text file
            with open('output.txt', 'w') as file:
                file.write('\n'.join(output_text))

            subprocess.Popen(['notepad.exe', 'output.txt'])

    def table_data(self):
        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//th")
        columns = len(column)
        for r in range(1, rows+1):
            for c in range(1, columns+1):
                if r == 1:
                    data =self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//tr["+str(r)+"]//th["+str(c)+"]")
                    print(data.text, end='       ')
                else:
                    data = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//tr["+str(r-1)+"]//td["+str(c)+"]")
                    print(data.text, end='    ')
                    # l.append(data.text)
            print()

        # import pandas as pd
        # print(tabulate(pd.read_csv("dashboard_table.csv", nrows=5),
        #                headers="keys", tablefmt="heavy_grid"))

    def print_in_excel(self):
        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//th")
        columns = len(column)
        for r in range(1, rows + 1):
            for c in range(1, columns + 1):
                if r == 1:
                    data_header = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//tr[" + str(r) + "]//th[" + str(c) + "]").text
                    print(data_header, end='       ')

                else:
                    data_row = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//tr[" + str(r - 1) + "]//td[" + str(c) + "]").text
                    print(data_row, end='    ')

            print()
                    # rows = data_row.split('\n')
                    # file_path = "table_data.txt"
                    # with open(file_path, 'a') as file:
                    #     header = ['State', 'OS', 'Instance', 'Private IP', 'Public IP', 'CPU(1m)', 'Memory(1m)','Bandwidth(15m)', 'Tags', 'Partner', 'Actions']
                    #     file.write('\t'.join(header) + '\n')
                    #     for row in rows:
                    #         print(row)
                    # print("Table data has been added to the text file.")



            # print()
            # file_path = "table_data.txt"
            # with open(file_path, 'a') as file:
            #
            #     header = ['State', 'OS', 'Instance', 'Private IP', 'Public IP', 'CPU(1m)', 'Memory(1m)','Bandwidth(15m)', 'Tags', 'Partner', 'Actions']
            #     file.write('\t'.join(header) + '\n')
            #
            #     # Write table rows
            #     for row in data_row.text:
            #         file.write('\t'.join(row) + '\n')
            #         # Convert each row to a tab-delimited string
            #         # row_str = '\t'.join(map(str, row))
            #         # # Write the row to the file
            #         # file.write(row_str + '\n')
            #
            # print("Table data has been added to the text file.")

        # table_data = i
        # rows = [line.split() for line in table_data.strip().split('\n')]
        #
        # # Determine the maximum width of each column
        # column_widths = [max(len(cell) for cell in column) for column in zip(*rows)]
        # filename = "table_data.txt"
        # with open(filename, "w") as file:
        #     # Write header row
        #     file.write("| " + " | ".join(header.ljust(width) for header, width in zip(rows[0], column_widths)) + " |\n")
        #     # Write separator row
        #     file.write("|-" + "-|-".join("-" * width for width in column_widths) + "-|\n")
        #     # Write data rows
        #     for row in rows[1:]:
        #         file.write("| " + " | ".join(cell.ljust(width) for cell, width in zip(row, column_widths)) + " |\n")
        #
        # print("Table data has been saved to", filename)



        # with open(filename, "w") as file:
        #             # Write each row of the table to the file
        #     for row in table_data:
        #                 # Join elements of the row with tab ('\t') separator and write to file
        #         file.write('\t'.join(row) + '\n')
        #
        # print("Table data has been saved to", filename)


                # try:
                #     json_data = json.loads(data.text)
                # except json.decoder.JSONDecodeError as e:
                #     print("Error decoding JSON:", e)
                # workbook = xlsxwriter.Workbook("table.xlsx")
                # worksheet = workbook.add_worksheet("firstsheet")
                # #
                # worksheet.write(0, 0, "#")
                # worksheet.write(0, 1, "State")
                # worksheet.write(0, 2, "OS")
                # worksheet.write(0, 3, "Instance")
                # worksheet.write(0, 4, "Private")
                # worksheet.write(0, 5, "Public")
                # worksheet.write(0, 6, "CPU")
                # worksheet.write(0, 7, "Memory")
                # worksheet.write(0, 8, "Bandwidth")
                # worksheet.write(0, 8, "Tags")
                # worksheet.write(0, 8, "partner")
                # for index, entry in enumerate(json_data):
                #     worksheet.write(index + 1, 0, str(index))
                #     worksheet.write(index + 1, 1, entry.get("State", ""))
                #     worksheet.write(index + 1, 2, entry.get("OS", ""))
                #     worksheet.write(index + 1, 3, entry.get("Instance", ""))
                #     worksheet.write(index + 1, 4, entry.get("Private", ""))
                #     worksheet.write(index + 1, 5, entry.get("Public", ""))
                #     worksheet.write(index + 1, 6, entry.get("CPU", ""))
                #     worksheet.write(index + 1, 7, entry.get("Memory", ""))
                #     worksheet.write(index + 1, 8, entry.get("Bandwidth", ""))
                #     worksheet.write(index + 1, 9, entry.get("Tags", ""))
                #     worksheet.write(index + 1, 10, entry.get("partner", ""))

                # for index, entry in enumerate(data.text):
                #     worksheet.write(index+1, 0, str(index))
                #     worksheet.write(index + 1, 1, entry.get("State", ""))
                #     worksheet.write(index + 1, 2, entry.get("State", ""))
                #     worksheet.write(index + 1, 3, entry.get("Instance", ""))
                #     worksheet.write(index + 1, 4, entry.get("Private", ""))
                #     worksheet.write(index + 1, 5, entry.get("Public", ""))
                #     worksheet.write(index + 1, 6, entry.get("CPU", ""))
                #     worksheet.write(index + 1, 7, entry.get("Memory", ""))
                #     worksheet.write(index + 1, 8, entry.get("Bandwidth", ""))
                #     worksheet.write(index + 1, 9, entry.get("Tags", ""))
                #     worksheet.write(index + 1, 10, entry.get("partner", ""))





                    # data = data.text
                    # L.append(data)
            # table_data = L
            # print(tabulate(table_data, headers='firstrow', tablefmt="fancy_grid"))



        # print("table is",L)
        # # Sample data
        # data = L
        #
        # # Convert the data into a DataFrame
        # df = pd.DataFrame(data, columns=["State", "OS", "Instance", "Private IP", "Public IP", "CPU(1m)", "Memory(1m)", "Bandwidth(15m)", "Tags", "Partner Actions"])
        #
        #
        # # Export the DataFrame to an Excel file
        # df.to_excel('output.xlsx', index=False)



    def dashboard_instance_table_action_button_for_add_tags(self):
        self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[1]/td[11])").click()
        time.sleep(3)
        lists = self.driver.find_elements(By.XPATH, self.dashboard_actions_list_xpath)
        print(len(lists))
        for ele in lists:
            if ele.text == "Add Tags":
                ele.click()
                break
        # folder_path = "screenshots"
        # screenshot_path = os.path.join(folder_path, "add_tags_screenshot.png")
        # self.driver.save_screenshot(screenshot_path)

    def dashboard_instance_table_action_button_for_edit_tags(self):
        self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[2]/td[11])").click()
        time.sleep(3)
        lists = self.driver.find_elements(By.XPATH, self.dashboard_actions_list_xpath)
        print(len(lists))
        for ele in lists:
            if ele.text == "Edit Tags":
                ele.click()
                break
        # folder_path = "screenshots"
        # screenshot_path = os.path.join(folder_path, "edit_tags_screenshot.png")
        # self.driver.save_screenshot(screenshot_path)


    def dashboard_instance_table_action_button_for_edit_instance(self):
        self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[2]/td[11])").click()
        time.sleep(3)
        lists = self.driver.find_elements(By.XPATH, self.dashboard_actions_list_xpath)
        print(len(lists))
        for ele in lists:
            if ele.text == "Edit Instance":
                ele.click()
                break
        # folder_path = "screenshots"
        # screenshot_path = os.path.join(folder_path, "edit_instance_screenshot.png")
        # self.driver.save_screenshot(screenshot_path)

    def dashboard_instance_table_action_button_for_Performance(self):
        self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[1]/td[11])").click()
        time.sleep(2)
        lists = self.driver.find_elements(By.XPATH, self.dashboard_actions_list_xpath)
        print(len(lists))
        for ele in lists:
            if ele.text == "Performance":
                ele.click()
                break
        # folder_path = "screenshots"
        # screenshot_path = os.path.join(folder_path, "Performance_screenshot.png")
        # self.driver.save_screenshot(screenshot_path)

    def dashboard_instance_table_action_button_for_Assign_Partner(self):
        self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[1]/td[11])").click()
        time.sleep(3)
        lists = self.driver.find_elements(By.XPATH, self.dashboard_actions_list_xpath)
        print(len(lists))
        for ele in lists:
            if ele.text == "Assign Partner":
                ele.click()
                break

    def dashboard_instance_table_action_button_for_remove_Partner(self):
        self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[2]/td[11])").click()
        time.sleep(3)
        lists = self.driver.find_elements(By.XPATH, self.dashboard_actions_list_xpath)
        print(len(lists))
        for ele in lists:
            if ele.text == "Remove Partner":
                ele.click()
                break
        # time.sleep(4)
        # folder_path = "screenshots"
        # screenshot_path = os.path.join(folder_path, "Assign Partner_screenshot.png")
        # self.driver.save_screenshot(screenshot_path)




























































# import time
# import os
#
# from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
# # from telnetlib import EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import tkinter as tk
# import pytest
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# url = 'https://dev.zybisys.com/login'
# email_address = "abdul@gmail.com"
# email_password = "Tulasi@123"
#
# class Test_Login:
#     def __init__(self, driver):
#         self.driver = driver
#     enter_email_ID = "login-email"
#     enter_password_id = "login-password"
#     click_xpath = "//button[contains(@type,'submit')]"
#     home_link_text = "Home"
#     dashboard_xpath = "//div[text()='Dashboard']"
#     location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
#     dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[1]"
#     dashboard_search_button_xpath = "(//button[contains(@type,'button')])[1]"
#     search_ipaddress_xpath = "//input[@id='search-autocomplete-instance']"
#
#     instance_button_xpath = "//p[text()='Instances']"
#     instance_total_xpath = "//p[text()='Instances']/parent::div/descendant::div[6]"
#     instance_up_xpath = "//p[text()='Instances']/parent::div/descendant::div[9]"
#     instance_down_xpath = "//p[text()='Instances']/parent::div/descendant::div[12]"
#
#     services_xpath = "//p[text()='Services']"
#     services_total_xpath = "//p[text()='Services']/parent::div/descendant::div[6]"
#     services_ok_xpath = "//p[text()='Services']/parent::div/descendant::div[9]"
#     services_warn_xpath = "//p[text()='Services']/parent::div/descendant::div[12]"
#     services_crit_xpath = "//p[text()='Services']/parent::div/descendant::div[15]"
#
#     tickets_xpath = "//p[text()='Tickets']"
#     pending_tickets_xpath = "//p[text()='Tickets']/parent::div/descendant::div[4]"
#     closed_tickets_xpath = "//p[text()='Tickets']/parent::div/descendant::div[5]"
#
#     billing_xpath = "//p[text()='Billing']"
#     billing_total_xpath = "//div[@class='MuiBox-root css-w95nqi']//span[text()='Total']"
#
#     # table_state_button_xpath = "(//tr[@class='MuiTableRow-root css-10shlfe']/td/div)["+str(a)+"]"
#
#     # dashboard_instance_xpath = "//*[contains(@class,'service_cards_div')]/a/parent::div/descendant::div[1]"
#     # dashboard_instance_xpath = "//*[contains(@class,'service_cards')]/a[1]"
#     dashboard_instance_xpath = "(//div[contains(text(), 'Instance')])[3]"
#     verify_instance_xpath = "//p[text()='Instances']"
#
#
#     backup_xpath = "(//div[contains(text(), 'Backup')])[2]"
#     verify_backup_xpath = "//h6[text()='Jobs History']"
#
#
#     monitoring_link_xpath = "(//div[contains(text(), 'Monitoring')])"
#     verify_monitoring_xpath = "//button[text()='Services']"
#
#
#     dashboard_billing_xpath = "(//div[text()='Billing'])[2]"
#     # verify_billing_xpath = "//p[text()='Total Balance | ₹0']"
#     verify_billing_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 css-4xlsup']"
#
#     report_link_xpath = "(//div[contains(text(), 'Report')])[4]"
#     verify_report_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 css-4xlsup']"
#
#     api_link_text = "API"
#     storage_link_text = "Storage"
#
#     actions_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td)[11]"
#     actions_edit_tag_linktext = "Edit Tags"
#     verify_actions_edit_xpath = "//div[@class='MuiBox-root css-jnfgxv']/p[1]"
#
#     actions_edit_instance_link_text = "Edit Instance"
#     verify_edit_instance_id = "mui-46-label"
#
#     actions_performance_xpath = "//span[text()='Performance']"
#     verify_performance_xpath = "//button[text()='Graphs']"
#
#
#     table_rows_xpath = "//table[@class='MuiTable-root css-1udbzah']//tr"
#     table_column_xpath = "//table[@class='MuiTable-root css-1udbzah']//th"
#
#     dashboard_actions_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[1]/td)[11]"
#     dashboard_action_removePartner_xpath = "//span[text()='Remove Partner']"
#     verify_remove_Partner_xpath = "//div[text()='Are you sure want to remove Partner ?']"
#     remove_partner_ok_xpath = "//button[text()='Yes']"
#     remove_partner_no_xpath= "//button[text()='No']"
#
#     dashboard_actions_second_row_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[2]/td)[11]"
#     actions_assign_partner_xpath = "//span[text()='Assign Partner']"
#     verify_assigned_partner_xpath = "//span[text()='Assigned Instances for Partner']"
#     add_instance_xpath = "(//button[contains(@type,'button')])[3]"
#     assigned_instance_checkbox_xpath = "(//input[contains(@type,'checkbox')])[3]"
#     assigned_instance_update_button_xpath = "(//button[contains(@type,'button')])[6]"
#
#     service_warn_table_rows_xpath = "(//table[@class='MuiTable-root css-s064k4'])//tr"
#     service_warn_table_columns_xpath = "(//table[@class='MuiTable-root css-s064k4'])//th"
#     service_warn_table_data_xpath = "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)"
#
#     report_xpath = "(//div[text()= 'Report'])"
#     report_data_from_input_xpath = "(//input[contains(@aria-invalid,'false')])[3]"
#     report_data_to_input_xpath = "(//input[contains(@aria-invalid,'false')])[4]"
#     report_button_xpath = "//button[text()='Submit']"
#
#     report_table_rows_xpath = "(//table[@class='MuiTable-root css-s064k4'])//tr"
#     report_table_columns_xpath = "(//table[@class='MuiTable-root css-s064k4'])//th"
#     report_table_data_xpath = "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)"
#
#
#
#     actions_edit_instance_xpath = "//span[text()='Edit Instance']"
#     # actions_edit_instance_enter_xpath = "//input[@id='input-with-icon-textfield']"
#     verify_edit_instance_xpath = "//label[text()='Current Instance Name']"
#
#     dashboard_actions_list_xpath = "//ul[contains(@role,'menu')]/div"
#     dashboard_edit_tags_xpath = "//span[text()='Edit Tags']"
#     edit_manage_tags_xpath = "(//button[contains(@type,'button')])[6]"
#     edit_manage_tags_button = "(//button[text()='Submit'])"
#     verify_tags_xpath = "//p[text()='MANAGE TAGS']"
#     edit_tags_send_keys_xpath = "(//input[@type='text'])[2]"
#
#     service_warn_click_xpath = "//p[text()='Services']/parent::div/descendant::div[12]"
#     verify_warn_service = "//div[text()='Total Warning Services']"
#
#     table_search_xpath = "(//div[@class='MuiBox-root css-1ny94l6']/div/div)[1]"
#     table_search_input_xpath = "(//input[@type='text'])[2]"
#
#     table_search_pdf_xpath = "//div[contains(@aria-label,'CXO Report')]"
#     cxo_report_xpath = "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng')]"
#     table_month= "//div[@class='MuiCalendarPicker-root css-1brzq0m']"
#
#     csv_report_xpath = "//div[contains(@aria-label,'Download CSV')]"
#
#     actions_remove_partner = "//span[text()='Remove Partner']"
#
#     state_data = "(//tr[@class='MuiTableRow-root css-10shlfe']/td/div)"
#
#     rows_per_page_xpath = "(//div[contains(@role,'button')])[2]"
#     rows_per_page_dropdown_xpath = "(//ul[contains(@role,'listbox')])/li"
#
#     performance_instance_button_xpath = "//button[text()='Instances']"
#     select_instance_check_box_xpath = "(//input[contains(@type,'checkbox')])[4]"
#     intervel_dropdown_xpath = "(//div[contains(@role,'button')])[3]"
#     dropdown_listitems_xpath = "(//ul[contains(@role,'listbox')])//li"
#     submit_button_xpath = "//button[text()='Submit']"
#     service_button_xpath ="//div[@id='demo-select-small']"
#     service_dropdown_list_xpath = "//ul[contains(@role,'listbox')]//li"
#     instance_table_rows_xpath = "//table[@class='MuiTable-root css-s064k4']//tr"
#     instance_table_columns_xpath = "//table[@class='MuiTable-root css-s064k4']//th"
#     table_action_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr/td[@dataindex='action'])[1]"
#
#     dashboard_question_mark_xpath = "//*[contains(@data-testid,'HelpIcon')]"
#     verify_question_mark_page_xpath = "//p[@class='text-lg text-justify font-normal py-3']"
#
#     shutdown_state_button_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])//*[@aria-label='Shutdown']"
#     running_state_button_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])//*[@aria-label='Running ']"
#     total_state_button_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])"
#
#     table_action_xpath_state = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[11])"
#
#     verify_reports_page_xpath = "//*[contains(@varaint,'body2')]"
#
#     def verify_reports_page(self):
#         return self.driver.find_element(By.XPATH, self.verify_reports_page_xpath).text
#
#     def running_state_button(self):
#         running = self.driver.find_elements(By.XPATH, self.running_state_button_xpath)
#         print(len(running))
#
#     def shutdown_state_button(self):
#         shutdown = self.driver.find_elements(By.XPATH, self.shutdown_state_button_xpath)
#         print(len(shutdown))
#
#     def verify_total_state(self):
#         data = self.driver.find_elements(By.XPATH, self.total_state_button_xpath)
#         total = len(data)
#         running = self.driver.find_elements(By.XPATH, self.running_state_button_xpath)
#         b = len(running)
#         shutdown = self.driver.find_elements(By.XPATH, self.shutdown_state_button_xpath)
#         c = len(shutdown)
#         totals = b + c
#         print(totals)
#         if total == totals:
#             print("successfully matched:", totals)
#         else:
#             print("not matched")
#
#
#     def report_page(self):
#         self.driver.find_element(By.XPATH, self.report_xpath).click()
#     def report_from_date(self,from_date):
#         self.driver.find_element(By.XPATH, self.report_data_from_input_xpath).click()
#         self.driver.find_element(By.XPATH, self.report_data_from_input_xpath).clear()
#         self.driver.find_element(By.XPATH, self.report_data_from_input_xpath).send_keys(from_date)
#
#     def report_to_date(self,to_date):
#         self.driver.find_element(By.XPATH, self.report_data_to_input_xpath).click()
#         self.driver.find_element(By.XPATH, self.report_data_to_input_xpath).clear()
#         self.driver.find_element(By.XPATH, self.report_data_from_input_xpath).send_keys(to_date)
#
#     def report_submit(self):
#         self.driver.find_element(By.XPATH, self.report_button_xpath).click()
#
#     def report_table_total_rows(self):
#         rows = self.driver.find_elements(By.XPATH,self.service_warn_table_rows_xpath)
#         return print(len(rows))
#     def report_table_total_columns(self):
#         columns = self.driver.find_elements(By.XPATH, self.service_warn_table_columns_xpath)
#         return print(len(columns))
#     def report_table_data(self):
#         body = self.driver.find_element(By.XPATH, self.service_warn_table_data_xpath)
#         data = []
#         for tr in body.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)/tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)//td")]
#             data.append(row)
#         print(data)
#
#
#
#
#
#
#     def service_warn_table_total_rows(self):
#         rows = self.driver.find_elements(By.XPATH,self.service_warn_table_rows_xpath)
#         return print(len(rows))
#     def service_warn_table_total_columns(self):
#         columns = self.driver.find_elements(By.XPATH, self.service_warn_table_columns_xpath)
#         return print(len(columns))
#     def service_warn_table_data(self):
#         body = self.driver.find_element(By.XPATH, self.service_warn_table_data_xpath)
#         data = []
#         for tr in body.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)/tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)//td")]
#             data.append(row)
#         print(data)
#
#     def add_instance(self):
#         self.driver.find_element(By.XPATH, self.add_instance_xpath).click()
#     def assigned_instance_checkbox(self):
#         self.driver.find_element(By.XPATH, self.assigned_instance_checkbox_xpath).click()
#
#     def assigned_instance_update(self):
#         self.driver.find_element(By.XPATH, self.assigned_instance_update_button_xpath).click()
#
#
#     def dashboard_question_mark(self):
#         self.driver.find_element(By.XPATH, self.dashboard_question_mark_xpath).click()
#
#     def verify_question_mark_page(self):
#         assert self.driver.find_element(By.XPATH, self.verify_question_mark_page_xpath).is_displayed()
#
#
#     def instance_total_rows(self):
#         rows = self.driver.find_elements(By.XPATH,self.instance_table_rows_xpath)
#         return print(len(rows))
#     def instance_total_columns(self):
#         columns = self.driver.find_elements(By.XPATH, self.instance_table_columns_xpath)
#         return print(len(columns))
#
#     def instance_table_data(self):
#         tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
#         data = []
#         for tr in tbody.find_elements(By.XPATH, "//tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table)//td")]
#             data.append(row)
#         print(data, end=' ')
#
#     def intervel_dropdown(self):
#         self.driver.find_element(By.XPATH, self.intervel_dropdown_xpath).click()
#
#     def service_button(self):
#         self.driver.find_element(By.XPATH, self.service_button_xpath).click()
#
#     def service_dropdown_list(self):
#         list = self.driver.find_elements(By.XPATH, self.service_dropdown_list_xpath)
#         print(list)
#         for i in list:
#             if i.text == 'CPU':
#                 i.click()
#                 break
#     def dropdown_listitems(self):
#         list = self.driver.find_elements(By.XPATH, self.dropdown_listitems_xpath)
#         print(list)
#         for i in list:
#             if i.text == 'Today':
#                 i.click()
#                 break
#     def submit_button(self):
#         self.driver.find_element(By.XPATH, self.submit_button_xpath).click()
#
#
#     def select_instance_check_box(self):
#         self.driver.find_element(By.XPATH, self.select_instance_check_box_xpath).click()
#
#     def performance_instance_button(self):
#         self.driver.find_element(By.XPATH, self.performance_instance_button_xpath).click()
#
#     def rows_per_page(self):
#         self.driver.find_element(By.XPATH, self.rows_per_page_xpath).click()
#
#     def rows_per_page_dropdown(self):
#         list = self.driver.find_elements(By.XPATH, self.rows_per_page_dropdown_xpath)
#         print(list)
#         for i in list:
#             if i.text == '100':
#                 i.click()
#                 break
#
#     def table_pdf(self):
#         self.driver.find_element(By.XPATH, self.table_search_pdf_xpath).click()
#
#         element = self.driver.find_element(By.XPATH, "(//input[contains(@aria-invalid,'false')])[4]")
#         element.click()
#         mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
#         print(mon_yy)
#         while True:
#             if mon_yy == "April 2024":
#                 break
#             else:
#                 self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()
#
#         dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
#         print(len(dates))
#         for ele in dates:
#             print(ele.text)
#             if ele.text == "1":
#                 ele.click()
#                 break
#
#         # self.driver.find_element(By.XPATH, self.cxo_report_xpath).click()
#         # self.driver.find_element(By.XPATH, self.cxo_report_xpath).clear()
#         # self.driver.find_element(By.XPATH, self.cxo_report_xpath).send_keys(dates)
#         # time.sleep(5)
#         element = self.driver.find_element(By.XPATH, "//button[text()='Generate Report']")
#         element.click()
#
#         # mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
#         # while True:
#         #     if (mon_yy == "February 2024"):
#         #         break
#         #     else:
#         #         self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()
#         #         mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
#         #
#         # self.driver.find_elements(By.XPATH,"//button[text()='12']").click()
#         # time.sleep(3)
#         # element = self.driver.find_element(By.XPATH, "//button[text()='Generate Report']")
#         # element.click()
#
#
#
#
#
#
#
#
#
#         # month_year = "February"
#         # # year = "2024"
#         # date = "23"
#         # self.driver.find_element(By.XPATH,self.table_search_pdf_xpath).click()
#         # self.driver.find_element(By.XPATH, self.cxo_report_xpath).click()
#         # while True:
#         #     # mon_yy = self.driver.find_element(By.XPATH, "//div[contains(@class,'MuiPickersCalendarHeader-label css-1v994a0')]").text
#         #     mon_yy = self.driver.find_element(By.XPATH,"//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
#         #     str1 = mon_yy.split()
#         #     # print(str1)
#         #     i = [str(s) for s in str1 if s.isalpha()]
#         #     # print(i)
#         #     mystring = "".join(str(element) for element in i)
#         #     print(mystring)
#         #     # yy = self.driver.find_elements(By.XPATH,"//div[@class='MuiYearPicker-root css-f09ynp']")
#         #     if mystring == month_year:
#         #         break
#         #     else:
#         #         self.driver.find_element(By.XPATH,"//button[contains(@title,'Previous month')]").click()
#         #
#         # dates= self.driver.find_elements(By.XPATH,"(//div[contains(@role,'presentation')])[4]//button")
#         # print(len(dates))
#         # print(dates)
#         # for element in dates:
#         #     if element.text == date:
#         #         element.click()
#         #         break
#
#         # element =self.driver.find_element(By.XPATH,"//button[text()='Generate Report']")
#         # element.click()
#
#     def dashboard_report(self):
#         element = self.driver.find_element(By.XPATH, self.report_link_xpath)
#         self.driver.execute_script("arguments[0].scrollIntoView();", element)
#         element.click()
#         # self.driver.find_element(By.XPATH, self.report_link_xpath).click()
#     def dashboard_verify_report(self):
#         return self.driver.find_element(By.XPATH, self.verify_report_xpath).text
#     def table_second_row(self):
#         self.driver.find_element(By.XPATH, self.dashboard_actions_second_row_xpath).click()
#     def action_assigned_partner(self):
#         self.driver.find_element(By.XPATH, self.actions_assign_partner_xpath).click()
#     def verify_assigned_partner(self):
#         return self.driver.find_element(By.XPATH, self.verify_assigned_partner_xpath).text
#
#     def actions_performance(self):
#         self.driver.find_element(By.XPATH, self.actions_performance_xpath).click()
#
#     def actions_verify_performance(self):
#         return self.driver.find_element(By.XPATH, self.verify_performance_xpath).text
#
#     def table_csv_report(self):
#         self.driver.find_element(By.XPATH, self.csv_report_xpath).click()
#
#
#     def table_search_ipaddress(self):
#
#         element = self.driver.find_element(By.XPATH, self.table_search_xpath)
#         element.click()
#         # self.driver.find_element(By.XPATH, self.table_search_xpath)
#     def table_search_enter_ipaddress(self,ip_address):
#
#         self.driver.find_element(By.XPATH, self.table_search_input_xpath).send_keys(ip_address)
#
#
#     def dashboard_service_page(self):
#         self.driver.find_element(By.XPATH,"(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiCard-root css-1hyex18'])[2]").is_displayed()
#     def dashboard_service_warn_button(self):
#
#         # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Services']/parent::div/descendant::div[12]")))
#
#         warn_button = self.driver.find_element(By.XPATH, self.service_warn_click_xpath)
#         warn_button.click()
#
#         element = self.driver.find_element(By.XPATH, self.service_warn_click_xpath)
#         self.driver.execute_script("arguments[0].click();", element)
#     def verify_service_warn_page(self):
#
#          return self.driver.find_element(By.XPATH, self.verify_warn_service).text
#
#
#     def actions_edit_instance(self):
#         # self.driver.switch_to.frame("Edit Instance")
#         # time .sleep(5)
#         element = self.driver.find_element(By.XPATH,self.actions_edit_instance_xpath)
#         element.click()
#         # self.driver.switch_to.frame("Edit Instance")
#
#         # try:
#         #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.actions_edit_instance_xpath)))
#         # except TimeoutException:
#         #     print("Element not found within the specified timeout.")
#     def action_edit_instance_enter_page(self):
#         return self.driver.find_element(By.XPATH, self.verify_edit_instance_xpath).text
#
#     def dashboard_instance(self):
#         element = self.driver.find_element(By.XPATH, self.dashboard_instance_xpath)
#         self.driver.execute_script("arguments[0].scrollIntoView();", element)
#         element.click()
#
#         element = self.driver.find_element(By.XPATH, self.dashboard_instance_xpath)
#         self.driver.execute_script("arguments[0].scrollIntoView();", element)
#         element.click()
#
#         # element = self.driver.find_element(By.LINK_TEXT,self.dashboard_instance_link_text)
#         # element.click()
#
#     def dashboard_verify_instance_page(self):
#         return self.driver.find_element(By.XPATH, self.verify_instance_xpath).text
#
#
#
#     def dashboard_backup(self):
#         element = self.driver.find_element(By.XPATH,self.backup_xpath)
#         self.driver.execute_script("arguments[0].scrollIntoView();", element)
#         element.click()
#
#
#         # element = self.driver.find_element(By.XPATH,self.backup_xpath)
#         # element.click()
#
#
#         # self.driver.find_element(By.XPATH, self.backup_xpath).click()
#
#
#     def dashboard_verify_backup_page(self):
#         return self.driver.find_element(By.XPATH, self.verify_backup_xpath).text
#
#     def dashboard_monitoring_page(self):
#         element = self.driver.find_element(By.XPATH, self.monitoring_link_xpath)
#         self.driver.execute_script("arguments[0].scrollIntoView();", element)
#         element.click()
#
#         # self.driver.find_element(By.XPATH, self.monitoring_link_xpath).click()
#
#     def dashboard_monitoring_verify_page(self):
#         return self.driver.find_element(By.XPATH, self.verify_monitoring_xpath).text
#
#     def dashboard_billing(self):
#         element = self.driver.find_element(By.XPATH, self.dashboard_billing_xpath)
#         self.driver.execute_script("arguments[0].scrollIntoView();", element)
#         element.click()
#         # element = self.driver.find_element(By.XPATH, self.billing_xpath)
#         # self.driver.execute_script("arguments[0].scrollIntoView();", element)
#         # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.billing_xpath)))
#         # element.click()
#         # self.driver.find_element(By.XPATH, self.billing_xpath).click()
#         # self.driver.switch_to.frame("Billing")
#
#     def dashboard_billing_verify_page(self):
#          return self.driver.find_element(By.XPATH, self.verify_billing_xpath).text
#         # self.driver.back()
#
#     def dashboard_report_page(self):
#         self.driver.find_element(By.LINK_TEXT, self.report_link_text).click()
#
#     def dashboard_report_verify_page(self):
#         assert self.driver.find_element(By.XPATH, self.verify_report_xpath).is_displayed()
#         self.driver.back()
#
#
#
#     def dashboard_action_list(self):
#         lists = self.driver.find_elements(By.XPATH,self.dashboard_actions_list_xpath)
#         print(len(lists))
#         for ele in lists:
#             if ele.text == "Edit Tags":
#                 ele.click()
#                 break
#
#     def dashboard_edit_tag(self):
#         self.driver.find_element(By.XPATH,self.dashboard_edit_tags_xpath).click()
#     def edit_manage_tags(self):
#         self.driver.find_element(By.XPATH,self.edit_manage_tags_xpath).click()
#     def edit_manage_tag_button(self):
#         self.driver.find_element(By.XPATH,self.edit_manage_tags_button).click()
#     def dashboard_verify_edit_tag(self):
#         # elements = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.verify_tags_xpath)))
#         # assert elements.text
#         return self.driver.find_element(By.XPATH,self.verify_tags_xpath).text
#
#     def dashboard_action_remove_partner(self):
#         self.driver.find_element(By.XPATH,self.dashboard_action_removePartner_xpath).click()
#
#     def dashboard_table_action_button(self):
#         element = self.driver.find_element(By.XPATH, self.dashboard_actions_xpath)
#         element.click()
#
#
#
#     def verify_remove_Partner(self):
#         assert self.driver.find_element(By.XPATH,self.verify_remove_Partner_xpath)
#
#     def remove_Partner_ok(self):
#         return self.driver.find_element(By.XPATH, self.remove_partner_ok_xpath).text
#     def remove_Partner_no(self):
#         return self.driver.find_element(By.XPATH,self.remove_partner_no_xpath).text
#
#
#
#     def email_enter(self,email_address):
#         # self.driver.find_element(By.ID,self.enter_email_ID).click()
#         # self.driver.find_element(By.ID, self.enter_email_ID).clear()
#         self.driver.find_element(By.ID, self.enter_email_ID)
#     def email_password(self,email_password):
#         # self.driver.find_element(By.ID, self.enter_password_id).click()
#         # self.driver.find_element(By.ID, self.enter_password_id).clear()
#         self.driver.find_element(By.ID, self.enter_password_id).send_keys(email_password)
#
#     def login_button(self):
#         self.driver.find_element(By.XPATH, self.click_xpath).click()
#
#     # def home_page(self):
#         self.driver.find_element(By.LINK_TEXT, self.home_link_text)
#
#     def dashboard_main_search_button(self):
#         self.driver.find_element(By.XPATH,self.dashboard_search_button_xpath).click()
#
#     def search_ip_address(self, search_ipaddress):
#         self.driver.find_element(By.XPATH,self.search_ipaddress_xpath).clear()
#         self.driver.find_element(By.XPATH, self.search_ipaddress_xpath).send_keys(search_ipaddress)
#
#     def Hover_over_dashboard(self):
#         self.elemet_to_hover = self.driver.find_element(By.XPATH, self.dashboard_xpath)
#         if self.elemet_to_hover:
#             actions = ActionChains(self.driver)
#             actions.move_to_element(self.elemet_to_hover).perform()
#         else:
#             print("Cannot perform hover action. Element is not available")
#
#     def location(self):
#         self.driver.find_element(By.XPATH, self.location_xpath).click()
#
#     def location_dropdown(self):
#         # self.driver.find_element(By.XPATH, self.dropdown_elements_xpath).click()
#         # element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_elements_xpath)))
#         # element.click()
#         element = self.driver.find_element(By.XPATH,self.dropdown_elements_xpath)
#         element.click()
#         # for location in element:
#         #     if location.text == "IN-MUM-WEST-1":
#         #         location.click()
#         #         break
#         # self.driver.execute_script("arguments[0].scrollIntoView();", element)
#         # element.click()
#
#         # print(locations)
#         # for router in locations:
#         #     if router.text() == 'India (Mumbai) IN-MUM-WEST-1':
#                 # break
#     def dashboard_search_private_ip_address(self):
#         self.driver.find_element(By.XPATH, self.dashboard_search_button_xpath).click()
#
#     def select_search_ip_address(self):
#         self.driver.find_element(By.XPATH, self.search_ipaddress_xpath).click()
#
#     # def dashboard_instance(self):
#     #     return self.driver.find_element(By.XPATH, self.instance_button_xpath).is_displayed()
#
#
#     def dashboard_instance(self):
#         assert self.driver.find_element(By.XPATH,self.instance_button_xpath).is_displayed()
#     def dashboard_total_intances(self):
#         total = self.driver.find_element(By.XPATH, self.instance_total_xpath).text
#         print("total instance:", total)
#         # total = self.driver.find_element(By.XPATH,self.instance_total_xpath)
#         # print(total)
#     def dashboard_up_instances(self):
#         up = self.driver.find_element(By.XPATH,self.instance_up_xpath).text
#         print("total instance up", up)
#
#     def dashword_down_instance(self):
#         down = self.driver.find_element(By.XPATH,self.instance_down_xpath).text
#         print("total instance down:", down)
#
#     def dashboard_instances(self):
#         total = int(self.driver.find_element(By.XPATH, self.instance_total_xpath).text)
#         up = int(self.driver.find_element(By.XPATH, self.instance_up_xpath).text)
#         down = int(self.driver.find_element(By.XPATH, self.instance_down_xpath).text)
#         total_instance = up + down
#         print("total instance:",total_instance)
#         if total==total_instance:
#             print("total instance values matched")
#         else:
#             print("not matched instance")
#
#     def services(self):
#         assert self.driver.find_element(By.XPATH, self.services_xpath).is_displayed()
#     def service_total(self):
#         total = self.driver.find_element(By.XPATH,self.services_total_xpath).text
#         print("total_service:", total)
#     def service_ok(self):
#         ok = self.driver.find_element(By.XPATH,self.services_ok_xpath).text
#         print("service ok:", ok)
#     def service_warn(self):
#         warn = self.driver.find_element(By.XPATH,self.services_warn_xpath).text
#         print("service warns:", warn)
#     def service_crit(self):
#         crit = self.driver.find_element(By.XPATH,self.services_crit_xpath).text
#         print("service critical:", crit)
#     def verify_total_service(self):
#         total = int(self.driver.find_element(By.XPATH, self.services_total_xpath).text)
#         ok = int(self.driver.find_element(By.XPATH, self.services_ok_xpath).text)
#         warn = int(self.driver.find_element(By.XPATH, self.services_warn_xpath).text)
#         crit = int(self.driver.find_element(By.XPATH, self.services_crit_xpath).text)
#         total_service = ok + warn + crit
#         print("total services is:",total_service)
#         if total==total_service:
#             print("successfully matched")
#         else:
#             print("not matched service")
#
#
#     def tickets(self):
#         assert self.driver.find_element(By.XPATH, self.tickets_xpath).is_displayed()
#     def pending_tickets(self):
#         pending_tickets = self.driver.find_element(By.XPATH,self.pending_tickets_xpath).text
#         print("pending tickets:", pending_tickets)
#     def closed_tickets(self):
#         closed_tickets = self.driver.find_element(By.XPATH,self.closed_tickets_xpath).text
#         print("closed tickets:", closed_tickets)
#
#     def billing(self):
#         assert self.driver.find_element(By.XPATH, self.billing_xpath).is_displayed()
#     def billing_total(self):
#         return self.driver.find_element(By.XPATH, self.billing_total_xpath)
#
#
#     def dashboard_instance_state_button(self):
#         total_instance = self.driver.find_element(By.XPATH, self.instance_total_xpath).text
#         str1 = total_instance.split()
#         i = [int(s) for s in str1 if s.isdigit()]
#         print(i)
#         for n in i:
#             print(n)
#             for a in range(1,n+1):
#                 xpath_state = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])["+str(a)+"]"
#                 # time.sleep(5)
#                 element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath_state)))
#                 # ActionChains(self.driver).move_to_element(element).perform()
#                 self.driver.execute_script("arguments[0].click();", element)
#                 # time.sleep(5)
#                 print("successfully displayed state button data")
#                 state_data = "(//*[contains(@class,'MuiTable-root css-1udbzah')]/tbody/tr/descendant::td[1])[" + str(a) + "]"
#                 data = self.driver.find_element(By.XPATH, state_data).text
#                 print(data)
#
#
#                 # print("xpath_state:", xpath_state)
#         # move_element = "(//button[contains(@type,'button')])[5]"
#         # move_element.click()
#         # move_element = self.driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[5]")
#         # move_element.click()
#     def dashboard_table_state(self):
#         total_instance = self.driver.find_element(By.XPATH, self.instance_total_xpath).text
#         str1 = total_instance.split()
#         i = [int(s) for s in str1 if s.isdigit()]
#         print(i)
#         for n in i:
#             print(n)
#             for a in range(1, n + 1):
#                 state_data = "(//*[contains(@class,'MuiTable-root css-1udbzah')]/tbody/tr/descendant::td[1])["+str(a)+"]"
#
#                 data = self.driver.find_element(By.XPATH, state_data).text
#                 print(data)
#         # return data.text
#         # print(data)
#                 # print(data)
#                 # state =data.strip()
#                 # for info in state:
#                 #     print(info)
#                 #     out=''.join(info)
#                 #     print(out)
#
#
#
#                 # element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, state_data))).text
#                 # # ActionChains(self.driver).move_to_element(element).perform()
#                 # # data =element.text
#                 # self.driver.execute_script("arguments[0].click();", element)
#                 # time.sleep(5)
#                 # print("successfully displayed state button data")
#                 # print("xpath_state:", element)
#                 # time.sleep(5)
#                 # data = self.driver.find_element(By.XPATH, state_data).text
#                 # print(data)
#
#
#
#
#         # instance_up = self.driver.find_element(By.XPATH,self.instance_up_xpath).text
#         # str1 = instance_up.split()
#         # i = [int(s) for s in str1 if s.isdigit()]
#         # print(i)
#         # for n in i:
#         #     print(n)
#         #     for a in range(1, n+1):
#         #         state_data = "(//tr[@class='MuiTableRow-root css-10shlfe']/td/div)"
#         #         time.sleep(5)
#         #
#         #         try:
#         #             element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, state_data)))
#         #             self.driver.execute_script("return document.readyState") == "complete"
#         #         except TimeoutException:
#         #             print("Element not found within the specified timeout.")
#         #         finally:
#         #             self.driver.quit()
#         #         # table_state = "(//tr[@class='MuiTableRow-root css-10shlfe']/td/div)["+str(a)+"]"
#         #         print("table state data:", element.text)
#
#         # state_data = "(//tr[@class='MuiTableRow-root css-10shlfe']/td/div)
#         # self.driver.find_element(By.XPATH,self.table_state_button_xpath).text
#         # for i in range(state_data):
#
#
#
#                 # self.driver.execute_script("arguments[0].scrollIntoView();", element)
#                 # element.click()
#                 # self.driver.find_element(By.XPATH,xpath_state).click()
#                 # self.driver.implicitly_wait(10)
#                 # capture_data.click()
#
#                 # print(capture_data)
#                 # self.driver.back()
#         # self.driver.implicitly_wait(20)
#         # self.driver.quit()
#
#         # n = int(self.driver.find_element(By.XPATH, self.intsance_button_xpath).is_displayed())
#         # for i in range(1, n + 1):
#         # xpath_state = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])"
#         # for element in xpath_state:
#         #     if isinstance(element, webdriver.remote.webelement.WebElement):
#         #     # if element.click():
#         #         print(element)
#
#         #    capture_data = self.driver.find_element(By.XPATH, xpath_state)
#         # self.driver.implicitly_wait(10)
#             # element = driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])["+str(i)+"]")
#
#             # self.driver.execute_script("arguments[0].scrollIntoView();", capture_data)
#             # data = capture_data.click()
#             # self.driver.implicitly_wait(10)
#             # # print(data)
#             # # capture_data.click()
#             # time.sleep(5)
#             # self.driver.back()
#
#
#
#     def dashboard_total_rows(self):
#         rows= self.driver.find_elements(By.XPATH,self.table_rows_xpath)
#         print(len(rows))
#     def dashboard_total_columns(self):
#         columns = self.driver.find_elements(By.XPATH, self.table_column_xpath)
#         print(len(columns))
#
#     def dashboard_table_data(self):
#         tbody =self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1z0dixm']/table/tbody")
#         data= []
#         for tr in tbody.find_elements(By.XPATH, "//tr"):
#             row =[item.text for item in tr.find_elements(By.XPATH, ".//td")]
#             data.append(row)
#         print(data, end ="  ")
#
#
#
#     def dashboard_instance_table_action_button_for_add_tags(self):
#         self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[1]/td[11])").click()
#         time.sleep(3)
#         lists = self.driver.find_elements(By.XPATH, self.dashboard_actions_list_xpath)
#         print(len(lists))
#         for ele in lists:
#             if ele.text == "Add Tags":
#                 ele.click()
#                 break
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "add_tags_screenshot.png")
#         self.driver.save_screenshot(screenshot_path)
#
#     def dashboard_instance_table_action_button_for_edit_tags(self):
#         self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[2]/td[11])").click()
#         time.sleep(3)
#         lists = self.driver.find_elements(By.XPATH, self.dashboard_actions_list_xpath)
#         print(len(lists))
#         for ele in lists:
#             if ele.text == "Edit Tags":
#                 ele.click()
#                 break
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "edit_tags_screenshot.png")
#         self.driver.save_screenshot(screenshot_path)
#
#
#     def dashboard_instance_table_action_button_for_edit_instance(self):
#         self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[2]/td[11])").click()
#         time.sleep(3)
#         lists = self.driver.find_elements(By.XPATH, self.dashboard_actions_list_xpath)
#         print(len(lists))
#         for ele in lists:
#             if ele.text == "Edit Instance":
#                 ele.click()
#                 break
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "edit_instance_screenshot.png")
#         self.driver.save_screenshot(screenshot_path)
#
#     def dashboard_instance_table_action_button_for_Performance(self):
#         self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[1]/td[11])").click()
#         time.sleep(3)
#         lists = self.driver.find_elements(By.XPATH, self.dashboard_actions_list_xpath)
#         print(len(lists))
#         for ele in lists:
#             if ele.text == "Performance":
#                 ele.click()
#                 break
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "Performance_screenshot.png")
#         self.driver.save_screenshot(screenshot_path)
#
#     def dashboard_instance_table_action_button_for_Assign_Partner(self):
#         self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[1]/td[11])").click()
#         time.sleep(3)
#         lists = self.driver.find_elements(By.XPATH, self.dashboard_actions_list_xpath)
#         print(len(lists))
#         for ele in lists:
#             if ele.text == "Assign Partner":
#                 ele.click()
#                 break
#         time.sleep(4)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "Assign Partner_screenshot.png")
#         self.driver.save_screenshot(screenshot_path)
#
#
#
#
#
#
