from abc import ABC

class Comando(ABC):

  def __init__(self, receptor):
    self.receptor = receptor

  def processo(self):
    pass

class ComandoIMP(Comando):

  def __init__(self, receptor):
    self.receptor = receptor

  def processo(self):
    self.receptor.acao()

class Receptor:

  def acao(self):
    print('Abrir cancela!')

class Requisitor:

  def comando(self, cmd):
    self.cmd = cmd

  def executar(self):
    self.cmd.processo()