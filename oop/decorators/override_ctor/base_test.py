import unittest

class base:
    def __init__(self):
        self.base_id = 1

class basetest(unittest.TestCase):
    @classmethod
    def setUp(self, module="test", path="/usr/bin"):
        self.moudule_name = module
        self.path_to_obj = path
        print("Path {} Module: {}".format(path, module))


    def get_module(self):
        return self.moudule_name

    def get_path(self):
        return self.path_to_obj
