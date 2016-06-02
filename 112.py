import codecs, sys, os, re
from os import listdir
from os.path import join as joinpath
from os.path import isfile

verbm=['Intransitive_verb','Tense', 'Verb_pattern','Verb_form', 'Choice_of_tense', 'Sequence_of_tenses', 'Tense_choice_in_conditionals',
'Voice', 'Choice_of_voice', 'Tense_form', 'Negative_form']
adresa=[]
tree=os.walk('C:/Users/Regina5/Desktop/kur/var/OV_2_year')
for d, dirs, files in tree: 
    for f in files:
        path=os.path.join(d,f)
        adresa.append(path)

b=0
e=0
dic={}
maskey=[]
masval=[]
dic2={}
dic3={}
dic4={}
for fil in adresa:    
    if fil.endswith('.ann'):
        maskey.append(fil)
    elif fil.endswith('.txt'):
        masval.append(fil)

for i in range(len(maskey)):
    if maskey[i].split('.')[0]==masval[i].split('.')[0]:
        dic[maskey[i]]=masval[i]
# а где гарантия что файлы совпадают? скорее всего это у тебя тут так. ну в смысле что соответствуют тексты ann текстам txt?
# но в реальности (на разных операционных системах тем более) может быть по-разному. 
# не факт, что они в массивы записались в том же порядке.
# я бы по названиям ещё проверила. то есть брала например file.split('.')[0] это будет название файла в твоем случае
# сразу бы проверяла что они совпадают и писала бы в том же цикле в словарь. ТОгда не нужно массивы держать и это экономит память. 
borders=[]

for key in dic.keys():
    content=codecs.open(key, 'r', 'utf-8')#... тогда закрывать файл не нужно будет в конце. ты вообще закрыватие пропустила кстати
    #countline=0
    dic2={}

    for line in content.readlines():
        
        
        
##        error = line.split('\t')[1].split()[0]
##        verb_error = error.split(' ')[0]
##        if line.startswith('T') and verb_error in verbm:
##
        if line.startswith('T') and line.split('\t')[1].split(' ')[0] in verbm:
             #####countline+=1
            borders=[]
            m=re.search('^T(\d+)', line)
            if m!=None:
                 #dic2[m.group(1)]=line.split('\t')[1].split()[0]
                 
                 '''dic- {словарь с [ann]-[txt]}
dic2-{номер ошибки-название ошибки}
dic3- '''
##print (dic2)
##print(len(dic2))

##                 print(line+ ' ' + m.group(0))
##                 numofer=m.group(1)
##                 error=line.split('\t')[1].split()[0]
                 error_name=line.split('\t')[1].split()[0]
                 wordwrong=line.split('\t')[2].strip()
                 #print(wordwrong + " T " + str(m.group(1)))
                 b=int(line.split('\t')[1].split()[1])
                 e=int(line.split('\t')[1].split()[2])
                 borders.append(error_name)
                 borders.append(b)
                 borders.append(e)
                 borders.append(wordwrong)
                 #for keys,values in dic3.items():
                 #keyfr=frozenset(dic2.items())
                 dic2[m.group(1)]=borders#ключ у dic3 - это dic2
                 #dic3.values()=borders
                 #print(dic3)
        #borders=[]
                 #значеиня dic3-
##
##             print(b-1)#äëÿ ïðîâåðêè ÷òî b
##        elif line.startswith('A'):  
##             countline-=1
##             #string1=0
##    #print(countline)
##
        elif line.startswith('#'):
            ####m=re.search('^#(\d+)',line)
            ####countline+=1
            ####if m!=None:
                ####print(str(countline) + ' ' + str(m.group(1)))
                ####if m.group(1)==countline:
            m=re.search('T(\d+)', line)#line.split(' ')[1].split('\t')[0])
            if m!=None:
                if m.group(1) in dic2.keys():
                    wordright=line.split('\t')[2].strip()#.split()[0]
                    #print('#' + wordright + ' ' + str(m.group(1)))
                    dic2[m.group(1)].append(wordright)
    dic3[key]=dic2
#print(dic3)

for key, value in dic.items():
        #print(value)
        #for one in dic.values():
        txtcontent=codecs.open(value, 'r', 'utf-8')
        line=txtcontent.read()
        print(dic3[key].keys())
        keysdic3=dic3[key].keys().sort(key=lambda a: a)

        #keysdic3=sorted(dic3[key]= lambda x: cmp())
        for el in keysdic3:
            print(el)
        if keysdic3 != None:
            d = 0
            print(dic3[key].keys())
            for el in keysdic3:
                arr = dic3[key][el]
                d += len(arr[4]) - len(arr[3])
                line = line[ : arr[1] + d] + arr[4] + line[arr[2] + d : len(line)]
            print(line)

        
            



        
####                if line.split('\t')[1]
####                    wordright=line.split('\t')[2]#.split()[0] #во во, нужно побить ещё и по пробелам
####                    print(wordright)
####                    if m.group(1) in dic2:#если countline проверяет, то и не нужно мб?
####                        for keys, values in dic4.items():
####                            dic4[dic3.values]=wordright
####                    #print(dic4)
####                else:
####                    print(dic3.values())
####                        #dic4.values()=wordright
####    countline=0
##                 print(line)#go on right word
##                 print(wordright)
##                 txt=codecs.open(dic[key], 'r', 'utf-8') # Всё. тут уже всё в кучу.
##                 #Нужен какой-то план. У тебя всё сразу. Мысли правильные, но структурировать бы их только
##                 for line in txt.readlines():#ïðîõîäèì ïî ñòðîêàì
##                     #for c in line[b-1:b]:#êàê áðàòü ýë-òû ñòðîêè?
##                     for elem in line:
##                         if elem[]==b:
##
##                         print(c)
##                         re.sub(c, wordright, c)
##                     #txt.write(str(line)[b:e]
##                 #string1=0


# Тебе ведь нужно когда проверяешь что ошибка твоя (глагольная) хранить сразу информацию и об ошибке и индексы,
# и неправильныt/правильные ответы. Например, у тебя есть:
#  T1	Transitive 122 136	influence with
#  #1	AnnotatorNotes T1	influence
# Я бы в цикле после твоих ifов вытаскивала индексы (122 136) заодно и текст ошибки (influence with)
# Находила бы соответсвующий #1 AnnotatorNotes для того же числа и записывала бы в словарь правильный ответ influence
# то есть словарь бы в виде каком-нибудь таком был {'T1':{'influence with':'influence', 'index':[122,136]}, ... }
# Ну необязательно прям так, но чтобы тебе удобно было потом проходя по тексту txt
# вытаскивать индексы и заменять строку с неправильным ответом на правильный
# если что есть удобные словари defaultdict. их легко делать вложенными и там почти не появляются keyerror 


#if __name__ == "__main__":
 #    main()

