# This file is a part of Arjuna
# Copyright 2015-2021 Rahul Verma

# Website: www.RahulVerma.net

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from arjuna.tpi.helper.arjtype import Offset
import os
import platform

from browsermobproxy.exceptions import ProxyServerError

from .pageelement import PlayWrightDriverElementDispatcher
from arjuna.interact.gui.dispatcher.playwright.page_commands import PageCommands
from arjuna.interact.gui.dispatcher.playwright.element_finder import PlayWrightElementFinder
from arjuna.interact.gui.dispatcher.playwright.melement import MultiElement
from playwright import Locator
from arjuna import log_info

class HttpProxy:  # YET TO START

    def __init__(self, host, port):
        self.proxy = "{}:{}".format(host, port)

    def add_to_capabilities(self, capabilities):

        capabilities['proxy'] = {
            'proxyType': "MANUAL",
            'httpProxy': self.proxy,
            'sslProxy': self.proxy
        }

    def close(self):
        pass

class PlayWrightDriverDispatcher:  # IN PROGRESS

    def __init__(self):
        self.__config = None
        self.__page = None
        self.__proxy_server = None
        self.__proxy = None
        self.__driver_service = None

    def __create_gui_element_dispatcher(self, element):
        log_info('creating dispatcher')
        return PlayWrightDriverDispatcher.create_dispatcher(self, element)

    @property
    def driver(self):
        return self.__page

    @property
    def proxy(self):
        return self.__proxy

    def launch(self, config):
        self.__config = config
        log_info('launch...')
        from .browser_launcher import BrowserLauncher

        svc_url = config["arjuna_options"]["SELENIUM_SERVICE_URL"]
        driver_download = config["arjuna_options"]["SELENIUM_DRIVER_DOWNLOAD"]
        browser_name = config["arjuna_options"]["BROWSER_NAME"]
        driver_path = config["arjuna_options"]["SELENIUM_DRIVER_PATH"]
        # if svc_url.lower() == "not_set":
        #     from arjuna.tpi.constant import BrowserName
        #     driver_service = None
        #     driver_downloader = None
        #     if browser_name == BrowserName.CHROME:
        #         from selenium.webdriver.chrome.service import Service
        #         driver_service = Service
        #         from webdriver_manager.chrome import ChromeDriverManager
        #         driver_downloader = ChromeDriverManager
        #     elif browser_name == BrowserName.FIREFOX:
        #         from selenium.webdriver.firefox.service import Service
        #         driver_service = Service
        #         from webdriver_manager.firefox import GeckoDriverManager
        #         driver_downloader = GeckoDriverManager
        #     if driver_download:
        #         driver_path = driver_downloader().install()
        #     self.__driver_service = Service(driver_path)
        #     self.__driver_service.start()
        #     svc_url = self.__driver_service.service_url
        # else:
        #     if not svc_url.lower().endswith("/wd/hub"):
        #         svc_url += "/wd/hub"

        # BrowserMob
        from arjuna import Arjuna
        bmproxy_server = Arjuna._get_bmproxy_server()
        if bmproxy_server is not None:
            self.__proxy = bmproxy_server.create_proxy()
        else:
            from arjuna import C
            if C("http.proxy.enabled"):
                self.__proxy = HttpProxy(C('http.proxy.host'), C('http.proxy.port'))

        self.__page = BrowserLauncher.launch(config, svc_url=svc_url, proxy=self.__proxy) 

    def quit(self):
        PageCommands.quit(self.__page)
        # if self.__driver_service:
        #     self.__driver_service.stop()
        if self.__proxy:
            self.__proxy.close()

    def go_to_url(self, url):
        PageCommands.go_to_url(self.__page, url)

    def go_back_in_browser(self):
        PageCommands.go_back_in_browser(self.__page)

    def go_forward_in_browser(self):
        PageCommands.go_forward_in_browser(self.__page)

    def refresh_browser(self):
        PageCommands.refresh_browser(self.__page)

    def get_source(self):
        return PageCommands.get_source(self.__page)

    def send_keys(self, key_str):
        PageCommands.send_keys(self.__page, key_str)

    def execute_javascript(self, script, *args):
        return PageCommands.evaluate(script, 
                *[
                isinstance(arg, PlayWrightDriverElementDispatcher) and arg.driver_element or arg for arg in args
            ]
        )

    def take_screenshot(self, file_path):
        PageCommands.take_screenshot(self.__page, file_path)

    def take_screenshot_as_base64(self):
        return PageCommands.take_screenshot_as_base64(self.__page)

    def find_element(self, with_type, with_value, *, relations=None, filters=None):
        element = PlayWrightElementFinder.find_element(self.__page, with_type, with_value, relations=relations, filters=filters)
        return 1, self.__create_gui_element_dispatcher(element)

    def __process_single_js_element(self, element):
        # JS returns null, undefined
        if element is None:
            raise Exception("JavaScript could not find element.")
        elif not isinstance(element, Locator):
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

    def find_element_with_js(self, js):
        element = self.execute_javascript(js)
        element = self.__process_js_element(element)
        return 1, self.__create_gui_element_dispatcher(element)

    def find_multielement(self, with_type, with_value, *, relations=None, filters=None):
        web_elements = PlayWrightElementFinder.find_elements(self.__page, with_type, with_value, relations=relations, filters=filters)
        melement = MultiElement([PlayWrightDriverElementDispatcher(self, web_element) for web_element in web_elements])
        return melement.get_size(), melement

    def find_multielement_with_js(self, js):
        web_elements = self.execute_javascript(js)
        web_elements = self.__process_js_multielement(web_elements)
        melement = MultiElement([PlayWrightDriverElementDispatcher(self, web_element) for web_element in web_elements])
        return melement.get_size(), melement

    def get_current_window_handle(self):
        return PageCommands.get_current_window_handle(self.__page)

    def get_current_window_title(self):
        return PageCommands.get_window_title(self.__page)

    def maximize_current_window(self):
        PageCommands.maximize_window(self.__page)

    def get_current_window_size(self):
        return PageCommands.get_current_window_size(self.__page)
        
    def get_all_window_handles(self):
        return PageCommands.get_all_winodw_handles(self.__page)

    def focus_on_window(self, handle):
        PageCommands.focus_on_window(self.__page, handle)

    def close_current_window(self):
        PageCommands.close_current_window(self.__page)

    def is_web_alert_present(self):
        return PageCommands.is_web_alert_present(self.__page)

    def confirm_web_alert(self):
        PageCommands.confirm_web_alert(self.__page)

    def dismiss_web_alert(self):
        PageCommands.dismiss_web_alert(self.__page)

    def get_text_from_web_alert(self):
        return PageCommands.get_text_from_web_alert(self.__page)

    def send_text_to_web_alert(self, text):
        PageCommands.send_text_to_web_alert(self.__page, text)

    def focus_on_frame(self, element_dispatcher):
        PageCommands.focus_on_frame(self.__page, element_dispatcher.driver_element)

    def get_element_for_setu_id(self, id):
        return self.__page_elements[id]

    def focus_on_parent_frame(self):
        PageCommands.focus_on_parent_frame(self.__page)

    def focus_on_dom_root(self):
        PageCommands.focus_on_dom_root(self.__page)

    def perform_action_chain(self, action_chain):
        PageCommands.perform_action_chain(self, self.__page, action_chain)

    def hover_on_element(self, element_dispatcher):
        PageCommands.hover_on_element(self.__page, element_dispatcher.driver_element)

    def mouse_click_on_element(self, element_dispatcher):
        PageCommands.mouse_click_on_element(self.__page, element_dispatcher.driver_element)

    def double_click_on_element(self, element_dispatcher):
        PageCommands.double_click_on_element(self.__page, element_dispatcher.driver_element)

    def switch_to_frame(self, element_dispatcher):
        PageCommands.switch_to_frame(self.__page, element_dispatcher.driver_element)

    def switch_to_dom_root(self):
        PageCommands.switch_to_dom_root(self.__page)

    def drag_element(self, source_element_dispatcher, offset):
        PageCommands.drag_element(self.__page, source_element_dispatcher.driver_element, offset)

    def drop_element(self, source_element_dispatcher, target_element_dispatcher, source_offset=None, target_offset=None):
        PageCommands.drop_element(self.__page, source_element_dispatcher.driver_element, target_element_dispatcher.driver_element, source_offset, target_offset)

    def scroll_to_element(self, element_dispatcher):
        PageCommands.scroll_to_element(self.__page, element_dispatcher.driver_element)


