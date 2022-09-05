# perform static database operation
from schema import *

#Task -1(only once)
d.create_all()

# Task -2(only once)
# c1=Colleges(college_id=1,college_name='Oxford',address='UK',director_name='Oxana')
# d.session.add(c1)
# c2=Colleges(college_id=2,college_name='Stanford',address='US',director_name='Paresh')
# d.session.add(c2)
# c3=Colleges(college_id=3,college_name='Harvard',address='US',director_name='Omni')
# d.session.add(c3)
# c4=Colleges(college_id=4,college_name='Cambridge',address='UK',director_name='Ene')
# d.session.add(c4)

# d.session.commit()

# p1=Programs(program_id=1,program_name='M.S. Data science',fees=5000,college_id=1)
# d.session.add(p1)
# p2=Programs(program_id=2,program_name='M.S.  IOT',fees=7000,college_id=1)
# d.session.add(p2)
# p3=Programs(program_id=3,program_name='M.S.Machine learing',fees=10000,college_id=4)
# d.session.add(p3)
# p5=Programs(program_id=4,program_name='M.S.cybersecurity',fees=10000,college_id=1)
# d.session.add(p5)

# d.session.commit()

# Task -3 (multiple times)
for clg in Colleges.query.all():
    print("-",clg.college_name)
    for program in clg.programs:
        print("\t - ",program.program_name)