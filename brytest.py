from browser import timer
    
class InputNext:
    def __init__(self, prompt, next):
       self.prompt = prompt
       self.next = next
       self.result = None
       print(prompt, end="")
       timer.set_timeout(self._wait_first, 0)
    
    def _wait_first(self):
        self.result = input()
        timer.set_timeout(self._wait_second, 0)
    
    def _wait_second(self):
        self.next(self.result)
    

def handlein_1(inp):
    print("we received input 1: ", inp)
    InputNext("give me input (2)", handlein_2)
    
def handlein_2(inp):
    print("we received input 2: ", inp)
        
InputNext("give me input (1)", handlein_1)
