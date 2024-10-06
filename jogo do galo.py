class jodoDogalo:
    
    tabuleiro = { '7': '', '8': '', '9': '', '4': '', '5': '', '6': '', '1':'', '2': '', '3': ''}
    turno = None
    
    
    
    
    def _init__(self, jogador_inicial="X"):
        self.turno = jogador_inicial
        
        
    def exibirTabuleiro(self):
        print("┌───┬───┬───┐")    
        print (f"| {self.tabuleiro['7']} | {self.tabuleiro['8']} | {self.tabuleiro['9']} |")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("└───┴───┴───┘")
        
    def verificar_jogada(self, jogada):
        if jogada in self.tabuleiro.keys():
            if self.tabuleiro[jogada] == "  ":
                return True
        return False
        
        
    def verificar_tabuleiro(self):
        # verifica as 3 colonas
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != '':
            return self.tabuleiro['7']
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != '':
            return self.tabuleiro['8']
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != '':
            return self.tabuleiro['9']
        
        # Verificação das horizontais
        if self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != '':
            return self.tabuleiro['7']
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != '':
            return self.tabuleiro['4']
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] !='':
            return self.tabuleiro['1']
        
        # Verificação das diagonáis 
        elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] !='':
            return self.tabuleiro['7'] 
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] !='':
            
        # verificar empate 
        if [*self.tabuleiro.values()]
        