# module_importer.py


class ModuleCommon:
    def __init__(self):
        self.import_modules()

    def import_modules(self):
        global BaseVariable1 , BaseVariable2
        from Mod.module_class1 import BaseVariable1
        from Mod.module_class2 import BaseVariable2

    def get_module(self, module_name):
        if module_name in globals():
            return globals()[module_name]
        else:
            raise ImportError(f"Module {module_name} is not imported.")