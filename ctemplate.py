import argparse
import os

parser = argparse.ArgumentParser(description="Create code project templates for C++, HTML and Python")

parser.add_argument("-t", "--template", help="Defines the template that you want to make", required=True)

parser.add_argument("-asrc", "--addsrc", action="store_true", help="Choose whether or not to add a SRC folder for your project")
parser.add_argument("-cpphdir", "--cppheaderdirectory",action="store_true", help="Choose if you want to make a directory for header files (Only in C++ template)")
parser.add_argument("-ajs", "--addjs", action="store_true", help="Choose if you want an main.js file in your HTML template")
parser.add_argument("-hfile", "--headerfilecpp", action="store_true", help="Choose if you want to create a header file for your main source file")

args = parser.parse_args()

def createCPPTemplate(isheader, toGenerateSrcFolder):
    print("Creating C++ template for directory " + os.getcwd() + ". Generated SRC folder: " + str(toGenerateSrcFolder))

    try:
        if (toGenerateSrcFolder):
            os.mkdir("src")
            os.system("touch src/main.cpp")

        else:
            os.system("touch main.cpp")
                         
        if (isheader):
            os.system("mkdir headers")

        if (isheader and args.headerfilecpp): 
            os.system("cd headers & touch main.h")

        elif (args.headerfilecpp):
            os.system("touch main.h")

    except expression as identifier:
        print("Failed to create template for c++")
        print(identifier)

def createPythonTemplate(toGenerateSrcFolder):
    print("Python TEMPLATE")

def createHTMLTemplate(withJS,toGenerateSrcFolder):
    print("HTML TEMPLATE")


if (args.template):

    args.template = args.template.lower()

    if (args.template == "html"):
        createHTMLTemplate(args.addjs, args.addsrc)
    
    elif (args.template == "c++" or args.template == "cpp"):
        createCPPTemplate(args.cppheaderdirectory, args.addsrc)

    elif (args.template == "py" or args.template == "python" or args.template == "python3"):
        createPythonTemplate(args.addsrc)




