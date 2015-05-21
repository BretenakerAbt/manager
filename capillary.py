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
capillary - A class describing a capillary used in electrophoresis
"""
import math

class Capillary:
    def __init__(self, total_length = 100.0, to_window_length = 90.0,
                 diameter = 30.0, pressure = 30.0, duration = 21.0,
                 viscosity = 1.0, concentration = 21.0,
                 molecular_weight = 150000.0, voltage = 30000.0,
                 electric_current = 4.0, detection_time = 3815.0,
                 electro_osmosis_time = 100.0):
        # The length of the capillary (centimeter)
        self.total_length = total_length
        # The window length (centimeter)
        self.to_window_length = to_window_length
        # The capillary inside diameter (micrometer)
        self.diameter = diameter
        # The pressure drop across the capillary (mbar)
        self.pressure = pressure
        # The time the pressure is applied (second)
        self.duration = duration
        # The buffer viscosity (cp)
        self.viscosity = viscosity
        # Analyte concentration (mol/l)
        self.concentration = concentration
        # Analyte molecular weight (g/mol)
        self.molecular_weight = molecular_weight
        # The voltage applied to the capillary (volt)
        self.voltage = voltage
        # The current applied to the capillary (microampere)
        self.electric_current = electric_current
        # The detection time (s)
        self.detectionTime = detection_time
        # The electro-osmosis time (s)
        self.electro_osmosis_time = electro_osmosis_time


    def delivered_volume(self):
        """Add description"""
        delivered_volume = ((math.pi*(self.diameter**4)*self.pressure*self.duration)/(128*self.viscosity*self.total_length))*(10**12)
        return delivered_volume

    def capillary_volume(self):
        """Add description"""
        capillary_volume = ((math.pi*(self.diameter**2)*self.total_length)/4)*(10**12)
        return capillary_volume

    def to_window_volume(self):
        """Add description"""
        to_window_volume = ((math.pi*(self.diameter**2)*self.to_window_length)/4)*(10**12)
        return to_window_volume

    def injection_plug_length(self):
        """Add description"""
        injection_plug_length = ((math.pi*(self.diameter**2)*self.total_length)/4)*(10**12)
        return injection_plug_length

    def time_to_replace_volume_sec(self):
        """Add description"""
        time_to_replace_volume_sec = ((32*self.viscosity*(self.total_length)**2)/((self.diameter**2)*self.pressure))
        return time_to_replace_volume_sec
    
    def time_to_replace_volume_min(self):
        """Add description"""
        time_to_replace_volume_min = (((32*self.viscosity*(self.total_length)**2)/((self.diameter**2)*self.pressure))/60)
        return time_to_replace_volume_min

    def computed_viscosity(self):
        """Add description"""
        computed_viscosity = ((math.pi*(self.diameter**4)*self.pressure*self.duration)/(32*self.to_window_length*self.total_length))*(10**3)
        return computed_viscosity

    def conductivity(self):
        """Add description"""
        conductivity = (4*self.total_length*self.to_window_length)/(math.pi*(self.diameter**2)*self.voltage)
        return conductivity

    def field_strength(self):
        """Add description"""
        field_strength = (self.voltage / self.total_length)
        return field_strength

    def micro_eof(self):
        """Add description"""
        micro_eof = ((self.total_length*self.to_window_length)/(self.electro_osmosis_time*self.voltage))
        return micro_eof

    def length_per_minute(self):
        """Add description"""
        
        return 0.0

    def flow_rate(self):
        """Add description"""
        flow_rate = (self.capillary_volume())/(self.time_to_replace_volume_min())
        return flow_rate