# -*- coding: utf-8 -*-
path = '/Users/harry/Desktop/My apps/OGE Site/bio_quest5_brain_ecology.html'
with open(path, 'r', encoding='utf-8') as f:
    s = f.read()

for line in s.splitlines():
    if 'Грибы →' in line and 'opts:' in line:
        new_line = line.replace('Грибы', 'Мох')
        s = s.replace(line, new_line)
        print('opts fixed')
        break
else:
    print('opts NOT FOUND')

s = s.replace(
    'Гриб → Насекомое = насекомое ест гриб, энергия переходит от гриба к насекомому.',
    'Мох → Насекомое = насекомое ест мох, энергия переходит от мха к насекомому.'
)
s = s.replace(
    'Гриб → Насекомое = насекомое ест гриб. Цепь начинается с продуцента, а не с вершины!',
    'Мох → Насекомое = насекомое ест мох. Цепь начинается с продуцента (растение), а не с вершины!'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(s)
print('done')
