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

@test
def check_hook_conf(request):
    '''
        For this test:
            - arjuna_config.py hook module's register_ref_confs hook creates a hook_conf configuration.
            - Use -c hook_conf switch to run.
    '''

    assert Arjuna.get_config("hook_conf").test_value == 123

    assert C("hook_conf.test_value") == 123


@test
def check_hook_conf_as_ref(request):
    '''
        For this test:
            - arjuna_config.py hook module's register_ref_confs hook creates a hook_conf configuration.
            - Use -c hook_conf switch to run.
    '''

    assert Arjuna.get_config().test_value == 123
    assert Arjuna.get_config("ref").test_value == 123

    assert C("test_value") == 123
    assert C("ref.test_value") == 123