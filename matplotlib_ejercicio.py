import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
ventas = [150, 200, 180, 220, 170, 190, 230, 210, 300, 320, 280, 350]

plt.plot(meses, ventas)
plt.xlabel('Meses')
plt.ylabel('Ventas')
plt.title('Evolución de Ventas Mensuales')
plt.show()
