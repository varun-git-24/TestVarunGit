# from Mod.module_class1 import *
# from Mod.module_class2 import *
from Mod.common_mod import ModuleCommon


class Test():

    def best(self):
        return ModuleCommon.module_class1.BaseVariable1.x


o = Test()
print(o.best())