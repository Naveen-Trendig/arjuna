from .driverelement import SeleniumDriverElement
from arjuna.setuext.guiauto.dispatcher.driver.impl.driver_commands import DriverCommands
from arjuna.setuext.guiauto.dispatcher.driver.impl.element_finder import ElementFinder
from arjuna.setuext.guiauto.dispatcher.driver.impl.melement import MultiElement
from selenium.webdriver.remote.webelement import WebElement

class SeleniumDriver:

    def __init__(self, setu_id):
        self.__setu_id = setu_id
        self.__config = None
        self.__driver = None
        self.__driver_elements = {}
        self.__driver_melements = {}

    def create_gui_element_dispatcher(self, element_setu_id):
        return SeleniumDriverElement(self, element_setu_id)

    @property
    def setu_id(self):
        return self.__setu_id

    @property
    def driver(self):
        return self.__driver

    def add_driver_element(self, setu_id, element):
        self.__driver_elements[setu_id] = element

    def add_driver_melement(self, setu_id, melement):
        self.__driver_melements[setu_id] = melement

    def get_driver_element(self, setu_id):
        return self.__driver_elements[setu_id]

    def get_driver_melement(self, setu_id):
        return self.__driver_melements[setu_id]

    def __create_success_response(self):
        response = dict()
        response["result"] = "success"
        response["data"] = {}
        return response

    def launch(self, config):
        self.__config = config
        from .impl.browser_launcher import BrowserLauncher
        self.__driver = BrowserLauncher.launch(config) 

    def quit(self):
        DriverCommands.quit(self.__driver)

    def go_to_url(self, url):
        DriverCommands.go_to_url(self.__driver, url)

    def go_back_in_browser(self):
        DriverCommands.go_back_in_browser(self.__driver)

    def go_forward_in_browser(self):
        DriverCommands.go_forward_in_browser(self.__driver)

    def refersh_browser(self):
        DriverCommands.refersh_browser(self.__driver)

    def get_source(self):
        return DriverCommands.get_source(self.__driver)

    def execute_javascript(self, script):
        return DriverCommands.execute_javascript(self.__driver, script)

    def take_screenshot(self):
        DriverCommands.take_screenshot(self.__driver)

    def find_element(self, child_gui_element_setu_id, with_type, with_value):
        element = ElementFinder.find_element(self.__driver, with_type, with_value)
        self.__driver_elements[child_gui_element_setu_id] = element

    def __process_single_js_element(self, element):
        # JS returns null, undefined
        if element is None:
            raise Exception("JavaScript could not find element.")
        elif not isinstance(element, WebElement):
            raise Exception("JavaScript returned a non-element object.")
        else:
            return element

    def __process_js_element_list(self, elements):
        if not elements: raise Exception("JavaScript could not find element.")
        return [self.__process_single_js_element(e) for e in elements]

    def __process_js_element(self, element):
        if type(element) is list:
            element = self.__process_js_element_list(element)[0]
        else:
            element = self.__process_single_js_element(element)
        return element

    def __process_js_multielement(self, elements):
        if type(elements) is list:
            elements = self.__process_js_element_list(elements)
        else:
            elements = [self.__process_single_js_element(elements)]
        return elements

    def find_element_with_js(self, child_gui_element_setu_id, js):
        element = self.execute_javascript(js)
        element = self.__process_js_element(element)
        self.__driver_elements[child_gui_element_setu_id] = element

    def __process_multielement(self, child_gui_element_setu_id, melement):
        self.__driver_melements[child_gui_element_setu_id] = melement
        return melement.get_instance_count()

    def find_multielement(self, child_gui_element_setu_id, with_type, with_value):
        melement = MultiElement(ElementFinder.find_elements(self.__driver, with_type, with_value))
        return self.__process_multielement(child_gui_element_setu_id, melement)

    def find_multielement_with_js(self, child_gui_element_setu_id, js):
        elem_list = self.execute_javascript(js)
        elements = self.__process_js_multielement(elem_list)
        melement = MultiElement(elements)
        return self.__process_multielement(child_gui_element_setu_id, melement)

    def get_current_window_handle(self):
        return DriverCommands.get_current_window_handle(self.__driver)

    def get_current_window_title(self):
        return DriverCommands.get_window_title(self.__driver)

    def maximize_current_window(self):
        DriverCommands.maximize_window(self.__driver)

    def get_current_window_size(self):
        res = DriverCommands.get_current_window_size(self.__driver)
        return {"width" : res[0], "height" : res[1]}

    def get_all_window_handles(self):
        return DriverCommands.get_all_winodw_handles(self.__driver)

    def focus_on_window(self, handle):
        DriverCommands.focus_on_window(self.__driver, handle)

    def close_current_window(self):
        DriverCommands.close_current_window(self.__driver)

    def is_web_alert_present(self):
        return DriverCommands.is_web_alert_present(self.__driver)

    def confirm_web_alert(self):
        DriverCommands.confirm_web_alert(self.__driver)

    def dismiss_web_alert(self):
        DriverCommands.dismiss_web_alert(self.__driver)

    def get_text_from_web_alert(self):
        return DriverCommands.get_text_from_web_alert(self.__driver)

    def send_text_to_web_alert(self, text):
        DriverCommands.send_text_to_web_alert(self.__driver, text)

    def focus_on_frame(self, elem_setu_id, is_instance_action=False, instance_index=0):
        element = None
        if is_instance_action:
            element = self.__driver_melements[elem_setu_id].get_element_at_index(instance_index)
        else:
            element = self.__driver_elements[elem_setu_id]
        DriverCommands.focus_on_frame(self.__driver, element)

    def get_element_for_setu_id(self, id):
        return self.__driver_elements[id]

    def focus_on_parent_frame(self):
        DriverCommands.focus_on_parent_frame(self.__driver)

    def focus_on_dom_root(self):
        DriverCommands.focus_on_dom_root(self.__driver)

    def perform_action_chain(self, action_chain):
        DriverCommands.perform_action_chain(self, self.__driver, action_chain)


