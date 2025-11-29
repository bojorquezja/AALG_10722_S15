import random
def montecarlo(cant, lado):
    cir = 0
    for z in range(cant):
        x = random.uniform(-lado/2, lado/2)
        y = random.uniform(-lado/2, lado/2)
        if x*x + y*y <= lado/2*lado/2:
            cir += 1
    return cir

cua = 1000000
cir = montecarlo(cua, 2)
print(f"montecarlo % circulo:{cir/cua*100}%")