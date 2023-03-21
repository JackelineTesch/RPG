class SerVivo:
    def __init__(self, pontos_de_vida, pontos_de_ataque, pontos_de_defesa):
        self.pontos_de_vida = pontos_de_vida
        self.pontos_de_ataque = pontos_de_ataque
        self.pontos_de_defesa = pontos_de_defesa
        
    def atacar(self, inimigo):
        dano = self.pontos_de_ataque - inimigo.pontos_de_defesa
        if dano > 0:
            inimigo.pontos_de_vida -= dano
            print(f"{self.nome} ataca {inimigo.tipo} e causa {dano} pontos de dano.")
        else:
            print(f"{self.nome} ataca {inimigo.tipo}, mas não causa nenhum dano.")
            
    def contraAtacar(self,heroi):
        dano = self.pontos_de_ataque - heroi.pontos_de_defesa
        if dano > 0:
            heroi.pontos_de_vida -= dano
            print(f"{self.tipo} ataca {heroi.nome} e causa {dano} pontos de dano.")
        else:
            print(f"{self.tipo} ataca {heroi.nome}, mas não causa nenhum dano.")
        

class Personagem(SerVivo):
    def __init__(self, nome, pontos_de_vida, pontos_de_ataque, pontos_de_defesa):
        super().__init__(pontos_de_vida, pontos_de_ataque, pontos_de_defesa)
        self.nome = nome
        
class Monstro(SerVivo):
    def __init__(self, tipo, pontos_de_vida, pontos_de_ataque, pontos_de_defesa):
        super().__init__(pontos_de_vida, pontos_de_ataque, pontos_de_defesa)
        self.tipo = tipo
        
class Lobo(Monstro):
    def __init__(self):
        super().__init__("Lobo", pontos_de_vida=80, pontos_de_ataque=90, pontos_de_defesa=70)
        self.forca = 100
    
class Goblin(Monstro):
    def __init__(self):
        super().__init__("Goblin", pontos_de_vida=60, pontos_de_ataque=70, pontos_de_defesa=100)
        self.inteligencia = 100
        

  ##Testando o ataque:
  
steve = Personagem("Steve", 50, 60, 50)
goblin = Goblin()

steve.atacar(goblin)

goblin.contraAtacar(steve)


        
        


