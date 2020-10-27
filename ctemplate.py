import argparse
import os
import sys

parser = argparse.ArgumentParser(description="Create code project templates for C++, HTML and Python")

parser.add_argument("-t", "--template", help="Defines the template that you want to make", required=True)

parser.add_argument("-asrc", "--addsrc", action="store_true", help="Choose whether or not to add a SRC folder for your project")
parser.add_argument("-cpphdir", "--cppheaderdirectory",action="store_true", help="Choose if you want to make a directory for header files (Only in C++ template)")
parser.add_argument("-ajs", "--addjavascript", action="store_true", help="Choose if you want an main.js file in your HTML template")
parser.add_argument("-hfile", "--headerfilecpp", action="store_true", help="Choose if you want to create a header file for your main source file")
parser.add_argument("-chjs", "--cssjshtml", action="store_true", help="Choose if you want a CSS-HTML-JS folder structure for your HTML template")

args = parser.parse_args()

def enterCLI(templateType):
    while True:
        cmd = input("\n{} $: ".format(templateType)).split(" ")

        if (cmd[0] == "cls" or cmd[0] == "clear"):

            os.system("cls") if sys.platform == "win32" else os.system("clear")

        elif (cmd[0] == "sysplatform"):

            print(sys.platform)

        
        if ("C++" in templateType):

            if (cmd[0] == "new" and cmd[1] == "header-source"):
                
                if (input("Create a new source file with a header? ({}) y/n: ".format(cmd[2]).lower()) == "y"):
                    
                    if (os.path.exists(os.getcwd() + "/src")):
                        os.system("touch src/{}".format(cmd[2]))
                    
                    else:
                        os.system("touch {}".format(cmd[2]))
                    
                    if (os.path.exists(os.getcwd() + "/headers")):
                        os.system("touch headers/{}".format(str(cmd[2])[0:len(cmd[2]) - 4] + ".h"))

                    else:
                        os.system("touch {}".format(str(cmd[2])[:2] + ".h"))
                    

                    print("Added new source file and header file. ({})".format(cmd[2]))
                else:   
                    print("Not created. ")
                    continue        
        
        if ("Python" in templateType):

            if (cmd[0] == "new" and cmd[1] == "pyfile"):

                if (input("Create a new python file? y/n: ").lower() == "y"):
                    
                    if (os.path.exists(os.getcwd() + "/src")):
                        os.system("touch src/{}".format(str(cmd[2])))
                    
                    else:
                        os.system("touch {}".format(str(cmd[2])))

                else:
                    print("Not created. ")
                    continue        

def createCPPTemplate(isheader, toGenerateSrcFolder):
    print("Creating C++ template for directory " + os.getcwd() + ".\n\nGenerated SRC folder: " + str(toGenerateSrcFolder))
    print("To make header file: " + str(args.headerfilecpp))
    print("To make directory for header files: " + str(isheader))

    yn = input("Do these configurations look good to you? y/n: ").lower()

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


            print("template created...\n")
            
            enter = input("Would you like to enter your template CLI? y/n: ")
            enter = enter.lower()

            enterCLI("C++ template ") if enter == "y" else exit(0)


        except Exception as e:
            print("Failed to create template for c++. Error occured: \n")
            print(e)

    elif (yn == "n"):
        print("template not created")
        input()

    else:
        print("error: you didn't enter y or n. Aborted")
        exit(0)



def createPythonTemplate(toGenerateSrcFolder):
        print("Creating Python template for directory " + os.getcwd() + ".\n\nGenerated SRC folder: " + str(toGenerateSrcFolder))

        yn = input("Do these configurations look good to you? y/n: ").lower()

        if (yn == "y"):
            try:
                if (toGenerateSrcFolder):
                    os.mkdir("src")
                    os.system("touch src/main.py")

                else:
                    os.system("touch main.py")


                print("template created...\n")
                
                enter = input("Would you like to enter your template CLI? y/n: ")
                enter = enter.lower()

                enterCLI("Python template ") if enter else exit(0)


            except Exception as e:
                print("Failed to create template for python. Error occured: \n")
                print(e)


        elif (yn == "n"):
            print("template not created")
            input()

        else:
            print("error: you didn't enter y or n. Aborted")
            exit(0)
            




def createHTMLTemplate(withJS, chjs_struct):
    print("Creating HTML template for directory " + os.getcwd() + ".")
    print("Generated JS file (main.js): " + str(withJS))
    print("HTML-CSS-JS folder structure: " + str(chjs_struct))


    yn = input("Do these configurations look good to you? y/n: ").lower()

    if (yn == "y"):
        try:
            if (chjs_struct):
                os.mkdir("HTML")
                os.mkdir("CSS")
                os.mkdir("JS")

                os.system("touch HTML/index.html & touch CSS/index.css")

            else:
                os.system("index.html")
                os.system("index.css")

            if (withJS):

                if (os.path.exists(os.getcwd() + "/JS")):
                    os.system("touch JS/main.js")
                
                else:
                    os.system("touch main.js")

        


        except Exception as e:
            print("Failed to create template for HTML. Error occured: \n")
            print(e)


    elif (yn == "n"):
        print("template not created")
        input()

    else:
        print("error: you didn't enter y or n. Aborted")
        exit(0)




if (args.template):

    args.template = args.template.lower()

    if (args.template == "html"):
        createHTMLTemplate(args.addjavascript, args.cssjshtml)
    
    elif (args.template == "c++" or args.template == "cpp"):
        createCPPTemplate(args.cppheaderdirectory, args.addsrc)

    elif (args.template == "py" or args.template == "python" or args.template == "python3"):
        createPythonTemplate(args.addsrc)




