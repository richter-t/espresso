#
# Copyright (C) 2013,2014 The ESPResSo project
#  
# This file is part of ESPResSo.
#  
# ESPResSo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# ESPResSo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 
#  
# Tests particle property setters/getters
import espressomd
import unittest as ut
import numpy as np
from espressomd import electrostatics
from espressomd.electrostatics import *

class MMM2D_test(ut.TestCase):
    es=espressomd.System()
    cs=es.cell_system
    cs.set_layered(3)
    test_params={}
    test_params["bjerrum_length"]=2
    test_params["maxPWerror"]=1e-4
    test_params["far_cut"] = 3
    test_params["far_calculated"]=1
    test_params["dielectric"] = 0
    test_params["dielectric_contrast_on"] = 0
    test_params["const_pot_on"] = 0
    test_params["pot_diff"] = 0
    test_params["delta_mid_top"] = 0
    test_params["delta_mid_bot"] = 0

    def runTest(self):
        mmm2d=MMM2D(bjerrum_length=self.test_params["bjerrum_length"], maxPWerror=self.test_params["maxPWerror"], dielectric=self.test_params["dielectric"],  dielectric_contrast_on=self.test_params["dielectric_contrast_on"], const_pot_on=self.test_params["const_pot_on"], delta_mid_top=self.test_params["delta_mid_top"], delta_mid_bot=self.test_params["delta_mid_bot"], far_cut=self.test_params["far_cut"])
        self.es.actors.add(mmm2d)
        set_params=mmm2d._getParamsFromEsCore()
        print set_params
        SAME=True
        for i in self.test_params.keys():
            if set_params[i] != self.test_params[i]:
                print "Parameter mismatch: ", i, " ", set_params[i]
                SAME=False
                break
        return SAME

if __name__ == "__main__":
 print("Features: ",espressomd.features())
 ut.main()
