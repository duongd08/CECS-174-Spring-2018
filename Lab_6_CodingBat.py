#This was done by Daniel Duong and Matthew Machado.

#1

print('***************************************')
print('Sleep_In')
def sleep_in(weekday, vacation):
  if  not weekday or vacation:
    return True
    
  else:
    return False

#2
print('***************************************')
print('Sum_Double')
def sum_double(a, b):
  if 'a' == 'b':
    return int(a + b) * 2
    
return int(a + b)


#3
print('***************************************')
print('love6')
def love6(a, b):
  if a and b == 6:
    return True
    
  elif a + b == 6:
    return True
  
  elif a == 6 or b == 6:
    return True
  
  elif a - b == 6 or b -a == 6:
    return True
  else:
    return False

#4
print('***************************************')
print('alarm_clock')
def alarm_clock(day, vacation):
  if vacation == True and (day == 0 or day == 6):
    return 'off'

  elif vacation == True and (day == 1 or day == 2 or day == 3 or day == 4 or day == 5):
    return '10:00'
    
  elif vacation == False and  day == 0 or day == 6:
    return '10:00'
    
  elif vacation == False and day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
    return '7:00'

#5
print('***************************************')
print('no_teen_sum')
def no_teen_sum(a, b, c):
  if 13 <= a <= 19 and a != 15 and a != 16:
    a = 0
  if 13 <= b <= 19 and b != 15 and b != 16:
    b = 0
  if 13 <= c <= 19 and c != 15 and c != 16:
    c = 0
    
  return int(a + b + c)
