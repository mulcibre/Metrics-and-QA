#   external library which allows cmd calls
from subprocess import call
import os

pathToPlotter = ["../gnuplot/","barplot.plt"]
origDir = "original/"

###
#   Function Section
###

def getLineOfData(file, cursor, anchor):
    #   scan for anchor, if found return next line which should have data
    for i in range(cursor[0], len(file)):
        if file[i].count(anchor):
            cursor[0] = i + 1
            return cursor[0]

    #   couldn't find anchor, something bad happened
    print "could not find string to match: " + anchor
    exit(-1)

def editPlotFile(plotFileLines, pngName, title, ylabel, dataCol):
    #   use cursor to scan file lines for correct anchors
    cursor = [0]

    #   Set name of output png
    lineNo = getLineOfData(plotFileLines, cursor, "define output")
    plotFileLines[lineNo + 1] = "".join(['set output "pngout/', pngName, 'barplot.png"\n'])

    #   Set title and ylabel of plot
    lineNo = getLineOfData(plotFileLines, cursor, "set title, labels, key position")
    plotFileLines[lineNo] = "".join(['set title "', title, '"\n'])
    plotFileLines[lineNo + 1] = "".join(['set ylabel "<-- ', ylabel, ' -->"\n'])

    #   set data to use
    lineNo = getLineOfData(plotFileLines, cursor, "plot barplot")
    plotFileLines[lineNo + 1] = "".join(['1:', str(dataCol), ':xtic(3) \\\n'])

def genPlot(pngName, title, ylabel, dataCol):
    #   open backup read file to avoid destruction by writing
    with open("".join([pathToPlotter[0], origDir, pathToPlotter[1]]), 'r') as file:
        # read a list of lines into source code
        plotData = file.readlines()

    #   make necessary changes to Gnuplot script
    editPlotFile(plotData, pngName, title, ylabel, dataCol)

    #   write lines back to appropriate plot file in gnuplot directory
    with open("".join([pathToPlotter[0],pngName,".plt"]), 'w') as file:
        #   write back to gnuplot file
        file.writelines(plotData)

    #   Switch to working dir to /Gnuplot, and run gnuplot on appropriate plot file
    CWD = os.getcwd()
    os.chdir(os.path.join(CWD, pathToPlotter[0]))
    call(["gnuplot", "".join([pngName,".plt"])])

    #   return to original directory
    os.chdir(CWD)

###
#   Execution Section
###

genPlot("cost", "Cost Required for Project", "Cost ($)", "4")
genPlot("staff", "Staff Required for Project", "Staff", "5")
genPlot("time", "Development Time Required for Project", "Time (Months)", "6")
genPlot("KLLOC", "Project KLLOC", "KLLOC", "7")