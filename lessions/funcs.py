import random
from students.models import students

pars = students.objects.all()
    

# def groupp (x, y):
#     res=[]
#     #N = len(seq)
#     for i in range( y):
#         while len(res) < y:
#             res = random.sample(x,k=y)
#             while x[i].first_language == x[i-1].first_language:
#                 res = random.sample(x,k=y)

#     return res

def groupp (x, y):
    res = random.sample(x, y)
    while len(set([u.first_language for u in res])) < y:
        res = random.sample(x, y)
    return res


