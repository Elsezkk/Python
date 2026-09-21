Qualidade_Celular = 0.90

if Qualidade_Celular <= 0.65:
    print("É uma merda!")

elif Qualidade_Celular >= 0.66 and Qualidade_Celular <= 0.80:
    print("É mediano!")

elif Qualidade_Celular >= 0.81 and Qualidade_Celular <= 0.90:
    print("É bom!")

elif Qualidade_Celular >= 0.91 and Qualidade_Celular <= 1.00:
    print("É excelente!")

else :
    print("Valor inválido!")