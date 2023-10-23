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



class PageCommands:  # IN PROGRESS

    # Page is similar to Driver in Selenium. in PlayWright Page refers to a browsre tab.
    #  Selenium           PlayWright
    #  Driver             Browser > BrowserContext > Page
    #  WebElement         Locator


    @classmethod
    def go_to_url(cls, page, url):
        page.goto(url)

    @classmethod
    def refresh_browser(cls, page):
        page.reload()

    @classmethod
    def go_back_in_browser(cls, page):
        page.go_back()

    @classmethod
    def go_forward_in_browser(cls, page):
        page.go_forward()

    @classmethod
    def quit(cls, page):
        page.close()

    @classmethod
    def get_page_title(cls, page):
        return page.title()

    @classmethod
    def get_url(cls, page):
        return page.url

    @classmethod
    def get_source(cls, page):
        return page.content()

    # method definition is different from selenium
    @classmethod
    def send_keys(cls, page, locator, key_str):
        page.press(locator, key_str)

    @classmethod
    def is_web_alert_present(cls, page):
        # pending
        pass

    @classmethod
    def confirm_web_alert(cls, page):
        page.on("dialog", lambda dialog: dialog.accept())

    @classmethod
    def dismiss_web_alert(cls, page):
        page.on("dialog", lambda dialog: dialog.dismis())

    @classmethod
    def send_text_to_web_alert(cls, page, text):
        # pending
        pass

    @classmethod
    def get_text_from_web_alert(cls, page):
        # pending
        pass

    @classmethod
    def focus_on_frame(cls, page, element):
        # pending
        pass

    @classmethod
    def focus_on_dom_root(cls, page):
        # pending
        pass

    @classmethod
    def focus_on_parent_frame(cls, page):
        # pending
        pass

    @classmethod
    def execute_javascript(cls, page, script, *args):
        from arjuna import log_debug
        log_debug("Executing JavaScript {} with args {}.".format(script, args))
        return page.evaluate(script, *args)

    @classmethod
    def take_screenshot(cls, page, file_path):
        return page.screenshot(path=file_path)

    @classmethod
    def take_screenshot_as_base64(cls, page):
        # pending
        pass

    @classmethod
    def set_window_size(cls, page, width, height):
        page.set_viewport_size({"width": width, "height": height})

    @classmethod
    def maximize_window(cls, page):
        # pending
        pass

    @classmethod
    def get_current_window_handle(cls, page):
        # pending
        pass

    @classmethod
    def focus_on_window(cls, page, window_handle):
        # pending
        pass

    @classmethod
    def close_current_window(cls, page):
        page.close()

    @classmethod
    def get_window_title(cls, page):
        return page.title()

    @classmethod
    def get_current_window_size(cls, page):
        # return Dict
        return page.viewport_size

    @classmethod
    def get_all_winodw_handles(cls, page):
        # pending
        pass

    @classmethod
    def replace_with_element(cls, setu_page, value_tuple):
        if value_tuple[1] == True:
            return setu_page.get_element_for_setu_id(value_tuple[0])
        else:
            return value_tuple[0]
        
    @classmethod
    def perform_action_chain(cls, setu_page, page, action_chain):
        # pending
        pass

    @classmethod
    def hover_on_element(cls, page, webelement):
        # **kwargs can be passed to hover method. needs an expansion.
        page.hover(webelement)

    @classmethod
    def mouse_click_on_element(cls, page, webelement):
        chain = ActionChains(page).click(webelement).perform()

    @classmethod
    def double_click_on_element(cls, page, webelement):
        chain = ActionChains(page).double_click(webelement).perform()

    @classmethod
    def drag_element(cls, page, source_element, offset):
        ActionChains(page).click_and_hold(source_element).move_by_offset(offset.x, offset.y).pause(3).release().perform(0)

    @classmethod
    def drop_element(cls, page, source_element, target_element, source_offset=None, target_offset=None):
        if source_offset is None:
            source_offset = (0,0)
        else:
            source_offset = (source_offset.x,source_offset.y)

        if target_offset is None:
            target_offset = (0,0)
        else:
            target_offset = (target_offset.x,target_offset.y)

        ActionChains(page).click_and_hold(source_element).move_by_offset(200, 50).move_to_element(target_element).pause(3).release().perform()

    @classmethod
    def scroll_to_element(cls, page, webelement):
        cls.execute_javascript(page, "arguments[0].scrollIntoView(true);", webelement)

    def switch_to_frame(page, webelement):
        page.switch_to.frame(webelement)

    def switch_to_dom_root(page):
        page.switch_to.default_content()
