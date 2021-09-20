from modulo_01_poo.ex_02_conta_bancaria.Classes import ContaCorrente, ContaPoupanca

cc = ContaCorrente(1, 2.5)
print("%.2f" % cc.saldo)
cc.depositar(1000)
print("%.2f" % cc.saldo)
cc.cobrar_taxa()
print("%.2f" % cc.saldo)

cp = ContaPoupanca(1, 0.15)
print("%.2f" % cp.saldo)
cp.depositar(1000)
print("%.2f" % cp.saldo)
cp.aplicar_juros()
print("%.2f" % cp.saldo)