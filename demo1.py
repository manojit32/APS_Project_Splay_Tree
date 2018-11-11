import pandas as pd
import time
import splay1
import bst1
df4=pd.read_csv("unique_tracks.txt",sep="<SEP>",header=None,engine='python')
df6=df4[[2,3]]
df6=df6.dropna()
s1=splay1.Splay()
for i in range(0,int(df6.size/8)):
    s1.insert(df6.iat[i,0],df6.iat[i,1])
print("1")
def face():
    while(1):
        i=int(input("Enter 1 to enter new record, 2 to search by artist name, 3 to delete, 4 to exit: \n"))
        if i==2:
            an=input("Enter artist name: ")
            s1.search(an)
        elif i==1:
            an=input("Enter artist name: ")
            song=input("Enter song name: ")
            # dt=an+" "+song
            s1.insert(an,song)
            print("Successfully inserted.")
        elif i==3:
            an=input("Enter artist name: ")
            song=input("Enter song name: ")
            # dt=an+" "+song
            s1.remove(an,song)
            print("Successfully deleted.")
        else:
            print("Exiting application.")
            break

    return 0
if __name__=="__main__":
    face()
