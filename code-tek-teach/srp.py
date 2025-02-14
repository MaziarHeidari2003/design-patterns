class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self,text):
        self.count += 1
        self.entries.append(f'{self.count}:{text}')

    def remove_entry(self,pos):
        del self.entries[pos]


    def __str__(self):
        return '\n'.join(self.entries)
    
    # def save(self,filename):
    #     file = open(filename,'w')
    #     file.write(str(self))
    #     file.close()

    # bad code !

class PersistanceManager:
    
    @staticmethod
    def save_to_file(journal,filename):
        file = open(filename,'w')
        file.write(str(journal))
        file.close










j = Journal()
j.add_entry('This is the worst thing in the world')
print(j)
                
file = r'H:\programming\desgin-patterns\s.txt'
PersistanceManager.save_to_file(j,file)

with open(file) as fh:
    print(fh.read())
