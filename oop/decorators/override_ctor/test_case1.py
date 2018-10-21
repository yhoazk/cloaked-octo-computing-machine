from base_test import *

class Test(basetest):

    def setUp(self):
        self.module = "com"
        self.module_path = "/usr/com" 
        super().setUp(self.module, self.module_path)

    def test_01_setup(self):
        '''
            Here we set the specifics for this test case module name
            and path
        '''
        assert super().get_module() == "com"
        # async for target in iter:
        #     block
        # else:
        #     block 

    def test_02_path(self):
        assert super().get_path() == "/usr/com"