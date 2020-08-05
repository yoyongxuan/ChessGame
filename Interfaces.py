class ConsoleInterface:
    def __init__(self):
        self.stdscr = curses.initscr()
        self.board = self.create_window(11,22,0,14,'Board')
        self.messages = self.create_window(5,50,11,0,'Messages')
        self.player = self.create_window(3,50,16,0,'Player')

    @staticmethod
    def create_window(height,width,y,x,label):
        border = curses.newwin(height,width,y,x)
        border.border()
        border.addstr(0,0,label)
        border.refresh()
        window = curses.newwin(height-2,width-4,y+1,x+2)
        return window

    def set_board(self, inputstr):
        '''
        Takes board info as an inputstr
        and prints it to the console.
        '''
        self.board.clear()
        inputlist = inputstr.split('\n')
        for row in range(len(inputlist)):
            self.board.addstr(row,0,inputlist[row])
        self.board.refresh()

    def set_msg(self, inputstr):
        '''
        Takes an inputstr and prints it
        to the console.
        '''
        self.messages.clear()
        self.messages.addstr(0,0,f'{inputstr}')
        self.messages.refresh()
        pass

    def get_player_input(self, msgstr):
        '''
        Prompts the user with a msgstr,
        returns their input as str.
        '''
        self.player.clear()
        self.player.addstr(0,0,msgstr)
        value = self.player.getstr()
        string = value.decode('utf-8')
        self.player.refresh()
        return string
