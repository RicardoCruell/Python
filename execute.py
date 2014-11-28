import os

Series = ['fileConstruct','kwOnFile','noRepeat','plotlyTest2']

i = 0
for s in Series:
    if i == 1:
        runFile = s + ".py > error.txt"
    else:
        runFile = s + ".py"
	os.system(runFile)
    