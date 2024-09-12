from serial import Serial
import numpy as np
import TDOA
import SPL as spl
import time


ser = Serial("COM6",9600,timeout = 5)
data = []
while True:
    for i in range(301):

      c = ser.readline() 
      string_n = c.decode()
      string = string_n.rstrip()
      data.append(int(string))

        
    zaman = round(data[0]/len(data))
    mic1 = np.array(data[1::3])
    mic2 = np.array(data[2::3])
    mic3 = np.array(data[3::3])
    print(zaman)
    print(mic1)
    print(mic2)
    print(mic3)

    


    
    # dif13 = TDOA.timedef(mic1,mic3)
    # dif12 = TDOA.timedef(mic1,mic2)
    # dif32 = TDOA.timedef(mic3,mic2)
    dif13 = TDOA.phase_dif(mic1,mic3)
    dif12 = TDOA.phase_dif(mic1,mic2)
    dif32 = TDOA.phase_dif(mic3,mic2)

    sound_speed = 0.000343  # meter per micro second
    fasele = zaman * sound_speed  #fasele makani ke sot dar har dor dade bardari tey mikonad
    print(fasele)
    print(zaman)
    TDOA.localization(-0.25,0,0.25,0,0,0.433,dif13*fasele,dif32*fasele)


    spl1 = spl.calculate_spl(mic1)
    spl2 = spl.calculate_spl(mic2)
    spl3 = spl.calculate_spl(mic3)
    mean_spl = sum([int(spl1),int(spl2),int(spl3)])/3
    print(spl1)
    print(spl2)
    print(spl3)
    print(mean_spl)
    
    if mean_spl < 40:
      reply = "kkkk"
      ser.write(reply.encode())
    elif mean_spl < 80:
      reply = "mmmm"
      ser.write(reply.encode())
    elif mean_spl < 120:
      reply = "cccc"
      ser.write(reply.encode())
    

    reply = "zzzz"
    ser.write(reply.encode())
    ser.write(str(fasele).encode())
    # ser.write()#---------------dakhel parantez khoroji TDOA ra mizarim

    inp = input()
    if inp=="r":
        key = "qqqq"
        ser.write(key.encode())

  
    
        
