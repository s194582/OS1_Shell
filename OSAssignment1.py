import os


print("Test")

#def Command(x):
def Command(x):
    #print("Virker cd commanden?")
    
    rc = os.fork()
    if rc == 0:
        print("Child process (pid", os.getpid(),")")
        os.execvp(x[0], x)
        
    if rc > 0:
        os.wait()
        print("Parent process (pid:", os.getpid,")")
    
def cd(x):
    os.chdir(x)

if __name__ == "__main__":
    
    while 1:
        print("TEST2")
        #x = input("$ ").split()
        x = input("$ ").split()
        if x[0] == "exit":
            break
        if x[0] == "cd":
            #cd(x)
            cd(x[1])
        else:
            Command(x)
    #run()



