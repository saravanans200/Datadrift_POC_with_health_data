import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import schedule 
import time 

print("started")
def func(): 
    print("started")
    filename = 'src/result.ipynb'
    with open(filename) as ff:
        nb_in = nbformat.read(ff, nbformat.NO_CONVERT)    
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    nb_out = ep.preprocess(nb_in)
  
schedule.every(1).minutes.do(func) 
  
while True: 
    schedule.run_pending() 
    time.sleep(1)