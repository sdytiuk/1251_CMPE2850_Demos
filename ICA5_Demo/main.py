import mysql.connector
mydb = mysql.connector.connect()
try:
    mydb = mysql.connector.connect(
        host="thor.cnt.sast.ca",
        user="demo_user",
        password='demo_password',
        database="demo_project")
except mysql.connector.Error as err:
    print(f'Something went wrong {err}')

if mydb is not None and mydb.is_connected():
    try:
        cursor = mydb.cursor(buffered=True, dictionary=True)
        query = f"Select * from authors where state like %s" + '%'
        filter = 'C%'
        params = (filter,)

        cursor.execute(query, params)
        column_names = cursor.column_names
        resultset = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f'Something went wrong {err}')
        resultset = None
    finally:
        cursor.close()

    print(column_names)
    print(resultset)

    #makedict don't need if dictionary=True
    resultlist = []
    for record in resultset:
        row = dict(zip(column_names, record))
        resultlist.append(row)
    print(resultlist)