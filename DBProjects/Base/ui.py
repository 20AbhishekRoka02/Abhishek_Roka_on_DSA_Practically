import sqlparse



dbmsname = "rokadb>"
if __name__=="__main__":
    print("This is ui of the DBMS project.")
    print("Enter something here....")
    while True:
        sql = input(f"{dbmsname} ")
        
        first_statement = sqlparse.parse(sql)[0]
        
        match first_statement.get_type():
            case 'INSERT':
                print("Hello insert")

            case 'DROP':
                print("Drop statement")
            
            case _:
                print(f"{first_statement.get_type()} is not supported, right now! ;-)")
        
        
        # for i in sqlparse.parse(sql):
        #     print(i)
        #     print(i.get_type())
    