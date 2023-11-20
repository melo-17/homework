import re
text = input()
print('Номера частных автомобилей:', re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', text))
print('Номера такси:', re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', text))