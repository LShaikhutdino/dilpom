radon hal mainwindow.py
    h1: 3
    h2: 10
    N1: 6
    N2: 12
    vocabulary: 13
    length: 18
    calculated_length: 37.974168451037094
    volume: 66.60791492653966
    difficulty: 1.8
    effort: 119.8942468677714
    time: 6.660791492653967
    bugs: 0.022202638308846556

radon raw mainwindow.py
    LOC: 90
    LLOC: 46
    SLOC: 46
    Comments: 34
    Single comments: 33
    Multi: 0
    Blank: 11
    - Comment Stats
        (C % L): 38%
        (C % S): 74%
        (C + M % L): 38%


radon cc mainwindow.py -s -a
-O, --output-file
    Save output to the specified output file.
    Value can be set in a configuration file using the output_file property.


    M 35:4 MainWindow.downloadFile - A (5)
    C 8:0 MainWindow - A (3)
    M 50:4 MainWindow.deleteItemFrmList - A (2)
    M 57:4 MainWindow.addText - A (2)
    M 71:4 MainWindow.openSecondWindow - A (2)
    M 9:4 MainWindow.__init__ - A (1)

6 blocks (classes, functions, methods) analyzed.
Average complexity: A (2.5)


[
    Class (name='MainWindow', lineno=8, col_offset=0, endline=76, 
           methods=
            [
                Function(name='__init__', lineno=9, col_offset=4, endline=33, is_method=True, classname='MainWindow', closures=[], complexity=1), 
                Function(name='downloadFile', lineno=35, col_offset=4, endline=48, is_method=True, classname='MainWindow', closures=[], complexity=5), 
                Function(name='deleteItemFrmList', lineno=50, col_offset=4, endline=54, is_method=True, classname='MainWindow', closures=[], complexity=2), Function(name='addText', lineno=57, col_offset=4, endline=68, is_method=True, classname='MainWindow', closures=[], complexity=2), 
                Function(name='openSecondWindow', lineno=71, col_offset=4, endline=76, is_method=True, classname='MainWindow', closures=[], complexity=2)
            ], 
           inner_classes=[], 
           real_complexity=13
          ), 
    Function(name='__init__', lineno=9, col_offset=4, endline=33, is_method=True, classname='MainWindow', closures=[], complexity=1), 
    Function(name='downloadFile', lineno=35, col_offset=4, endline=48, is_method=True, classname='MainWindow', closures=[], complexity=5), 
    Function(name='deleteItemFrmList', lineno=50, col_offset=4, endline=54, is_method=True, classname='MainWindow', closures=[], complexity=2), 
    Function(name='addText', lineno=57, col_offset=4, endline=68, is_method=True, classname='MainWindow', closures=[], complexity=2), 
    Function(name='openSecondWindow', lineno=71, col_offset=4, endline=76, is_method=True, classname='MainWindow', closures=[], complexity=2)
]