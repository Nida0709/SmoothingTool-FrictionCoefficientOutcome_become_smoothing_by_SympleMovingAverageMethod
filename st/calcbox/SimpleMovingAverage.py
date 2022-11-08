def SMAcalc(t, y, delta):
    temp_y = []
    if delta % 2 == 1:
        range_other = int((delta-1)/2+1)
        for i in range(0,range_other):
            temp_value = 0
            for j in range(0,i*2+1):
                temp_value = temp_value + y[j]
            temp_y.append(temp_value/(i*2+1))
        for i in range(range_other,len(t)-range_other):
            temp_value = 0
            for j in range(int(i-(delta-1)/2),int(i+(delta+1)/2)):
                temp_value = temp_value + y[j]
            temp_y.append(temp_value/delta)
        for i in range(len(t)-range_other, len(t)):
            temp_value = 0
            for j in range(i-((len(t)-1)-i), len(t)):
                temp_value = temp_value + y[j]
            temp_y.append(temp_value/(((len(t)-1)-i)*2+1))
        return temp_y
    else:
        range_other = int((delta)/2+1)
        for i in range(0,range_other):
            temp_value = 0
            for j in range(0,i*2+1):
                temp_value = temp_value + y[j]
            temp_y.append(temp_value/(i*2+1))
        for i in range(range_other,len(t)-range_other):
            temp_value = 0
            for j in range(int(i-(delta-2)/2),int(i+delta/2)):
                temp_value = temp_value + y[j]
            temp_value = temp_value + 0.5*y[int(i-(delta-2)/2-1)] + 0.5*y[int(i+delta/2)]
            temp_y.append(temp_value/delta)
        for i in range(len(t)-range_other, len(t)):
            temp_value = 0
            for j in range(i-((len(t)-1)-i), len(t)):
                temp_value = temp_value + y[j]
            temp_y.append(temp_value/(((len(t)-1)-i)*2+1))
        return temp_y