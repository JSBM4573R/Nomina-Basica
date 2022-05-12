sdatos=input()
adatos=sdatos.split(" ")
salario_base=float(adatos[0])
n_horas_extras=float(adatos[1])
bonificacion=float(adatos[2])
if bonificacion==1:
    bonificacion1=salario_base*0.095 
    horalaboral=salario_base/188
    v_horas_extra=n_horas_extras*(horalaboral*0.15+horalaboral)
    salario_total=salario_base+v_horas_extra+bonificacion1 
elif bonificacion==0:
    bonificacion0=salario_base*0
    horalaboral=salario_base/188
    v_horas_extra=n_horas_extras*(horalaboral*0.15+horalaboral)
    salario_total=salario_base+v_horas_extra+bonificacion0
desc1=salario_total*0.03
desc2=salario_total*0.03
desc3=salario_total*0.01
vpagar=salario_total-desc1-desc2-desc3
isalario_total=round(salario_total,1)
ivpagar=round(vpagar,1)
print(isalario_total,ivpagar)