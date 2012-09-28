def myRenameMachine(location, header='IMG', middle='00',startNo=1):
    os.chdir(location)
    for files in os.listdir(location):
        newName = "%s_%s_%04d.CR2" % (header, middle, startNo)
        os.rename(files, newName)
        startNo+=1
        print newName
    print 'END'
    
if __name__ = '__main__':
	print 'My Rename Machine'
	# myRenamerMachine('E:\\Photo\\ImageFolder01\\'