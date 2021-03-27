# import os for python to access your device and operating system
import os

def main():
    # get a variable
    i = 0
    file_path = # ex 'C:/Users/chryz/Desktop/try/mysite/polls/templates/polls/'
    for file_name in os.listdir(file_path)
    my_files = file_name + str(i) # you can add any extension to this depending on your files
    # if it is a folder full of python codes ---------- my_files = file_name + str(i) + '.py'--------------

    #sorting out the renaming of the files
    my_source = file_path + file_name
    my_files = file_path + my_files
    os.rename(my_source, my_files)
    # define the variable more better to suit our purpose
    i =+ 1

# calling the defined function
    if __name__ = '__main__' :
        main()
