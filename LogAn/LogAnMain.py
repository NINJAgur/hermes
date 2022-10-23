def main(filepath):
    with open(filepath, 'r') as fi:
        lineslist = fi.readlines()
        lines = {i: lineslist[i] for i in range(len(lineslist))}
        errors = {i: lines[i] for i in lines.keys() if "ERROR" in lines[i]}
        warns = {i: lines[i] for i in lines.keys() if "WARNS" in lines[i]}
        infos = {i: lines[i] for i in lines.keys() if "INFOS" in lines[i]}
    

if __name__ == "__main__":
    main(input("File Path:\t"))
