from browser import timer

class NextWrapper:
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg

    def delayed(self):
        self.func(self.arg)
        
    def go(self):
        timer.set_timeout(self.delayed, 100)

"""
def inputnext(arg, next):
    strin = input(arg)
    n = NextWrapper(next, strin)
    n.go()
    #time.set_timeout(next, 1)
    #t = threading.Thread(target = next, args=(strin,))
    #t.start()
"""
    
class InputNext:
    def __init__(self, prompt, next):
       self.prompt = prompt
       self.next = next
       self.result = None
       print(prompt, end="")
       timer.set_timeout(self.waitfirst, 0)
    
    def waitfirst(self):
        self.result = input()
        timer.set_timeout(self.waitsecond, 0)
    
    def waitsecond(self):
        self.next(self.result)
    


def handlein_1(inp):
    print("we received input 1: ", inp)
    InputNext("give me input (2)", handlein_2)
    
def handlein_2(inp):
    print("we received input 2: ", inp)
        
InputNext("give me input (1)", handlein_1)
