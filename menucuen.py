from cuentas import Cuenta
import os
class MenuCuenta:
    @staticmethod
    def menu_cuenta():
        while True:
            print('*************** MENU AUTOMÓVILES ********************')
            print('    1- Registrar nueva cuenta')
            print('    2- Buscar cuenta por codigo')
            print('    3- Salir')
            print('*************** MENU AUTOMÓVILES   ********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
            if opcion == '3':
                print('Gracias por usar nuestra app..')
                os.system("pause")
                os.system("cls")
                break
                
            elif opcion == '1':
                
                print('     1. Registrar Cuenta -->')
                print('****************************************************************')
                cuenta1 = Cuenta()  
                cuenta1.guardar_cuenta()
                
                os.system("pause")
                os.system("cls")
            
            elif opcion == '2':
                print('    2.Buscar Cuenta Por Codigo-->')
                print('****************************************************************')
                
                cuenta1  = Cuenta()
                cuenta1.buscar_cuenta_codigo()
                os.system("pause")
                os.system("cls")
if __name__ == '__main__':
    MenuCuenta.menu_cuenta()