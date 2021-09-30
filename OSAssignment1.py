import os

STDIN = 0
STDOUT = 1 #dette er for så den ikke smider den ud til skærmen ved exec() funktionen

def Command(x):
    #create a child process
    rc = os.fork()

    if rc < 0:
        print(OSError)

    #if rc is equal to 0 the child process is running.
    if rc == 0:
        #execute a new progam, replacing the current process. when done running the process, terminate the process
        os.execvp(x[0], x) 
        
    if rc > 0:
        os.wait() #Stop the parent process, until the child process is done. 
        
#define the cd command
def cd(x):
    #check if there are more than one argument in user input
    if len(y) > 1:
        #Take second argument from user input and move to new directory
        os.chdir(x[1])
    else:
        #go to home directory
        os.chdir(os.environ["HOME"])


def pipe(x):
    #The string x is split at the "|" symbol, and defined as two new string()
    a = x.split("|")
    #File descriptors r,w for Reading and Writing
    if os.fork():
    #parent
        os.wait() #Stop the parent process, until the child process is done.
    else:
        #child, and also parent of child2
        w,r = os.pipe() #initialising the pipe
        if os.fork():
            # Child of parent, and parent of child2
            # Closes a file descriptor, so that it no longer refers to any file,
            # and may be reused
            os.close(r)
            os.dup2(w, STDIN) #Copies the file descriptor w, into STDIN 
            str = a[1]
            str = str.replace(' ', '') #this helps with user input errors.
            os.execlp(str,'-1') #this executes the right side of the pipe of the command 
        else:
            #child2: child of child1
            os.close(w)    #Closes a file descriptor, so that it no longer refers to any file, and may be reused
            os.dup2(r, STDOUT) #Copies the file descriptor r, into STDOUT
            os.execvp('ps', a[0].split()) #Splits the commands of the left side of the pipe and executes the command
            #instead of the execvp command goes into STDOUT it is redirected into the right side of the command.

 
if __name__ == "__main__":

    while 1:
        #Variable used for test
        i = 0
        x = input("$ ") #Take and define the user input
        #takes the user input and splits the string between each space
        #space 0 is the system command and space 1 is the target
        y = x.split()
        
        #check if user input is using pipe
        if "|" in x:
            #Give variable i the value 1
            i = 1
            #Run the defined function pipe(), 
            pipe(x)


        #Check if user input is equal to "exit"
        if y[0] == "exit": 
            #Stops the process.
            break
            
        #check if user input is equal to "cd"    
        if y[0] == "cd":
            #run the defined function cd()
            #the user input as argument
            cd(y)

        else:
            #check if the variable i is equal to 0
            if i == 0:
                #takes the user input and splits the string between each space
                #space 0 is the system command and space 1 is the target
                #y = x.split() 
                #run the defined function Command() with the string y as argument
                Command(y) 






    
