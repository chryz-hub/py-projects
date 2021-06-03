# file input for users
fname = input('Enter file name: ')
# if the enter key is pressed 'emailfile.txt' is the file automatically
if (len(fname) < 1): fname = 'emailfile.txt'
#file handle
fh = open(fname)
# a loop that prints out the email
for line in fh:
    # parsing through
    if not line.startswith('From '): continue
    pieces = line.split()
    email = pieces[1]
    info1 = email.find('@')
    info2 = email.find(' ', info1)
    org = email[info1 + 1:info2]

    print (org)
