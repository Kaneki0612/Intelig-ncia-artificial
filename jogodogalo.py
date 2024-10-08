class JogoDoGalo:
    
    def __init__(self, jogador_inicial="X"):
        self.tabuleiro = { '7': '', '8': '', '9': '', '4': '', '5': '', '6': '', '1': '', '2': '', '3': ''}
        self.turno = jogador_inicial

    def exibirTabuleiro(self):
        print("┌───┬───┬───┐")    
        print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("└───┴───┴───┘")
        
    def verificar_jogada(self, jogada):
        if jogada in self.tabuleiro.keys() and self.tabuleiro[jogada] == '':
            return True
        return False
        
    def verificar_tabuleiro(self):
        # Verificação das colunas
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != '':
            return self.tabuleiro['7']
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != '':
            return self.tabuleiro['8']
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != '':
            return self.tabuleiro['9']
        
        # Verificação das linhas
        if self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != '':
            return self.tabuleiro['7']
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != '':
            return self.tabuleiro['4']
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != '':
            return self.tabuleiro['1']
        
        # Verificação das diagonais
        if self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != '':
            return self.tabuleiro['7']
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != '':
            return self.tabuleiro['1']
        
        # Verificar empate
        if '' not in self.tabuleiro.values():
            return "empate"
        
        return None
        
    def jogar(self):
        while True:
            self.exibirTabuleiro()
            print(f"Turno do {self.turno}, qual é a próxima jogada?")
            
            # Enquanto a jogada não for válida
            while True:
                jogada = input("jogada (1-9): ")
                
                if self.verificar_jogada(jogada):
                    break
                else:
                    print(f"Jogada do {self.turno} inválida, jogue novamente.")
            
            # Atualizar o tabuleiro com a jogada
            self.tabuleiro[jogada] = self.turno
            
            # Verificar se há um vencedor ou empate
            estado = self.verificar_tabuleiro()
            
            if estado == "X":
                self.exibirTabuleiro()
                print("X é o vencedor!")
                break
            elif estado == "O":
                self.exibirTabuleiro()
                print("O é o vencedor!")
                break
            elif estado == "empate":
                self.exibirTabuleiro()
                print("Empate!")
                break
            
            # Troca para a próxima jogada
            self.turno = "X" if self.turno == "O" else "O"

# Criação e execução do jogo
jogo = JogoDoGalo()
jogo.jogar()
