def grafica(m, v, pcov, longitud):
    # Error estándar de la pendiente
    sigma_m = np.sqrt(pcov[0, 0])

    # Calcular los valores ajustados y las bandas de error
    y_fit = m * longitud
    y_fit_upper = (m + sigma_m) * longitud
    y_fit_lower = (m - sigma_m) * longitud

    # Crear la gráfica
    plt.figure(figsize=(10, 6))

    # Línea de ajuste
    plt.plot(longitud, y_fit, color='black', linestyle='-', label='Ajuste lineal')

    # Puntos de datos
    plt.scatter(longitud, v, color='white', edgecolors='tab:red', s=40, label='Datos')

    # Barras de error (en x)
    plt.errorbar(longitud, v, xerr=0.001, fmt='None', ecolor='tab:red', alpha=0.5)

    # Área de error
    plt.fill_between(longitud, y_fit_lower, y_fit_upper, color='red', alpha=0.2, label='Área de error')

    # Etiquetas y leyenda
    plt.ylabel(r'Voltaje $[V]$')
    plt.xlabel(r'Longitud $[m]$')
    plt.legend()
    plt.grid(True)

    # Mostrar la gráfica
    plt.show()