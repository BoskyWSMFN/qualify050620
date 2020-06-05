# -*- coding: utf-8 -*-
import sys, getopt
import numpy as np

class LibraryMem(object):
    def savefile(self):
        ar = np.vstack((self.id, self.author))
        ar = np.vstack((ar, self.name))
        ar = np.vstack((ar, self.publish))
        ar = np.vstack((ar, self.section))
        ar = np.vstack((ar, self.opinion))
        ar = np.vstack((ar, self.available))
        ar = np.vstack((ar, self.count))
        ar = np.transpose(ar)
        np.savetxt(self.inputfile, ar,
                   header='id,author,name,publish,section,opinion,available,count',
                   delimiter=",", encoding='utf-8', fmt='%s')
    
    def __init__(self, inputfile, argv,*args,**kwargs):
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        for opt, arg in opts:
            if opt == '-h':
                print
                'library.py -i <inputfile>'
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
        self.inputfile = inputfile
        self.id = np.genfromtxt(inputfile, skip_header=1, delimiter=',',
                                    dtype = int, usecols=(0), encoding='utf-8',
                                    defaultfmt='%03d')
        self.author = np.genfromtxt(inputfile, skip_header=1, delimiter=',',
                                    dtype = str, usecols=(1), encoding='utf-8')
        self.name = np.genfromtxt(inputfile, skip_header=1, delimiter=',',
                                  dtype = str, usecols=(2), encoding='utf-8')
        self.publish = np.genfromtxt(inputfile, skip_header=1, delimiter=',',
                                     dtype = str, usecols=(3), encoding='utf-8')
        self.section = np.genfromtxt(inputfile, skip_header=1, delimiter=',',
                                     dtype = str, usecols=(4), encoding='utf-8')
        self.opinion = np.genfromtxt(inputfile, skip_header=1, delimiter=',',
                                     dtype = str, usecols=(5), encoding='utf-8')
        self.available = np.genfromtxt(inputfile, skip_header=1, delimiter=',',
                                       dtype = int, usecols=(6), encoding='utf-8')
        self.count = np.genfromtxt(inputfile, skip_header=1, delimiter=',',
                                   dtype = int, usecols=(7), encoding='utf-8',
                                   defaultfmt='%03d')

