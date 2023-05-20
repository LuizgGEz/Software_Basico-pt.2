tempo=int(input('Insira o tempo de duração do evento:'))
hora=tempo//3600
minutos=(tempo-hora*3600)//60
seg=(tempo-hora*3600-minutos*60)
print('O tempo de duração do evento foi de {} horas, {} minutos e {} segundos'.format(hora,minutos,seg))