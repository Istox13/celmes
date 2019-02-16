'''Шаблон для создания игры
1) Название файла игры должно начинаться с маленькой g далее название игры с большой буквы на английском языке без каких-либо разделителей(примером может послужить название этого файла)'''

class Template:
    def __init__(self):
        self.score = 0
        self.lvl = 1
        self.print_next = False
        self.status = ''
        self.game = True
        self.speed = 1

    def motion(self, evant):
        '''Передается список нажатых кнопок'''
        
    
    def render(self):
        f'''Вызывается через {self.speed} секунд при self.game == True'''
