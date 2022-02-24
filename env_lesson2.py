#python 注册器模式

from dataclasses import dataclass
class Register:
    _module_dict = dict()


    def _register(self,cls):
        self._module_dict[cls.__name__] = cls
        return cls

    def __call__(self, cls):
        self._register(cls)

    def get_module(self,name:str):
        return self._module_dict[name]

if __name__ == '__main__':
    myregister = Register()
    @myregister
    class Test:
        counter:int = 1

    print(myregister.get_module('Test').counter)


