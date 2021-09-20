from modulo_01_poo.ex_03_e_commerce.Classes import Livro, Brinquedo, CestaCompras

livro1 = Livro("Senhor dos Aneis", 15.00)
brinq1 = Brinquedo("Carrinho", 12.99)

cesta = CestaCompras()
cesta.adicionar_item(livro1, 3)
cesta.adicionar_item(brinq1, 4)

cesta.relatorio_final()
