import sys

if __name__ == "__main__": 
    
    
    fileName = sys.argv[1]
    
    with open(fileName, 'r+') as fileContent:
        readedContent = fileContent.readlines()
        for lines in readedContent:
            print(lines)