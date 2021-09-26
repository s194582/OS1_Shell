import os


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
        print("Parent process (pid:", os.getpid,")")
    
def cd(x):
    os.chdir(x)

if __name__ == "__main__":
    
    while 1:
        print("TEST2")
        x = input("$ ").split() #takes the user input and splits the string between each space
        #space 0 is the system command and space 1 is the target
        
        #terminates the terminal.
        if x[0] == "exit": 
            break
        #cd system call for changing the directory x[1] is the target directory.    
        if x[0] == "cd":
            cd(x[1])
        else:
        #we use command for all the systems calls that needs a child process i.e ls, cat, pwd.
            Command(x)
    