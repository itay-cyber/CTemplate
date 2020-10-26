import argparse
import os

parser = argparse.ArgumentParser(description="Create code project templates for C++, HTML and Python")

parser.add_argument("-t", "--template", help="Defines the template that you want to make", required=True)

parser.add_argument("-asrc", "--addsrc", action="store_true", help="Choose whether or not to add a SRC folder for your project")
parser.add_argument("-cpphdir", "--cppheaderdirectory",action="store_true", help="Choose if you want to make a directory for header files (Only in C++ template)")
parser.add_argument("-ajs", "--addjavascript", action="store_true", help="Choose if you want an main.js file in your HTML template")
parser.add_argument("-hfile", "--headerfilecpp", action="store_true", help="Choose if you want to create a header file for your main source file")
parser.add_argument("-chjs", "--cssjshtml", action="store_true", help="Choose if you want a CSS-HTML-JS folder structure for your HTML template")

args = parser.parse_args()

def createCPPTemplate(isheader, toGenerateSrcFolder):
    print("Creating C++ template for directory " + os.getcwd() + ".\n\nGenerated SRC folder: " + str(toGenerateSrcFolder))
    print("To make header file: " + str(args.headerfilecpp))
    print("To make directory for header files: " + str(isheader))

    yn = input("Do these configurations look good to you? y/n: ")
    
    if (yn == "y"):
        try:
            if (toGenerateSrcFolder):
                os.mkdir("src")
                os.system("touch src/main.cpp")

            else:
                os.system("touch main.cpp")
                            
            if (isheader):
                os.system("mkdir headers")

            if (isheader and args.headerfilecpp): 
                os.system("touch headers/main.h")

            elif (args.headerfilecpp):
                os.system("touch main.h")

            print("Entering your template cli...")

            while True:
                cmd = input("\nC++ template $: ")

                if (cmd == "clear" or cmd == "cls" or cmd == "c"):
                    os.system("clear")
                
                elif (cmd == ""):
                    pass
                
                elif (cmd == "exit"):
                    print("Thank you for using CTemplate! Bye!")
                    input()
                    exit()

                else:
                    print("C++ template: command not found: " + "\"{}\"".format(cmd))

        except Exception as identifier:
            print("Failed to create template for c++. Error occured: \n")
            print(identifier)

    elif (yn == "n"):
        print("template not created")
        input()

    else:
        print("error: you didn't enter y or n. Aborted")
        exit(0)



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




