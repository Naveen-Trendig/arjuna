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

class PageElementCommands: # IN PROGRESS

    @classmethod
    def send_text(cls, element, text):
        element.type(text)

    @classmethod
    def clear_text(cls, element):
        # sending empty string will empty the value
        element.fill("")

    @classmethod
    def submit(cls, element):
        # element.submit()
        # no such method.
        pass

    @classmethod
    def click(cls, element):
        element.click()

    @classmethod
    def get_text_content(cls, element):
        return element.text_content()

    @classmethod
    def get_attr_value(cls, element, attr):
        return element.get_attribute(attr)

    @classmethod
    def get_tag_name(cls, element):
        # no method
        pass

    @classmethod
    def is_visible(cls, element):
        return element.is_visible()

    @classmethod
    def is_clickable(cls, element):
        return element.is_enabled()

    @classmethod
    def is_selected(cls, element):
        return element.is_checked()