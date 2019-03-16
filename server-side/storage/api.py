import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="hack",
  passwd="hack",
  database="hackdb"
)

# print(mydb)
mycursor = mydb.cursor()
def get_way(f_id, l_id):
    mycursor.execute("select f_id, l_id, way from ways where (f_id = %i and l_id = %i) or (f_id =%i and l_id = %i)"%(f_id, l_id, l_id, f_id))
    myresult = mycursor.fetchall()
    return myresult[0][2].split('-')

def get_coords(id):
    mycursor.execute("select id, x, y from dotes where id = %i"%(id))
    myresult = mycursor.fetchall()
    return myresult[0][1:3]


print(get_way(1, 42))
print('1:', get_coords(1), '\n42:', get_coords(42))

# for i in range(len(lines)):
#     if lines[i] == '*': continue
#     x, y = lines[i].split()
#     mycursor.execute("insert into dotes values(%i, %f, %f)"%(i, float(x)/1000, float(y)/1000))
# mydb.commit()
#
# mycursor.execute("select * from dotes")
# myresult = mycursor.fetchall()
# # print(pathes)
# for row in myresult:
#     print(row)

# mycursor.execute('delete from ways')
# file = open('tt.txt', 'r')
# lines = [i.replace('\n', '') for i in file.readlines()]
# file.close()
# lines = [line.split(' :  ') for line in lines]
# print(False in [False for i in lines if len(i)!=2])
# ways, pathes = [], []
# print(lines)
# for line in lines:
#     ways.append(line[0].split())
#     try:
#         pathes.append(line[1].split())
#     except Exception as e:
#         print(e, line)
#
# for i in range(len(lines)):
#     mycursor.execute('insert into ways(f_id, l_id, way) values(%i, %i, "%s")'%(int(ways[i][0]),int(ways[i][1]), '-'.join(pathes[i])))
#     # print("insert into ways(f_id, l_id, way) values(%i, %i, %s)"%(int(ways[i][0]),int(ways[i][1]), f(pathes[i], '')))
#     # print(pathes[i])
# mydb.commit()
# mycursor.execute("select * from ways")
# myresult = mycursor.fetchall()
# print(pathes)
# for row in myresult:
#     print(row)
# mycursor.execute('insert into ways(f_id, l_id, way) values (1, 2, "1-2-3-2-3-24-2-2-24-24-2-235-1-2-23-3-25-1463-3")')
# print(pathes)
# mydb.commit()








# mycursor.execute("drop table dotes, ways")
# mycursor.execute("create table dotes(id tinyint primary key, x smallint, y smallint)")
# mycursor.execute("create table dotes(id tinyint primary key, x DOUBLE, y DOUBLE)")
# mycursor.execute("create table ways(f_id tinyint, l_id tinyint, way text)")
