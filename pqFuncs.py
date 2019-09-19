#! python3
# pqVars.py
# functions to import for pubQuery.py 

## FUNCTIONS
def change_search_engine():
    validInp = False

    while validInp == False:
        site = input("Please choose your Search Engine: \n(1) Google \n(2) Google Scholar \n(3) DuckDuckGo \n(4) Yahoo \nWhich site would you like to search?     ")
    
        if site== "1" or site.upper() == "GOOGLE":
            search_engine = "Google"
            validInp = True
        elif site == "2":
            search_engine = "Google Scholar"
            validInp = True
        else:
            print("Invalid entry...please restart...")
    return search_engine



def update_var(filename, var_name, var):
    #var_name = str(var)
    i = 0
    new_lines = []
    with open(filename,"r") as fh:
        lines = fh.readlines()
        for line in lines:
            i += 1
            print("CURRENT LINE ({1}):  {0}".format(line, i))
            if var_name in line.strip():
                print("Overwriting line {} in temporary storage...".format(i))
                updated_line = "{} = '{}'".format(var_name,var)
                new_lines.append(updated_line)
                print("Line {1} is now: {0}".format(updated_line, i))
            else:
                new_lines.append(line)
    with open(filename, "w") as fd:
        fd.seek(0)
        fd.truncate()
        for l in new_lines:
            fd.write(l)
        
