import os
import sys
import datetime

thisFileName = os.path.abspath(os.path.dirname(sys.argv[0]))
print('\nRunning init file from folder ' + thisFileName +  ' \nPython Version: ' + sys.version + '\n')

#CommandsList = { 'slCd' : 'lambda d: os.chdir(d)', \
#                              'slClear' : 'lambda: os.system("cls") or None',\
#                              'slRun' : 'lambda myPyFile: execfile(myPyFile)'\
#                              }
                              
                              
class Prompt():
    def __str__(self):
        
        return 'python' + \
               sys.version[0:sys.version.index(' ')] + ': ' + \
               str(datetime.datetime.now().time().isoformat()[:8]) + \
               '>\n   '

sys.ps1 = Prompt()                              
#myPrompt = sys.version[:6]
#sys.ps1 = myPrompt.strip() + '>   '
slCd =  lambda d: os.chdir(d) 
slClear = lambda: os.system("cls") or None

if float(sys.version[:3]) < 3.0:
    slRun = lambda myPyFile: execfile(myPyFile)
else:
    print('Please run the command:')
    print('    slRun = lambda myPyFile: exec(open(myPyFile).read())')
    print('from the shell!')
#...  if float(sys.version[:3]) < 3.0:  .....................................................................
print()
print('Following commands instantiated:\n slCd, slClear\n\n')
