import os

def writeDirectory(path, txtPath):
    joinedPath = os.path.join(txtPath, '_path.txt')
    with open(joinedPath, 'w') as file:
        file.write(path)
        
def readDirectory(txtPath):
    joinedPath = os.path.join(txtPath, '_path.txt')
    with open(joinedPath, 'r') as file:
        return file.readline()
        
    