import sqlite3
base = sqlite3.connect("test.db")
c = base.cursor()
from time import sleep

# c.execute("""CREATE TABLE fp1_3( 
#     driver text,
#     team text,
#     best_lap_time float,
#     tyre_compound text,
#     track_temp float,
#     windspeed float

# )
# """)

# c.execute("""CREATE TABLE fp2_2( 
#     driver text,
#     team text,
#     best_lap_time float,
#     tyre_compound text,
#     track_temp float,
#     windspeed float

# )
# """)

# c.execute("""CREATE TABLE fp3_4( 
#     driver text,
#     team text,
#     best_lap_time float,
#     tyre_compound text,
#     track_temp float,
#     windspeed float

# )
# """)

# c.execute("""CREATE TABLE previous_starting_positions_4(
#     driver text,  
#     grand_prix text,
#     grid_position int

# )
# """) #past qualifying posotions for tyre compound choice


# c.execute("INSERT INTO fp1_3 VALUES('Max Verstappen' , 'Red Bull'	, 91.394 ,'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Lewis Hamilton' , 'Mercedes'	, 91.921 ,'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Pierre Gasly' , 'AlphaTauri' , 92.195 , 'soft' , 47.7, 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Valtteri Bottas' , 'Mercedes' , 91.692 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Sergio Pérez' , 'Red Bull' , 92.307 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Carlos Sainz' , 'Ferrari' , 92.366 , 'soft' , 47.7, 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Kimi Räikkönen' , 'Alfa Romeo' , 	93.134 , 'soft' , 47.7, 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Esteban Ocon' , 	'Alpine' , 93.528 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Lance Stroll' , 	'Aston Martin' , 93.233 , 'soft', 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Daniel Ricciardo' , 'McLaren',	92.434,	'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Charles Leclerc',	'Ferrari' , 91.993 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Antonio Giovinazzi' , 'Alfa Romeo' , 92.786 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Yuki Tsunoda' , 'AlphaTauri' , 93.329 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Sebastian Vettel' , 'Aston Martin' , 93.157 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Fernando Alonso' , 'Alpine' , 93.872 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Lando Norris' , 'McLaren' , 92.860 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('George Russell' , 'Williams' , 94.127 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Mick Schumacher' , 'Haas' , 94.501 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Nikita Mazepin' , 'Haas' , 94.975 , 'soft' , 47.7 , 0.2)")
# c.execute("INSERT INTO fp1_3 VALUES('Nicholas Latifi',  'Williams' , 94.340, 'soft' , 47.7 , 0.2)")

# c.execute("INSERT INTO fp2_2 VALUES('Max Verstappen' , 'Red Bull'	, 90.847 ,'soft' , 28.1 ,1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Lewis Hamilton' , 'Mercedes'	, 91.082 ,'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Pierre Gasly' , 'AlphaTauri' , 91.483 , 'soft' , 28.1, 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Valtteri Bottas' , 'Mercedes' , 91.218 , 'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Sergio Pérez' , 'Red Bull' , 91.503 , 'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Carlos Sainz' , 'Ferrari' , 91.127 , 'soft' , 28.1, 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Kimi Räikkönen' , 'Alfa Romeo' , 	91.862 , 'soft' ,28.1, 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Esteban Ocon' , 	'Alpine' , 91.601, 'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Lance Stroll' , 	'Aston Martin' , 91.393 , 'soft', 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Daniel Ricciardo' , 'McLaren',	91.230,	'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Charles Leclerc',	'Ferrari' , 91.612 , 'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Antonio Giovinazzi' , 'Alfa Romeo' , 91.370 , 'soft' , 28.1, 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Yuki Tsunoda' , 'AlphaTauri' , 91.294 , 'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Sebastian Vettel' , 'Aston Martin' , 91.769 , 'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Fernando Alonso' , 'Alpine' , 91.770 , 'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Lando Norris' , 'McLaren' , 90.942 , 'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('George Russell' , 'Williams' , 92.331 , 'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Mick Schumacher' , 'Haas' , 93.297 , 'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Nikita Mazepin' , 'Haas' , 93.400 , 'soft' , 28.1 , 1.1)")
# c.execute("INSERT INTO fp2_2 VALUES('Nicholas Latifi',  'Williams' , 93.449, 'soft' , 28.1 , 1.1)")


# c.execute("INSERT INTO fp3_4 VALUES('Max Verstappen' , 'Red Bull'	, 90.577 ,'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Lewis Hamilton' , 'Mercedes'	, 91.316 ,'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Pierre Gasly' , 'AlphaTauri' , 91.583 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Valtteri Bottas' , 'Mercedes' , 91.855 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Sergio Pérez' , 'Red Bull' , 91.908 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Carlos Sainz' , 'Ferrari' , 92.108 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Kimi Räikkönen' , 'Alfa Romeo' , 	92.224 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Esteban Ocon' , 	'Alpine' , 92.423 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Lance Stroll' , 	'Aston Martin' , 92.431 , 'soft', 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Daniel Ricciardo' , 'McLaren',	92.447,	'medium' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Charles Leclerc',	'Ferrari' , 92.482 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Antonio Giovinazzi' , 'Alfa Romeo' , 92.5 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Yuki Tsunoda' , 'AlphaTauri' , 92.709 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Sebastian Vettel' , 'Aston Martin' , 92.755 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Fernando Alonso' , 'Alpine' , 92.820 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Lando Norris' , 'McLaren' , 92.860 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('George Russell' , 'Williams' , 93.323 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Mick Schumacher' , 'Haas' , 93.422 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Nikita Mazepin' , 'Haas' , 93.662 , 'soft' , 48.2 , 1.4)")
# c.execute("INSERT INTO fp3_4 VALUES('Nicholas Latifi',  'Williams' , 93.959 , 'soft' , 48.2 , 1.4)")



# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Max Verstappen','bahrain gp',1 )") 
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Max Verstappen','imola gp',3 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Lewis Hamilton','bahrain gp',2 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Lewis Hamilton','imola gp',1 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Pierre Gasly','bahrain gp',5 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Pierre Gasly','imola gp',5 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Valtteri Bottas','bahrain gp',3 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Valtteri Bottas','imola gp',8 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Sergio Pérez','bahrain gp',11 )") 
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Sergio Pérez','imola gp',2 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Carlos Sainz','bahrain gp',8 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Carlos Sainz','imola gp',11 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Kimi Räikkönen','bahrain gp',14 )") 
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Kimi Räikkönen','imola gp',16 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Esteban Ocon','bahrain gp',16 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Esteban Ocon','imola gp',9 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Lance Stroll','bahrain gp',10 )") 
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Lance Stroll','imola gp',10 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Daniel Ricciardo','bahrain gp',6 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Daniel Ricciardo','imola gp',6 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Charles Leclerc','bahrain gp',4 )") 
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Charles Leclerc','imola gp',4 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Antonio Giovinazzi','bahrain gp',12 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Antonio Giovinazzi','imola gp',17 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Yuki Tsunoda','bahrain gp',13 )") 
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Yuki Tsunoda','imola gp',20 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Sebastian Vettel','bahrain gp',18 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Sebastian Vettel','imola gp',13 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Fernando Alonso','bahrain gp',9 )") 
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Fernando Alonso','imola gp',15 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Lando Norris','bahrain gp',7 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Lando Norris','imola gp',7 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('George Russell','bahrain gp',15 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('George Russell','imola gp',12 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Mick Schumacher','bahrain gp',19 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Mick Schumacher','imola gp',18 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Nikita Mazepin','bahrain gp',20 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Nikita Mazepin','imola gp',19)")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Nicholas Latifi','bahrain gp',17 )")
# c.execute("INSERT INTO previous_starting_positions_4 VALUES ('Nicholas Latifi','imola gp',14 )")





c.execute("SELECT * FROM fp1_3")
rows_fp1 = c.fetchall()
# print(rows_fp1) #prints table data in the form of tuples nested within lists
print()
print()

c.execute("SELECT * FROM fp2_2")
rows_fp2 = c.fetchall()
# print(rows_fp2)
print()
print()

c.execute("SELECT * FROM fp3_4")
rows_fp3 = c.fetchall()
# print(rows_fp3)
print()
print()

c.execute("SELECT * FROM previous_starting_positions_4")
rows_previous_grid = c.fetchall()
print(rows_previous_grid)

base.commit()
base.close()
print(base)

print()
print()

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
    print(temp/2)
print()
print(d_avg_pos)

d_q2_compounds = {}
for x in d_avg_pos:
    if d_avg_pos[x] > 6 and d_avg_pos[x] <= 15:
        d_q2_compounds[x] = "soft"
    elif d_avg_pos[x] > 15:
        d_q2_compounds[x] = "dnq"
    elif d_avg_pos[x] <= 3:
        d_q2_compounds[x] = "medium/hard"
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

original_lap_times_list = lap_times_list
original_drivers_list = drivers_list

original_lap_times_list_1 = lap_times_list
original_drivers_list_1 = drivers_list

def bubble_sort(l,l2):
    for y in range(len(l)):
        for x in range(len(l)):
            if x != len(l) - 1:
                if l[x+1] < l[x]:
                    l[x+1],l[x] = l[x],l[x+1]  
                    l2[x+1],l2[x] = l2[x],l2[x+1]   
    return (l,l2)

print(bubble_sort(lap_times_list , drivers_list))


def q1():
    for x in range(len(drivers_list)):
        if d_avg_pos[drivers_list[x]] >= 12:
            pass
        #predicted to run on softs
        elif d_avg_pos[drivers_list[x]] in range(6,12):
            global lap_times_list
            lap_times_list[x] += 0.9 #predicted medium tyres
        else:
            lap_times_list[x] += 1

    temp = bubble_sort(lap_times_list,drivers_list)
    lap_times_list = temp[0]
    print("Q1 is starting 5 drivers will be eliminated......")
    sleep(1)

    for x in range(len(lap_times_list)-1,len(lap_times_list)-6,-1):
        print( x+1 , drivers_list[x] )
    print(" have been eliminated ")

def q2():
    for x in range(len(drivers_list)-5):
        if d_avg_pos[drivers_list[x]] >= 7:
            pass #predicted to run on softs
        elif d_avg_pos[drivers_list[x]] in range(4,7):
            global lap_times_list
            lap_times_list[x] += 0.9 #predicted medium tyres
        else:
            lap_times_list[x] += 1.3 #predicted hard tyres or medium tyre

    temp = bubble_sort(lap_times_list[0:15],drivers_list[0:15])
    lap_times_list = temp[0]
    print("Q2 is starting 5 drivers will be eliminated......")
    sleep(1)

    for x in range(len(original_lap_times_list)-6,len(original_lap_times_list)-11,-1):
        print( x+1 , drivers_list[x] )
    print(" have been eliminated ")

def q3():
    global lap_times_list
    temp = bubble_sort(lap_times_list[0:10],drivers_list[0:10])
    lap_times_list = temp[0]
    print("Q3 is starting.........")
    sleep(1)

    for x in range(len(lap_times_list)-11,len(lap_times_list)-16,-1):
        print( x+1 , drivers_list[x] )

q1()
q2()
q3()
    

    


