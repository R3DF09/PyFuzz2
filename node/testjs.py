import random
from fuzzing.browser.browser_fuzzer import BrowserFuzzer


random.seed(0)

fuzzer = BrowserFuzzer(5,2,10,10,'2d', 1,10,'html')

with open("test.html", 'wb+') as fd:
    fd.write(fuzzer.fuzz()[0])
