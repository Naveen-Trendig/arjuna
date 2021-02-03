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

from arjuna import *

'''
    Try with the following switches to see different behaviors:
        -ao browser.network.recorder.enabled true
        -ao report.network.always true
'''

def __activity(config=None):
    browser = GuiApp(url="https://google.com", config=config)
    browser.launch()
    browser.network_recorder.record("Test Mile")
    browser.go_to_url("http://testmile.com")
    browser.quit()

@test
def check_filter_on(request):
    cb = request.config.builder
    cb["browser.network.recorder.automatic"] = True
    config = cb.register()

    __activity(config)
    1/0

@test
def check_filter_off(request):
    cb = request.config.builder
    cb["browser.network.recorder.automatic"] = True
    cb["report.network.filter"] = False
    config = cb.register()

    __activity(config)
    1/0