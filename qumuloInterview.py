import os
import struct
import sys
import unittest
import io


def produce(filename):
    """This should take a filename and make three files that meet the
    assignment's criteria. Return the output filenames.

The seperation will look like the following;
    # File1 25 bytes + (0 - 66% of file) (Beginning -> Middle)
    # File2 20 bytes + (33% - 100%) (Middle -> End)
    # File3 8 bytes + (0 - 33%) + (66% - 100%) (Beginning + End)

    Parameters
    ----------
    filename : str
        The corresponding important client document.


    Returns
    -------
    tuple
        Three files that are a split version of the original document.
    """


    emp_file_1 = "Employee_1_file"
    emp_file_2 = "Employee_2_file"
    emp_file_3 = "Employee_3_file"
    if (getSize(filename)) >= 25:
        with open(filename, "r+") as in_file, open(emp_file_1, "a+") as ef1, open(emp_file_2, "a+") as ef2, open(emp_file_3, "a+") as ef3:
            ef1.write(in_file.read(25))
            in_file.seek(0)

            ef2.write(in_file.read(20))
            in_file.seek(0)

            ef3.write(in_file.read(8))

            in_file.seek(0)
            ef1.write(in_file.read(int(2/3 * getSize(filename))))

            in_file.seek(int(1/3 * getSize(filename)))
            ef2.write(in_file.read())

            in_file.seek(0)
            ef3.write(in_file.read(int(1/3 * getSize(filename))))
            in_file.seek(int(2/3 * getSize(filename)))
            ef3.write(in_file.read())
    return emp_file_1, emp_file_2, emp_file_3

                
def increaseFileSize(filename):
    """Function that accepts a file and inserts a byte

    Parameters
    ----------
    filename : str
        The corresponding important client document or one of the three split employee files.
    

    Returns
    -------
    void
    """


    with open(filename, "ab") as in_file:
        in_file.write(" ".encode('utf8'))
        
def checkFileSize(filename):
    """Function that accepts a file and check its size (in bytes) until it's divisible by 3

    Parameters
    ----------
    filename : str
        The corresponding important client document or one of the three split employee files.
    

    Returns
    -------
    void
    """


    fileSize = getSize(filename)
    while (fileSize % 3) != 0:
        increaseFileSize(filename)
        fileSize = getSize(filename)


def combine(filename1, filename2):
    """This should take any two binary input files from produce and recreate
    the original data. Return the output filename.

    Parameters
    ----------
    filename1 : str
        One of the three split employee files.
    filename2 : str
        One of the three split employee files.
    

    Returns
    -------
    Name of assembled document : str
    """

    
    if getSize(filename1) > getSize(filename2):
        if(getSize(filename1) - getSize(filename2)) == 5:
            return mergeAlgo1_2(filename1, filename2)

        elif (getSize(filename1) - getSize(filename2)) == 17:
            return mergeAlgo1_3(filename1, filename2)

        elif (getSize(filename1) - getSize(filename2)) == 12:
            mergeAlgo2_3(filename1, filename2)
        
        else:
            return False

    else:
        if(getSize(filename2) - getSize(filename1)) == 5:
            return mergeAlgo1_2(filename2, filename1)

        elif (getSize(filename2) - getSize(filename1)) == 17:
            return mergeAlgo1_3(filename2, filename1)

        elif (getSize(filename2) - getSize(filename1)) == 12:
            return mergeAlgo2_3(filename2, filename1)
        else:
            return False


def confirmFile(original, merged):
    """This should take any both 
    the original data and final assembled data. Confirm that they're both the same content and size.

    Parameters
    ----------
    original : str
        The original client file.
    merged : str
        The final assembled file from the 2/3 split employee files.
    

    Returns
    -------
    Confirmation if they're the same file : boolean
    """


    if(getSize(original) == getSize(merged)):
        with open(original, 'r+') as f1, open(merged, 'r+') as f2:
            data1 = f1.read()
            data2 = f2.read()
            if data1 == data2:
                return True
            else:
                return False
    return False


def mergeAlgo1_2(f1, f2):
    """This runs the 1st file and 2nd file through the merging algorithm.
    Following suit:
    File1 25 bytes + (0 - 66% of file) (Beginning -> Middle)
    File2 20 bytes + (33% - 100%) (Middle -> End)
    
    The goal is the merge the entire 1st file's content with the final portion of the 2nd file.

    Parameters
    ----------
    f1 : str
        One of the three split employee files.
    f2 : str
        One of the three split employee files.
    

    Returns
    -------
    Name of assembled document : str
    """


    with open(f1, 'r+') as f_1, open(f2, 'r+') as f_2, open('clientsAssembledProduct', 'a+') as clientDoc:
         totalSize = ((getSize(f1) - 25) * 3) / 2
         f_1.seek(25)
         clientDoc.write(f_1.read())
         f_2.seek(20+(1/3*totalSize))
         clientDoc.write(f_2.read())
    return 'clientsAssembledProduct'


