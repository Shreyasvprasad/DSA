"""pythonstarter"""
import sys,time
def main():
    sys.stdin=open('in.txt','r')
    sys.stdout=open('out.txt','w')
    start_time = time.time()
    print("-----%s seconds-----"%(time.time()-start_time))
