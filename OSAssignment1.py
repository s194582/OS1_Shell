
import os

STDIN = 0
STDOUT = 1 #dette er for så den ikke smider den ud til skærmen ved exec() funktionen

def Command(x):
    #create a child process
    rc = os.fork()
    #if rc is equal to 0 the child process is running.
    if rc == 0:
        #execute a new progam, replacing the current process. when done running the process, terminate the process
        os.execvp(x[0], x) 
        
    if rc > 0:
        os.wait() #Stop the parent process, until the child process is done. 
        
#define the cd command
def cd(x)
    #check if there are more than one argument in user input
    if len(y) > 1:
        #Take second argument from user input and move to new directory
        os.chdir(x[1])
    else:
        #go to home directory
        os.chdir(os.environ["HOME"])


def pipe(x):
    #The string x is split, and defined as two new string()
    z = x[1].split()
    #File descriptors r,w for Reading and Writing
    r, w = os.pipe()
    #create a child process
    rc1 = os.fork()

    #Check if fork() has been run
    if rc1 < 0:
        print("OSError")

    if rc1 == 0:
        #child
        #create a new child process inside the earlier child process.
        #By doing this, the old child process will be both a child process, but also a parent process.
        rc3 = os.fork()
        if rc3 == 0:
            #child
            os.close(r)
            os.dup2(w, STDOUT)
            #close the child process
            exit()
            
            
        else:
            #parent
            os.close(w)
            os.dup2(r, STDIN) #kopirer processen og sætter den ene ende af pipen istedet for STDOUT
                
            os.wait() #Stop the parent process, until the child process is done.
            #execute a new progam, replacing the current process. when done running the process, terminate the process
            os.execvp(z[0], z)
    else:
        #parent
        os.wait() #Stop the parent process, until the child process is done. 



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
            #while also splitting the user input in two, where "|" is in the user input
            pipe(x.split("|"))


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






    
