import os


print("Test")

def Command(x):
    rc = os.fork()
    if rc == 0:
        print("Child process (pid", os.getpid(),")")
        os.execvp(x[0], x)
        
    if rc > 0:
        os.wait()
        print("Parent process (pid:", os.getpid,")")
    
def wait():
    os.wait()

def getcwd():
    print(os.getcwd())

def ls():
    os.listdir()

def cd():
    os.chdir()

def exit():
    os._exit()

if __name__ == "__main__":
    
    while 1:
        x = input("$ ").split()
        if x[0] == "cd":
            cd()
        Command(x)
    #run()

'''


'''

