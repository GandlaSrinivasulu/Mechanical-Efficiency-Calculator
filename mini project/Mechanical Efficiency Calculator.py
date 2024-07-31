from math import pi

#To calculate BP
def BP_cal(N,T):
    BP = (2*pi*N*T)/60000
    return BP
#To calculate IP
def IP2stroke_cal(P,L,A,N,K):
    IP = (P*L*A*N*K)/60000
    return IP

def IP4stroke_cal(P,L,A,N,K):
    IP = (P*L*A*N*K)/(2*60000)
    return IP

#To calculate mechanical efficiency
def Mech_cal(BP,IP):
    mech = IP*100 / BP
    return mech

N = float(input("Enter rpm:"))
T = float(input("Enter Torque(NM):"))
K = float(input("Enter no of cylinders:"))
S = float(input("Enter stroke type(2 or 4):"))
P = float(input("Enter mean effective pressure(N/m**2):"))
L = float(input("Enter length of stroke(m):"))
A = float(input("Enter area(m**2):"))
BP = BP_cal(N,T)
if S == 2:
    IP = IP2stroke_cal(P,L,A,N,K)
elif S == 4:
    IP = IP2stroke_cal(P,L,A,N,K)
    
Mech = Mech_cal(BP,IP)
print("Brake power = %.2f kw"%(BP))
print("Indicated power = %.2f Kw"%(IP))
print("Frictional Power = %.2f Kw"%(abs(IP - BP)))
print("Mechanical efficiency = %.2f per"%(Mech))


