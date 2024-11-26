from Mod.module_class1 import *
from Mod.module_class2 import *


class Test(BaseVariable1, BaseVariable2):

    def test_mod_class1(self):
        return self.x

    def test_mod_class2(self):
        return self.y
