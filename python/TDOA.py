
# دوتا داده را میگیرد و مقدار کرلیشن را در هر حالت حساب می کند
import random
import numpy as np
import sympy as sp
from matplotlib import pyplot as plt
from scipy.stats import pearsonr,spearmanr, kendalltau
import scipy.signal as ss
from scipy.linalg import norm


# def show_max(x,direction):
#     j=0
#     counter=0
#     for i in x:
#         if abs(i)>abs(j):
#             j=i
#             count=counter
#         counter=counter+1
#     if direction>0:
#         print(count,j)
#         return(count)
#     else:
#         print(-count,j)
#         return(-count)        
     

# def timedef(z,y):
#     pear_zforward=[]
#     pear_yforward=[]

#     for i in range(30):
#         pear_zforward.append(float(str(pearsonr(z[i:99], y[0:99-i]))[25:37]))
#     for i in range(30):
#         pear_yforward.append(float(str(pearsonr(z[0:99-i], y[i:99]))[25:37]))
        
#     jolo = show_max(pear_zforward,1)
#     aghab = show_max(pear_yforward,-1)

#     pear_yforward.reverse()
#     corel_list = pear_yforward + pear_zforward


#     t_corellist = range(-30,30)
#     tj = range(99-jolo)
#     ta = range(99+aghab)
#     mehvar_x = np.arange(0,101,step=20)
#     plt.subplot(4,1,1)
#     plt.plot(tj,z[jolo:99],'r')
#     plt.plot(tj,y[0:99-jolo],'g')
#     plt.ylabel(f'jolo {jolo}')
#     plt.xticks(mehvar_x)
#     plt.subplot(4,1,2)
#     plt.plot(ta,z[0:99+aghab],'r')
#     plt.plot(ta,y[-aghab:99],'g')
#     plt.ylabel(f'aghab {aghab}')
#     plt.xticks(mehvar_x)
#     plt.subplot(4,2,5)
#     plt.plot(range(len(z)),z,'k')
#     plt.plot(range(len(y)),y,'m')
#     plt.xticks(mehvar_x)
#     plt.ylabel('wave')
#     plt.subplot(4,2,7)
#     plt.plot(t_corellist,corel_list)
#     plt.ylabel('corelation')
#     plt.xlabel('back & forth')
#     plt.show()

#     if abs(jolo)>abs(aghab):
#         return jolo
#     else:
#         return aghab

def localization(x1,y1,x2,y2,x3,y3,d1,d2):
    
    X , Y  = sp.symbols('X Y')
    D = sp.symbols('D', positive=True)
    first = ((X-x1)**2+(Y-y1)**2)
    second = ((X-x2)**2+(Y-y2)**2)
    third = ((X-x3)**2+(Y-y3)**2)
    answer = sp.solve([sp.Eq(first,(D+d1)**2),sp.Eq(second,(D+d2)**2),sp.Eq(third,D**2)],[X,Y,D])
    plt.subplot(2,2,4)
    plt.plot([x1,x2,x3],[y1,y2,y3],'ro')
    plt.plot(answer[0][0],answer[0][1],'bo')
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.grid()
    plt.show()
    print(answer)


def phase_dif(a,b):
    cor = ss.correlate(a,b)

    total_norm = norm(a)*norm(b)
    cor = cor / total_norm
    phase_diffrence = np.argmax(cor)-len(a)
    print(phase_diffrence)

    plt.subplot(3,1,1)
    plt.plot(a , 'r' )
    plt.plot(b , 'g' )
    plt.subplot(3,1,2)
    plt.plot(cor)
    plt.subplot(3,1,3)
    if phase_diffrence < 0:
        plt.plot(a[abs(phase_diffrence):] ,'r')
        plt.plot(b[:phase_diffrence-1] , 'g')
    else:
        plt.plot(a[:phase_diffrence-1] , 'r')
        plt.plot(b[abs(phase_diffrence):] , 'g')
    plt.show()

    return phase_diffrence




#----------------------------------------test-----------------------

# 
# z = np.array([np.cos(0.02*np.pi*t) for t in range(200)])
# plt.plot(x)
# plt.plot(y)

# # print(spearmanr(x,y))
# timedef(x,y)
# plt.show()

# a = [35, 34, 36, 35, 1020, 35, 1020, 1023, 1022, 1021, 1021, 1021, 1022, 1021, 1021, 1023, 1022, 1020, 1021, 1021, 1021, 
#      1021, 1022, 1021, 1021, 1020, 1022, 1022, 1021, 
# 1021, 1021, 35, 35, 1021, 1022, 37, 1023, 1021, 1021, 1021, 1021, 1022, 1022, 1021, 1021, 1022, 1021, 1021, 1021, 1020, 
# 1021, 1021, 1021, 1021, 1021, 1020, 1021, 1021, 1020, 1021, 35, 35, 35, 35, 1020, 1023, 1021, 1022, 1021, 1022, 1021, 1021, 
# 1020, 1022, 1021, 1020, 1020, 1021, 1021, 1020, 1022, 1022, 1020, 1022, 1021, 1022, 1021, 1022, 1021, 1021, 35, 35, 35, 1021,
#  1020, 1021, 1022, 1022, 1021, 1022]
# c = np.array([random.randint(1,100) for _ in range(100)])

# b = np.array(list(c)[:-10]+[0 for _ in range(10)])
# c = [0 for _ in range(10)] + list(c)[10:]

# phase_dif(c,b)
