from vagas import Receptor, Requisitor, ComandoIMP

receptor = Receptor()
requisitor = Requisitor()
cmd = ComandoIMP(receptor)

requisitor.comando(cmd)
requisitor.executar()