import json

data = {}

class Program():
    def add(self,name: str, score: int) -> None:
        global data
        if not name in data.keys():
            try:
                data[name] = score
                self.save()
                print('Student successfuly added!')
            except:
                print('Database Error!')
        else:
            print('There is already a student with the same name in the database.')
    
    def delete(self,name: str) -> None:
        global data
        if name in data.keys():
            try:
                del data[name]
                self.save()
                print('Student successfuly deleted!')
            except:
                print('Database Error!')
        else:
            print('There isn\'t a student with the name in the database.')

    def show(self,value = True) -> None:
        global data
        if value:
            table = sorted(data.items(),key=lambda p : p[1],reverse=True)
            
            for i,(name,score) in enumerate(table,start=1):
                print(f"{i}# {name} - {score}")
        else:
            table = filter(lambda x : 'm' in x or 'M' in x, data)
            print(list(table))
    
    def download(self):
        try:
            table = sorted(data.items(),key=lambda p : p[1],reverse=True)
            
            for i,(name,score) in enumerate(table,start=1):
                with open('save.txt','a',encoding='utf-8') as f:
                    f.write(f"{i}# {name} - {score} \n")
                
                print('Successfuly downloaded as save.txt!')
        except Exception as e:
            print('Something went wrong!',e)
    
    def save(self) -> None:
        global data
        try:
            with open('text.json','w',encoding='utf-8') as f:
                json.dump(data,f,ensure_ascii=False,indent=4)
        except:
            print('Database saving proccess failed!')
    
    def load(self) -> None:
        global data
        try:
            with open('text.json','r',encoding='utf-8') as f:
                data = json.load(f)
        except:
            print('Database loading proccess failed!')
    
    
program = Program()

program.load()

while True:
    print(f"""
    **********************************
    *            BY ALI              *
    **********************************
    *     1 - add data               *
    *     2 - delete data            *
    *     3 - show data              *
    *     4 - save board             *
    *     0 - quit                   *
    **********************************
    """)
    
    try:
        ch = int(input('Enter the number: '))
        
        if ch == 1:
            name: str = input('Enter student name: ')
            score: int = int(input('Enter the student score: '))
            program.add(name,score)
        elif ch == 2:
            name: str = input('Enter student name: ')
            program.delete(name)
        elif ch == 3:
            value = input('Show leaderboard or m letter (T/F): ')
            if value.upper() == 'T':
                program.show(True)
            elif value.upper() == 'F':
                program.show(False)
            else:
                program.show()
        elif ch == 4:
            program.download()
        elif ch == 0:
            break
        else:
            print('Enter valid number!')
    except Exception as e:
        print('Something went wrong!',e)
