cost_letter = {
  'а':1, 'б':2, 'в':3,'г':4,'д':5,'е':6,'ё':7,'ж':8,'з':9,'и':10,'й':11,'к':12,
  'л':13,'м':14,'н':15,'о':16,'п':17, 'р':18,'с':19,'т': 20,'у': 21,'ф':22,
  'х':23,'ц':24,'ч':25,'ш':26,'щ':27,'ъ':28,'ы':29,'ь':30,'э':31,'ю':32,'я':33
  }
  
def prewiev():  
  print('''Это программа расчитывает "стоимость" слов.
И помогает отыскивать "долларывые" слова.
Каждая буква в слове имеет свою ценность.
Буква "а" стоит 1 цент, буква "б" - два
и так далее до буквы "я", которая стоит 33 цента
''')

def valid(letter):
  return letter.isalpha() and letter not in ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's','d', 'f', 'g', 'h', 'j', 'k', 'l','z','x','c','v','b','n','m']

def is_valid_cont():
  while True:
    n = input('Введите "да" или "нет": ')
    if n.lower() not in ['да', 'д', 'нет', 'н']:
      print('Я вас не понял, вы, наверное, ввели что-то другое.')
      continue
    elif n.lower() == 'д' or n.lower() == 'да':
      game()
    else:
      print('Спасибо, до встречи!')
      break
  
  
def game():
  words_list = (input('Напишите слово или несколько слов через запятую:')).split(',')
  print()
  for word in words_list:
    word_dif = word.strip().lower()
    count = 0
    for letter in word_dif:
      if valid(letter) == False:
        print('Слово', word_dif, 'написано не русским алфавитом.')
        break
      else:
        count += cost_letter[letter]

    if count == 100:
      print('Поздравляю! Вы нашли "долларовое" слово. Цена слова', word.strip(), 'составляет ровно 100 центов.')
    elif count == 0:
      continue
    elif count%10 == 1:
      print('Стоимость слова', word.strip(), 'составляет', count, 'цент')
    elif count%10 in [2, 3, 4]:
      print('Стоимость слова', word.strip(), 'составляет', count, 'цента')
    else:
      print('Стоимость слова', word.strip(), 'составляет', count, 'центов')
  print('Хотите проверить ещё слова?')

prewiev()

game() 

is_valid_cont()
