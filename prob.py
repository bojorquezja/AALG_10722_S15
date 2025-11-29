import random
def montecarlo2(cant, lado, rad):
    cir = 0
    for z in range(cant):
        x = random.uniform(-lado/2, lado/2)
        y = random.uniform(-lado/2, lado/2)
        cir += 1
        if x*x + y*y <= rad*rad:
            return cir
    return -1

def lasvegas2(cant, lado, rad):
    cir = 0
    while True:
        x = random.uniform(-lado/2, lado/2)
        y = random.uniform(-lado/2, lado/2)
        cir += 1
        if x*x + y*y <= rad*rad:
            return cir
    return -1

cua = 100
cir = montecarlo2(cua, 4000, 1)
cir2 = lasvegas2(cua, 4000, 1)
print(f"montecarlo ops para 1 punto :{cir}")
print(f"las vegas ops para 1 punto :{cir2}")