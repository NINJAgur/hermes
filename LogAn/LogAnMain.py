def main(filepath):
    with open(filepath, 'r') as fi:
        lines = fi.readlines()
        for line in lines:
            print(line)
    

if __name__ == "__main__":
    main(input("File Path:\t"))
