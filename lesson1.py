from dataclasses import dataclass

@dataclass
class _:
    counter: int = 1

    def __call__(this, cls):

            class CLO(cls):
                def __init__(self):
                    if this.counter == 1:
                        this.counter -= 1
                        super().__init__()
                    else:
                        print('fail')

            return CLO



@_()
class SIM:

    def __init__(self):
        print("success")


res = []
for i in range(5):
    SIM()
