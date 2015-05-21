# -*. coding: utf-8 -*-
# Copyright (c) 2015 CNRS and University of Strasbourg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

"""
manager - A screen manager for CEToolbox
"""

import kivy
kivy.require('1.8.0')

from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder



class MenuScreen(Screen):
    pass

class ViscosityPopup(Popup):
    pass

class InjectionPopup(Popup):
    pass

class ConductivityPopup(Popup):
    pass

class FlowPopup(Popup):
    pass

class InjectionScreen(Screen):
    def show_injection_results(self):
        self._popup = InjectionPopup()
        self._popup.open()

class ViscosityScreen(Screen):
    def show_viscosity_results(self):
        self._popup = ViscosityPopup()
        self._popup.open()


class ConductivityScreen(Screen):
    def show_conductivity_results(self):
        self._popup = ConductivityPopup()
        self._popup.open()

class FlowScreen(Screen):
    def show_flow_results(self):
        self._popup = FlowPopup()
        self._popup.open()

class AboutScreen(Screen):
    pass

class ManagerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(InjectionScreen(name='injection'))
        sm.add_widget(ViscosityScreen(name='viscosity'))
        sm.add_widget(ConductivityScreen(name='conductivity'))
        sm.add_widget(FlowScreen(name='flow'))
        sm.add_widget(AboutScreen(name='about'))
        return sm


if __name__ == '__main__':
    ManagerApp().run()
