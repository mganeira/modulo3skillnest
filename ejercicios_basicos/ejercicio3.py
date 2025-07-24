#input
kilos_comprados_manzana=input("¿Cuántos kilos de manzana lleva?:  ")
kilos_comprados_naranja=input("¿Cuántos kilos de naranja lleva?:   ")
valor_naranja=input("Ingresa valor naranja")
valor_manzana=input("Ingresa valor naranja")

valor_total_manzana= valor_manzana * kilos_comprados_manzana
valor_total_naranja= valor_naranja * kilos_comprados_naranja

valor_total=valor_total_manzana + valor_total_naranja

print(f"El costo total de tu compra es {valor_total}")