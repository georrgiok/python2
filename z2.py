# -*- coding: utf-8 -*-
print('_______________________________________')
print('|  X  |  Y  |  Z  |  !(X /\ Y) \/ Z   |')
print('|_____|_____|_____|___________________|')
for x in range(2):
    for y in range(2):
        for z in range(2):
            print('|  '+str(x)+'  |  '+str(y)+'  |  '+str(z)+'  |         '+ str(int(not( (x and y) or z)))+ '         |')
print('|_____|_____|_____|___________________|')