def run(fname, argvr):
    lm = LibraryMem(inputfile=fname, argv=argvr)
    while True:
        print('Действие - выход, ввод, вывод, изменить')
        inputac = input('Действие: ')
        if inputac =='выход':
            lm.savefile()
            break
        elif inputac == 'ввод':
            lm.author = np.append(lm.author, input('Введите имя автора: '))
            lm.name = np.append(lm.name, input('Введите название книги: '))
            lm.publish = np.append(lm.publish, input('Введите название издательства: '))
            lm.section = np.append(lm.section, input('Введите название раздела: '))
            lm.opinion = np.append(lm.opinion, input('Введите мнение: '))
            while True:
                inputac = input('Введите количество: ')
                try:
                    if int(inputac) > 0:
                        lm.count = np.append(lm.count, int(inputac))
                        lm.available = np.append(lm.available, 1)
                        lm.id = np.append(lm.id, len(lm.id)+1)
                        break
                    elif int(inputac) < 0:
                        print('Количество не может быть меньше нуля!\n')
                    else:
                        lm.count = np.append(lm.count, int(inputac))
                        lm.available = np.append(lm.available, 0)
                        lm.id = np.append(lm.id, len(lm.id)+1)
                        break
                except ValueError:
                    print('Должно быть целое число!\n')
                    continue
            continue
        elif inputac == 'вывод':
            while True:
                print('Действие - назад, поиск')
                inputac = input('Действие: ')
                if inputac == 'назад':
                    break
                elif inputac == 'поиск':
                    while True:
                        print('Поиск по - автор, название, издательство')
                        inputac = input('Действие: ')
                        if inputac == 'автор':
                            s = np.where(lm.author == input('Автор: '))[0]
                            if len(s) != 0:
                                print('Номер записи Автор Название Издательство Раздел Мнение Количество')
                                for i in s:
                                    print(lm.id[i], ' ',
                                          lm.author[i], ' ',
                                          lm.name[i], ' ',
                                          lm.publish[i], ' ',
                                          lm.section[i], ' ',
                                          lm.opinion[i], ' ',
                                          lm.count[i])
                                print('\n')
                            else:
                                print("Нет данных по запросу!\n")
                            break
                        elif inputac == 'название':
                            s = np.where(lm.name == input('Название: '))[0]
                            if len(s) != 0:
                                print('Номер записи Автор Название Издательство Раздел Мнение Количество')
                                for i in s:
                                    print(lm.id[i], ' ',
                                          lm.author[i], ' ',
                                          lm.name[i], ' ',
                                          lm.publish[i], ' ',
                                          lm.section[i], ' ',
                                          lm.opinion[i], ' ',
                                          lm.count[i])
                                print('\n')
                            else:
                                print("Нет данных по запросу!\n")
                            break
                        elif inputac == 'издательство':
                            s = np.where(lm.publish == input('Издательство: '))[0]
                            if len(s) != 0:
                                print('Номер записи Автор Название Издательство Раздел Мнение Количество')
                                for i in s:
                                    print(lm.id[i], ' ',
                                          lm.author[i], ' ',
                                          lm.name[i], ' ',
                                          lm.publish[i], ' ',
                                          lm.section[i], ' ',
                                          lm.opinion[i], ' ',
                                          lm.count[i])
                                print('\n')
                            else:
                                print("Нет данных по запросу!\n")
                            break
                        else:
                            print('Недопустимые данные!\n')
                            break
                    
                    continue
                else:
                    print('Недопустимые данные!\n')
                    continue
            continue
        elif inputac == 'изменить':
            while True:
                print('Действие - назад, удалить запись, выдать книгу, принять книгу')
                inputac = input('Действие: ')
                if inputac == 'назад':
                    break
                elif inputac == 'удалить запись':
                    while True:
                        try:
                            inputac = input('Номер записи: ')
                            s = np.where(lm.id == int(inputac))[0]
                        except ValueError:
                            print('Должно быть целое число!')
                            continue
                        if len(s) != 0:
                            lm.id = np.array(range(1, len(lm.id)))
                            lm.author = np.delete(lm.author, s)
                            lm.name = np.delete(lm.name, s)
                            lm.publish = np.delete(lm.publish, s)
                            lm.section = np.delete(lm.section, s)
                            lm.opinion = np.delete(lm.opinion, s)
                            lm.available = np.delete(lm.available, s)
                            lm.count = np.delete(lm.count, s)
                            print('Запись удалена!\n')
                            break
                        else:
                            print('Не существует записи с таким номером!\n')
                            break
                    continue
                elif inputac == 'выдать книгу':
                    while True:
                        try:
                            inputac = input('Номер записи: ')
                            s = np.where(lm.id == int(inputac))[0]
                        except ValueError:
                            print('Должно быть целое число!')
                            continue
                        if len(s) != 0:
                            if lm.count[s.item()] == 1:
                                lm.count[s.item()] -= 1
                                lm.available[s.item()] = 0
                                print('Книга выдана! Больше нет в наличии!\n')
                                break
                            elif lm.count[s.item()] == 0:
                                print('Нет в наличии!\n')
                                break
                            else:
                                lm.count[s.item()] -= 1
                                print('Книга выдана!\n')
                                break
                        else:
                            print('Не существует записи с таким номером!\n')
                            break
                    continue
                elif inputac == 'принять книгу':
                    while True:
                        try:
                            inputac = input('Номер записи: ')
                            s = np.where(lm.id == int(inputac))[0]
                        except ValueError:
                            print('Должно быть целое число!')
                            continue
                        if len(s) != 0:
                            if lm.count[s.item()] == 0:
                                print('Книга принята! Теперь в наличии!\n')
                                lm.available[s.item()] = 1
                            else:
                               print('Книга принята!\n') 
                            lm.count[s.item()] += 1
                            break
                        else:
                            print('Не существует записи с таким номером!\n')
                            break
                    continue
                else:
                    print('Недопустимые данные!\n')
                    continue
            continue
        elif inputac == 'общий вывод':
            print('Номер записи Автор Название Издательство Раздел Мнение Количество')
            for i in range(len(lm.id)):
                print(lm.id[i], ' ',
                      lm.author[i], ' ',
                      lm.name[i], ' ',
                      lm.publish[i], ' ',
                      lm.section[i], ' ',
                      lm.opinion[i], ' ',
                      lm.count[i])
            print('\n')
            continue
        else:
            print('Недопустимые данные!\n')
            continue

def main(argv):
    inputfile = 'library.csv'
    run(inputfile, argv)

if __name__ == "__main__":
   main(sys.argv[1:])