def mergeAlgo1_3(f1, f2):
    """This runs the 1st file and 2nd file through the merging algorithm.
    Following suit:
    File1 25 bytes + (0 - 66% of file) (Beginning -> Middle)
    File2 8 bytes + (0-33% + 66-100%) (Beginning + End)
    
    The goal is the merge the entire 1st file's content with the final portion of the 2nd file.

    Parameters
    ----------
    f1 : str
        One of the three split employee files.
    f2 : str
        One of the three split employee files.
    

    Returns
    -------
    Name of assembled document : str
    """
    with open(f1, 'r+') as f_1, open(f2, 'r+') as f_2, open('clientsAssembledProduct', 'a+') as clientDoc:
         totalSize = ((getSize(f1) - 25) * 3) / 2
         f_1.seek(25)
         clientDoc.write(f_1.read())
         f_2.seek(8+(1/3*totalSize))
         clientDoc.write(f_2.read())
    return 'clientsAssembledProduct'


def mergeAlgo2_3(f1, f2):
    """This runs the 1st file and 2nd file through the merging algorithm.
    Following suit:
    File1 20 bytes + (66-100% of file) (Beginning -> Middle)
    File2 8 bytes + (0-33% + 66-100%) (Beginning + End)
    
    The goal is the merge the entire 2nd file's content with the first portion of the 1st file.

    Parameters
    ----------
    f1 : str
        One of the three split employee files.
    f2 : str
        One of the three split employee files.
    

    Returns
    -------
    Name of assembled document : str
    """


    with open(f1, 'r+') as f_1, open(f2, 'r+') as f_2, open('clientsAssembledProduct', 'a+') as clientDoc:
         totalSize = ((getSize(f1) - 20) * 3) / 2
         f_2.seek(8)
         data = 1/3 * totalSize
         clientDoc.write(f_2.read(int(data)))
         f_1.seek(20)
         clientDoc.write(f_1.read())
    return 'clientsAssembledProduct'

def getSize(filename):
    """Return the size of a file (bytes)

    Parameters
    ----------
    filename : str
        Any file.
    

    Returns
    -------
    Size of file : int
    """


    st = os.stat(filename)
    return st.st_size

def run(filename):
    """
    Basic function that runs the logic of the program from main.
    """
 
    truncateFiles()
    checkFileSize(filename)
    produce(filename)
    combine('Employee_1_file', 'Employee_2_file')
    print(confirmFile(filename,'clientsAssembledProduct'))
    print("Success")


def truncateFiles():
    """
    Function that clears all the relevant files.
    """


    deleteContent('clientsAssembledProduct')
    deleteContent('Employee_1_file')
    deleteContent('Employee_2_file')
    deleteContent('Employee_3_file')

def deleteContent(fName):
    """
    Helper function that opens and truncates files content.
    """


    with open(fName, "w"):
        pass

def main():
    """
    Main function()
    """


    if len(sys. argv) > 1:
        filename = argv[1]
        checkFileSize(filename)
    else:
        filename = input("Enter the name of the document you wish to split: ")
        if os.path.isfile(filename):
            checkFileSize(filename)
        else:
            return False
    run(filename)


class TestMe(unittest.TestCase):
    def testMerge1_2(self):
        truncateFiles()
        filename = 'testDocument.txt'
        checkFileSize(filename)
        produce(filename)
        combine('Employee_1_file', 'Employee_2_file')
        self.assertEqual(True, confirmFile(filename,'clientsAssembledProduct'))

    def testMerge1_3(self):
        truncateFiles()
        filename = 'binaryFile.txt'
        checkFileSize(filename)
        produce(filename)
        combine('Employee_1_file', 'Employee_3_file')
        self.assertEqual(True, confirmFile(filename,'clientsAssembledProduct'))
    
    def testMerge2_3(self):
        truncateFiles()
        filename = 'numbers.txt'
        checkFileSize(filename)
        produce(filename)
        combine('Employee_2_file', 'Employee_3_file')
        self.assertEqual(True, confirmFile(filename,'clientsAssembledProduct'))




if __name__ == "__main__":
    #unittest.main()
    main()


