import os

STDIN = 0
STDOUT = 1 #dette er for så den ikke smider den ud til skærmen ved exec() funktionen
print("Test")


#def Command(x):
def Command(x):

    #initialisation of the fork system call. 
    rc = os.fork()
    #if rc is equal to 0 the creation of the child process succeeded. 
    if rc == 0:
        print("Child process (pid", os.getpid(),")")
        os.execvp(x[0], x) #this terminates the child process and returns to the parent process.

    if rc > 0:
        os.wait() #wait call so the child process finishes before returning to the parent process. 
        print("Parent process (pid:", os.getpid(),")")

def cd(x):
    os.chdir(x)

def pipe(x):
    #File descriptors r,w for Reading and Writing
    y = x[0].split()
    z = x[1].split()
    r, w = os.pipe()
    rc1 = os.fork()

    #Check if fork() has been run
    if rc1 < 0:
        print("OSError")

    if rc1 == 0:
        #child
        print("TEST!!!!!")

        print("Child process (pid", os.getpid(),")")
       
        rc3 = os.fork()
        if rc3 == 0:
            #child
            os.close(r)
            os.dup2(w, STDOUT)
            exit()
            
            
        else:
            #parent
            os.close(w)
            os.dup2(r, STDIN) #kopirer processen og sætter den ene ende af pipen istedet for STDOUT
                
            os.wait()
            os.execvp(z[0], z)
    else:
        #parents
        os.wait()



if __name__ == "__main__":

    while 1:
        i = 0
        x = input("$ ")

        if "|" in x:
            i = 1
            pipe(x.split("|"))


        #terminates the terminal.
        if x[0] == "exit": 
            break
        #cd system call for changing the directory x[1] is the target directory.    
        if x[0] == "cd":
            cd(x[1])

        else:    
            if i == 0:
                y = x.split() #takes the user input and splits the string between each space
                #space 0 is the system command and space 1 is the target
                Command(y) 





    
