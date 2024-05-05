# ######## 2. Программное переживание radon'a
import radon.metrics as rm
import radon.complexity as rc
import radon.raw as rw

rw.analyze(text_code)
Module(loc=143, lloc=77, sloc=77, comments=53, multi=0, blank=14, single_comments=52)

rm.h_visit(text_code)  # 1. Хольстееед
Halstead(
    total=
            HalsteadReport(
                            h1=4, 
                            h2=14, 
                            N1=8, 
                            N2=16, 
                            vocabulary=18, 
                            length=24, 
                            calculated_length=61.30296890880645, 
                            volume=100.07820003461549, 
                            difficulty=2.2857142857142856, 
                            effort=228.75017150769253, 
                            time=12.708342861538474, 
                            bugs=0.0333594000115385
            ), 
    functions=
            [
                ('__init__', HalsteadReport(h1=0, h2=0, N1=0, N2=0, vocabulary=0, length=0, calculated_length=0, volume=0, difficulty=0, effort=0, time=0.0, bugs=0.0)), 
                ('analizeMetrics', HalsteadReport(h1=1, h2=2, N1=1, N2=2, vocabulary=3, length=3, calculated_length=2.0, volume=4.754887502163469, difficulty=0.5, effort=2.3774437510817346, time=0.1320802083934297, bugs=0.0015849625007211565)), 
                ('openFileOrText', HalsteadReport(h1=1, h2=2, N1=1, N2=2, vocabulary=3, length=3, calculated_length=2.0, volume=4.754887502163469, difficulty=0.5, effort=2.3774437510817346, time=0.1320802083934297, bugs=0.0015849625007211565)), 
                ('downloadFile', HalsteadReport(h1=1, h2=2, N1=1, N2=2, vocabulary=3, length=3, calculated_length=2.0, volume=4.754887502163469, difficulty=0.5, effort=2.3774437510817346, time=0.1320802083934297, bugs=0.0015849625007211565)), 
                ('deleteItemFrmList', HalsteadReport(h1=0, h2=0, N1=0, N2=0, vocabulary=0, length=0, calculated_length=0, volume=0, difficulty=0, effort=0, time=0.0, bugs=0.0)), 
                ('addText', HalsteadReport(h1=2, h2=6, N1=4, N2=8, vocabulary=8, length=12, calculated_length=17.509775004326936, volume=36.0, difficulty=1.3333333333333333, effort=48.0, time=2.6666666666666665, bugs=0.012)), 
                ('openSecondWindow', HalsteadReport(h1=0, h2=0, N1=0, N2=0, vocabulary=0, length=0, calculated_length=0, volume=0, difficulty=0, effort=0, time=0.0, bugs=0.0))
            ]
)

rc.cc_visit(text_code)
[
    Class (name='MainWindow', lineno=8, col_offset=0, endline=124, 
           methods=
            [
                Function(name='__init__', lineno=9, col_offset=4, endline=37, is_method=True, classname='MainWindow', closures=[], complexity=1), 
                Function(name='analizeMetrics', lineno=39, col_offset=4, endline=50, is_method=True, classname='MainWindow', closures=[], complexity=3), 
                Function(name='openFileOrText', lineno=52, col_offset=4, endline=67, is_method=True, classname='MainWindow', closures=[], complexity=3), 
                Function(name='downloadFile', lineno=69, col_offset=4, endline=90, is_method=True, classname='MainWindow', closures=[], complexity=6), 
                Function(name='deleteItemFrmList', lineno=92, col_offset=4, endline=96, is_method=True, classname='MainWindow', closures=[], complexity=2), 
                Function(name='addText', lineno=100, col_offset=4, endline=120, is_method=True, classname='MainWindow', closures=[], complexity=3), 
                Function(name='openSecondWindow', lineno=123, col_offset=4, endline=124, is_method=True, classname='MainWindow', closures=[], complexity=1)
            ], 
            inner_classes=[], 
            real_complexity=20
          ), 
    Function(name='__init__', lineno=9, col_offset=4, endline=37, is_method=True, classname='MainWindow', closures=[], complexity=1), 
    Function(name='analizeMetrics', lineno=39, col_offset=4, endline=50, is_method=True, classname='MainWindow', closures=[], complexity=3), 
    Function(name='openFileOrText', lineno=52, col_offset=4, endline=67, is_method=True, classname='MainWindow', closures=[], complexity=3), 
    Function(name='downloadFile', lineno=69, col_offset=4, endline=90, is_method=True, classname='MainWindow', closures=[], complexity=6), 
    Function(name='deleteItemFrmList', lineno=92, col_offset=4, endline=96, is_method=True, classname='MainWindow', closures=[], complexity=2), 
    Function(name='addText', lineno=100, col_offset=4, endline=120, is_method=True, classname='MainWindow', closures=[], complexity=3), 
    Function(name='openSecondWindow', lineno=123, col_offset=4, endline=124, is_method=True, classname='MainWindow', closures=[], complexity=1)
]


# ######## 1. Командная CLI
# _1.
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

# _2.
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

# _3.
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

