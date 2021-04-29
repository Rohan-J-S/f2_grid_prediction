import sqlite3
base = sqlite3.connect("test.db")
c = base.cursor()

# c.execute("""CREATE TABLE fp1_1( 
#     driver text,
#     team text,
#     best_lap_time float,
#     tyre_compound text,
#     track_temp float,
#     windspeed float

# )
# """)

# c.execute("""CREATE TABLE fp2( 
#     driver text,
#     team text,
#     best_lap_time float,
#     tyre_compound text,
#     track_temp float,
#     windspeed float

# )
# """)

# c.execute("""CREATE TABLE fp3_1( 
#     driver text,
#     team text,
#     best_lap_time float,
#     tyre_compound text,
#     track_temp float,
#     windspeed float

# )
# """)

# c.execute("""CREATE TABLE previous_starting_positions_2(
#     driver text,  
#     grand_prix text,
#     grid_position int

# )
# """) #past qualifying posotions for tyre compound choice

# c.execute("INSERT INTO fp1_1 VALUES ('verstappen','red bull racing honda' , 89 , 'soft' , 35 , 5 )")

# c.execute("INSERT INTO fp2 VALUES ('verstappen','red bull racing honda' , 88.6 , 'soft' , 31 , 8 )")

# c.execute("INSERT INTO fp3_1 VALUES ('verstappen','red bull racing honda' , 88.2 , 'medium' , 31 , 8 )")


# c.execute("INSERT INTO previous_starting_positions_2 VALUES ('verstappen','bahrain gp',1 ),('verstappen' , 'imola gp' , 3),('perez','bahrain gp',11 ),('perez' , 'imola gp' , 2)") 

c.execute("SELECT * FROM fp1_1")
rows_fp1 = c.fetchall()
print(rows_fp1) #prints table data in the form of tuples nested within lists

c.execute("SELECT * FROM fp2")
rows_fp2 = c.fetchall()
print(rows_fp2)

c.execute("SELECT * FROM fp3_1")
rows_fp3 = c.fetchall()
print(rows_fp3)

c.execute("SELECT * FROM previous_starting_positions_2")
rows_previous_grid = c.fetchall()
print(rows_previous_grid)

base.commit()
base.close()
print(base)

#average starting grid pos calculation
d_avg_pos = {}
for x in range(len(rows_previous_grid)):
    if x == 0:
        temp = 0
        name = rows_previous_grid[0][0]
        temp += rows_previous_grid[x][2]
    elif x == len(rows_previous_grid)-1:
        temp += rows_previous_grid[x][2]
        d_avg_pos[name] = temp/2
    elif name != rows_previous_grid[x]:
        d_avg_pos[name] = temp/2
        name = rows_previous_grid[x][0]
        temp = rows_previous_grid[x][2]
    else:
        temp += rows_previous_grid[x][2]

print(d_avg_pos)

d_q2_compounds = {}
for x in d_avg_pos:
    if d_avg_pos[x] > 6 and d_avg_pos[x] <= 15:
        d_q2_compounds[x] = "soft"
    elif d_avg_pos[x] > 15:
        d_q2_compounds[x] = "dnq"
    else:
        d_q2_compounds[x] = "medium"
print(d_q2_compounds)

#lap time calculation on softs for most racers +0.9 for mediums and +1.6 for hard
drivers_list = []
lap_times_list = []  #for easy sorting while calling funcs q1 q2 and q3
for x in range(len(rows_fp1)):
    count = 0
    name = rows_fp1[x][0]

    if  rows_fp1[x][3] == "soft":
        fp1_time = rows_fp1[x][2]
    elif rows_fp1[x][3] == "medium":
        fp1_time = rows_fp1[x][2] - 0.9
    else:
        fp1_time = rows_fp1[x][2] - 1.6

    if  rows_fp2[x][3] == "soft":
        fp2_time = rows_fp2[x][2]
    elif rows_fp2[x][3] == "medium":
        fp2_time = rows_fp2[x][2] - 0.9
    else:
        fp2_time = rows_fp2[x][2] - 1.6

    if  rows_fp3[x][3] == "soft":
        fp3_time = rows_fp3[x][2]
    elif rows_fp3[x][3] == "medium":
        fp3_time = rows_fp3[x][2] - 0.9
    else:
        fp3_time = rows_fp3[x][2] - 1.6    

    lap_time = (fp1_time + 3*fp2_time + 2*fp3_time)/6
    drivers_list += [name]
    lap_times_list += [lap_time]
print(drivers_list,lap_times_list)


# fp1_1 = float(input("..")) #to be taken from database table
# fp1_2 = float(input(".."))
# fp1_3 = float(input(".."))
# fp2_1 = float(input(".."))
# fp2_2 = float(input(".."))
# fp2_3 = float(input(".."))
# fp3_1 = float(input(".."))
# fp3_2 = float(input(".."))
# fp3_3 = float(input(".."))
# temp = float(input("track temp: "))
# windspeed = float(input("enter wind speed: "))

# #calculation 
# avg_time_2 = (fp1_1 + fp2_1*3 + fp3_1*2)/6
# avg_time_2 = (fp1_2 + fp2_2*3 + fp3_2*2)/6
# avg_time_2 = (fp1_3 + fp2_3*3 + fp3_3*2)/6

