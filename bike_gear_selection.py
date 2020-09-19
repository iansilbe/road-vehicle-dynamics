#Gear Selection for Max Acceleration on a Bicycle
import numpy
import matplotlib.pyplot as plt
import math

#Bicycle Parameters
M = 70 #[kg]
It = 0.2 #[kg*m^2]
Rt = 0.4 #[m]

grats = [32/53, 20/53, 11/53] #Defined as R2/R1 (same as cars)

thetapdot = numpy.linspace(0,250,501) #[rpm]
thetapdot2 = thetapdot*2*math.pi/60 #[rad/s]

#thetapdot = numpy.ndarray.tolist(thetapdot)
#thetapdot2 = numpy.ndarray.tolist(thetapdot2)
#numpy.multiply(5.73,thetapdot2)

xdot_g1 = (Rt/grats[0])*thetapdot2 #bike speed [m/s]
xdot_g2 = (Rt/grats[1])*thetapdot2 #bike speed [m/s]
xdot_g3 = (Rt/grats[2])*thetapdot2 #bike speed [m/s]

xddot_g1 = ((grats[0]/Rt)*(150-5.73*thetapdot2)) / (M + (2*It)/(Rt**2))
xddot_g2 = ((grats[1]/Rt)*(150-5.73*thetapdot2)) / (M + (2*It)/(Rt**2))
xddot_g3 = ((grats[2]/Rt)*(150-5.73*thetapdot2)) / (M + (2*It)/(Rt**2))


plt.plot(thetapdot, xddot_g1,'r:',
         thetapdot, xddot_g2,'b:',
         thetapdot, xddot_g3,'g:')
plt.xlabel('Pedaling Rate [rpm]')
plt.ylabel('Bike Acceleration [m/s^2]')
plt.legend(['Gear Ratio: 32/53','Gear Ratio: 20/53','Gear Ratio: 11/53'])
plt.title('Acceleration as a Function of Pedaling Rate')
plt.grid(True)

plt.figure()
plt.plot(xdot_g1*2.23694, xddot_g1,'r:',
         xdot_g2*2.23694, xddot_g2,'b:',
         xdot_g3*2.23694, xddot_g3,'g:')
plt.xlabel('Bike Speed [mph]')
plt.ylabel('Bike Acceleration [m/s^2]')
plt.legend(['Gear Ratio: 32/53','Gear Ratio: 20/53','Gear Ratio: 11/53'])
plt.title('Acceleration as a Function of Bike Speed')
plt.grid(True)

#Simulating the Race using Euler Forward Method
N = 501
dt = 0.5 #Sampling interval [s]
#t = list(range(0,(N-1)*dt,dt))
t = numpy.ndarray.tolist(numpy.arange(0,N*dt,dt))

x = [0] #Initial condition
xdot = [0] #Initial condition
xddot = []

for k in list(range(len(t)-1)): #Because k must be an integer; ie the index of t rather than the value of t
#len(t) - 1 because if not xdot.- and x.append will predict an extra value
    if xdot[k] < 24/2.23694:
        #Pedaling Rate and Acceleration at the Current Time 
        print('gear 1')
        thetapdot2[k] = (1/Rt)*grats[0]*xdot[k]
        xddot.append(((grats[0]/Rt)*(150-5.73*thetapdot2[k])) / (M + ((2*It)/(Rt**2))))
    elif xdot[k] < 40/2.23694:
        print('gear 2')
        thetapdot2[k] = (1/Rt)*grats[1]*xdot[k]
        xddot.append(((grats[1]/Rt)*(150-5.73*thetapdot2[k])) / (M + ((2*It)/(Rt**2))))
    else:
        print('gear 3')
        thetapdot2[k] = (1/Rt)*grats[2]*xdot[k]
        xddot.append(((grats[2]/Rt)*(150-5.73*thetapdot2[k])) / (M + ((2*It)/(Rt**2))))
    
    #Velocity and Position at the Next Time Step
    xdot.append(xdot[k] + xddot[k]*dt)
    x.append(x[k] + xdot[k]*dt)

[item*2.23694 for item in xdot] #Convert to mph

plt.figure()
plt.plot(t,xdot)
plt.ylabel('Velocity [mph]')
plt.xlabel('Time [s]')
plt.grid(True)