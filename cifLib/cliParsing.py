import cifLib.miscellaneous as misc
import cifLib.helpL as hlp
import sys
import os.path

preAccOpts = [ ['-h', '--help'],
               ['--sampleFmt'],
               ['--tee'],
               ['-l', '--log'],
               ['-N', '--noNone'],
               ['-c', '--count'],
               ['-p', '--print'],
               ['-n'],
               ['-a', '--append'],
               ['-H', '--header'] ]

accOpts=[ee for e in preAccOpts for ee in e]

def catchForeignOpts(myOptDict):
    for opt in myOptDict:
        if opt not in accOpts:
            sys.stderr.write("error: %s is not an implemented option\n" %(opt))
            sys.exit()

def getPrefDict(preAccOpts):
    """Returns a dictionary with the preferred option forms, those are the
first elements of preAccOpts

    """
    prefDict = {}
    for pL in preAccOpts:
        for p in pL:
            prefDict[p] = pL[0]

    return prefDict

def getPrefOptDict(myOptDict, preAccOpts):
    prefD = getPrefDict(preAccOpts)#A dictionary for using the preferred forms
    newOptDict = {}
    for e in myOptDict:
        if e in prefD:
            newOptDict[prefD[e]] = myOptDict[e]
    return newOptDict

def getMyOptDict(myArgs):
    myOptDict={}
    tmpOpt=''
    for i in range(len(myArgs)):
        e=myArgs[i]
        if e == '':#makes some scripting easier (empty strings)
            continue
        if e[0] == '-' and not misc.isFloat(e) and not e == '-':
            #only changes if new option is found negative numbers are
            #not options also the lone '-' is not an option
            if e not in myOptDict:
                myOptDict[e]=[]
            tmpOpt=e
            continue #Just skipping the option
        if tmpOpt == '':
            #Ignoring for now everything that is not an option
            continue

        myOptDict[tmpOpt].append(myArgs[i])

    return myOptDict

def getMyOptDict1(myArgs):
    myOptDict0 = getMyOptDict(myArgs)
    catchForeignOpts(myOptDict0)
    myPrefOptDict = getPrefOptDict(myOptDict0, preAccOpts)
    myProcOptDict = pOD(myPrefOptDict)
    return myProcOptDict

def getRefactoredOptDict(mOD):
    """Just refactors the option dictionary into a nicer form"""
    if '-l' in mOD:
        mOD['-l'] = mOD['-l'][0]

    return mOD

def checkIfValidOpts(myOptDict, accOpts):
    """Just checks if the options are valid."""
    for e in myOptDict:
        #Will leave as is for now
        if e not in accOpts:
            print("error: %s is not a valid option" %(e))
            return False

    return True

def getParsedSignals(myArgs, optD):
    """Will return values, given the arguments, handled by another function"""
    if len(myArgs) == 1:
        """Print help"""
        return 1
    if '-h' in optD:
        """Print extended help"""
        return 100
    if '--sampleFmt' in optD:
        """Giving sample text for a fmtFile"""
        return 1000
    if '-c' in optD:
        """Counting the cif files within inPath"""
        if len(myArgs) < 3:
            """There has to be at least 2 arguments (inPath and -c)"""
            return 30
        inPath = myArgs[1]
        if not os.path.exists(inPath):
            """The inPath has to exist"""
            return 3
        return 0 #Ok to move forward

    if '-n' in optD:
        """The enumerate option"""
        if '-p' not in optD:
            """It has to be used with the -p option"""
            return 210
        if len(optD['-n']) != 0:
            """No arguments should be used"""
            return 211

    if '-p' in optD:
        """Counting the cif files within inPath"""
        if len(myArgs) < 3:
            """There has to be at least 2 arguments (inPath and -p)"""
            return 60
        inPath = myArgs[1]
        if not os.path.exists(inPath):
            """The inPath has to exist"""
            return 3
        return 0 #Ok to move forward

    if len(myArgs) < 4:
        """We need the 3 filenames as arguments"""
        return 2
    inPath,fmtFile,outCsv=myArgs[1:4]
    if not os.path.exists(inPath):
        """The inPath has to exist"""
        return 3
    if not os.path.exists(fmtFile):
        """The fmtFile has to exist"""
        return 4
    if not os.path.isfile(fmtFile):
        """The fmtFile has to be a regular file"""
        return 5

    if not outCsv.endswith(".csv") and outCsv != '-':
        """The outCsv has to be a .csv file or a - for stdout"""
        return 6

    if '-l' in optD:
        """The log option"""
        if len(optD['-l']) != 1:
            """There should be exactly one argument"""
            return 20

    if '-a' in optD:
        """The append option"""
        if len(optD['-a']) != 0:
            """No arguments are accepted"""
            return 40

    if '-H' in optD:
        """The header option"""
        if len(optD['-H']) != 0:
            """No arguments are accepted"""
            return 50

    if '-N' in optD:
        """Avoid None lines"""
        if len(optD['-N']) != 0:
            """No arguments are accepted"""
            return 300

    return 0

def pOD(mOD):
    """Receives the option dictionary assigns the proper values for each
option, it processes them"""
    if '-h' in mOD:
        pass

    # if '-f' in mOD:
    #     if len(mOD['-f']) != 1:
    #         print("error: -f needs a single argument")
    #         sys.exit()

    return mOD
