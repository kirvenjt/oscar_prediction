import codecs 
from collections import defaultdict 

actors = defaultdict(set)
movies = defaultdict(set)
#actors movie file format
#title, year, fname, lname, billing_position
#(u'Day Zero', u'2007', u'Jon', u'Bernthal', u'3')
with codecs.open('./actor_experience/full', 'r', encoding='utf-8') as r_file:
    for l in r_file.readlines():
        l=eval(l)
        fname = l[2]
        lname = l[3]

        year = l[1]
        title = l[0]
        bil_pos = int(l[4])-1
        movies[(title, year)].add(((fname,lname), bil_pos))
        actors[(fname,lname)].add((year, title, bil_pos))

outfile = codecs.open('actor_experience.txt', 'w', encoding='utf-8')
actors_per_movie = 10
#For each movie count the number of movies each of the top 10 actors had been in
# prior to the year of that movie
for m in movies.keys():
    actors_experience = [0]*actors_per_movie
    for actor, bil_pos in movies[m]:

        for year, title, _ in actors[actor]:
            if title != m[0] and year<=m[1]:
                actors_experience[bil_pos] += 1

    outfile.write(str((m, actors_experience))+ '\n')
            
