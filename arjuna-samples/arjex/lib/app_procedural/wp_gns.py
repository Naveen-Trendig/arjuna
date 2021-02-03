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

def create_wordpress_app():
    url = C("wp.login.url")
    wordpress = GuiApp(url=url, label="WordPress", gns_dir="app_procedural")
    wordpress.launch()
    return wordpress

def login(wordpress):
    user = C("wp.admin.name")
    pwd = C("wp.admin.pwd")
    
    # Login
    wordpress.gns.user.text = user
    wordpress.gns.pwd.text = pwd
    wordpress.gns.submit.click()
    wordpress.gns.view_site

def logout(wordpress):
    url = C("wp.logout.url")
    wordpress.go_to_url(url)
    wordpress.gns.logout_confirm.click()
    wordpress.gns.logout_msg

    wordpress.quit()