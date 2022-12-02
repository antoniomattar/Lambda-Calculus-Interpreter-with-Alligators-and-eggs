from ast import Not
from numpy import save
import logic
import parsing
import image_maker
import app_functions
import os
import time
import pyfiglet
import keyboard
import shutil
import platform

if platform.system() == 'Windows':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

welcome_banner = pyfiglet.figlet_format('LambdaCalculus Interpreter')
good_bye_banner = pyfiglet.figlet_format('Goodbye!')

main_menu_options = {
    1: 'Beta-Reduction',
    2: 'Interactive Beta-Reduction',
    3: 'Arithmetic Operations',
    4: 'Show Numbers',
    5: 'boolean expression',
    6: 'Exit',
}

arithmetic_operations_options = {
    1: 'Addition',
    2: 'Subtraction',
    3: 'Multiplication',
    4: 'Power',
    5: 'Successor',
    6: 'Predecessor',
    7: 'Back',
}

choice_number_representation= {
    1: 'Integer numbers (church representation)',
    2: 'Relative numbers',
    3: 'Back'
}

boolean_representation= {
    1: 'NOT',
    2: 'AND',
    3: 'OR',
    4: 'XOR',
    5: 'IS_ZERO',
    6: 'back'

}

def save_images(terme,nom,date):
    os.makedirs("/sauvegarde", exist_ok=True)
    logic.captureImage(terme,"/sauvegarde",nom,date)

def delete_images(folder):
    if os.path.exists(folder):
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
def moveImages(src, dest):
	for filename in os.listdir(src):
         if os.path.isfile(dest+'/'+filename):
            os.remove(dest+'/'+filename)
         shutil.move(src+"/"+filename, dest)

def return_main_menu():
    image_maker.colors = ['black','blue','green','orange','pink','purple','red','yellow']
    not_pressed = True
    print('Press ENTER to return to the main menu')
    while not_pressed:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('ENTER'):  # if key 'ENTER' is pressed 
                not_pressed = False  # finishing the loop
                clear()
                time.sleep(1)
                logic.image_counter = 0
                image_maker.variables_colors_couple = {}
                break
        except:
            break  # if user pressed a key other than the given key the loop will break
    run_main_menu()

def run_beta_reduction_totale(terme,path='beta_reduction_totale'):
    terme = parsing.parseTerm(terme)
    if logic.recognize_term(terme):
        print(" terme infini detecté")
        return None
    os.makedirs(path, exist_ok=True)# cree le rep si il existe pas, le vide si non
    if len(os.listdir(path)) > 0:
        logic.image_counter = 0
    k=logic.beta_reduction_totale(terme,path)
    print(" le terme obtenu est: "+logic.to_string(k))
    save_image_choice = input('Do you want to save the images? (Y/n): ')
    while save_image_choice not in ['y','n','']:
            save_image_choice = input('Invalid choice. Do you want to save the images? (Y/n): ')
    if save_image_choice == 'y' or save_image_choice=='':
        os.makedirs("./sauvegarde/"+path, exist_ok=True)
        moveImages(path,'./sauvegarde/'+path)
        os.rmdir(path)
    elif save_image_choice=='n':
        delete_images(path)
        os.rmdir(path)

def run_beta_reduction_interactive_totale(terme,path='beta_reduction_interactive_totale'):
    terme = parsing.parseTerm(terme)
    if logic.recognize_term(terme):
        print(" terme infini detecté")
        return None
    os.makedirs(path, exist_ok=True)
    if len(os.listdir(path)) > 0:
        logic.image_counter = 0
    logic.beta_reduction_interactive_totale(terme,path)
    save_image_choice = input('Do you want to save the images? (Y/n): ')
    while save_image_choice not in ['y','n','']:
            save_image_choice = input('Invalid choice. Do you want to save the images of the reduction? (Y/n): ')
    if save_image_choice == 'y'or save_image_choice=='':
        os.makedirs("./sauvegarde/"+path, exist_ok=True)
        moveImages(path,'./sauvegarde/'+path)
        os.rmdir(path)
    elif save_image_choice == 'n':
        delete_images(path)
        os.rmdir(path)

def run_show_numbers(path):
    os.makedirs(path, exist_ok=True)
    print_menu(choice_number_representation)
    choice = int(input('Enter your choice: '))
    while choice not in main_menu_options:
        clear()
        print_menu(choice_number_representation)
        choice = int(input('Invalid choice. Enter your choice: '))
    if choice ==1:
        clear()
        terme = int(input('Enter a number: '))
        while terme < 0:
            terme = int(input('Enter a number: '))
        t = app_functions.dec_to_church(terme)
        print('Voici le terme:',logic.to_string(t))
        logic.captureImage(t,path,'ENTIER'+str(terme),False)
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images of the reduction? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y' or save_image_choice == 'Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)

    elif choice==2:
        clear()
        terme = int(input('Enter a number: '))
        t = app_functions.dec_to_lambda_relative_integers(terme)
        print('Voici le terme:',logic.to_string(t))
        logic.captureImage(t,path,'ENTIER-RELATIF#'+'('+str(terme)+')',False)
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images of the reduction? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)
    elif choice==3:
        run_main_menu()

def run_boolean_expression(path):
    os.makedirs(path, exist_ok=True)
    print_menu(boolean_representation)
    choice = int(input("enter your choice : "))
    while choice not in boolean_representation:
        clear()
        print_menu(boolean_representation)
        choice = int(input('Invalid choice. Enter your choice: '))
    if choice ==1:
        clear()
        t = app_functions.NOT
        print('Voici le terme:',logic.to_string(t))
        logic.captureImage(t,path,'NOT',False)
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images of the reduction? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)
    elif choice==2:
        clear()
        t = app_functions.AND
        print('Voici le terme:',logic.to_string(t))
        logic.captureImage(t,path,'AND',False)
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images of the reduction? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)
    elif choice==3:
        clear()
        t = app_functions.OR
        print('Voici le terme:',logic.to_string(t))
        logic.captureImage(t,path,'OR',False)
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images of the reduction? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)
    elif choice ==4:
        clear()
        t = app_functions.XOR
        print('Voici le terme:',logic.to_string(t))
        logic.captureImage(t,path,'XOR',False)
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images of the reduction? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)

    elif choice==5:
        clear()
        t = app_functions.IS_ZERO
        print('Voici le terme:',logic.to_string(t))
        logic.captureImage(t,path,'IS_ZERO',False)
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images of the reduction? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)
    elif choice==6:
        run_main_menu()

    


#------------------------------------------------------------------------------------------------------------------------------------

def print_menu(options):
    for key, value in options.items():
        print(key,'--',value)

def run_main_menu():
    choice = ''
    print(welcome_banner)
    print_menu(main_menu_options)
    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        clear()
        print_menu(main_menu_options)
    while choice not in main_menu_options:
        choice = int(input('Enter your choice: '))
    if choice == 1:
        clear()
        terme1 = input('Enter a term: ')
        k=run_beta_reduction_totale(terme1)
        if k!=None:
          clear()
          print('Done!')
        else:
            time.sleep(2)
        return_main_menu()
    elif choice == 2:
        clear()
        terme2 = input('Enter a term: ')
        v= run_beta_reduction_interactive_totale(terme2)
        if v!=None:
          clear()
          print('Done!')
        else:
            time.sleep(2)
        return_main_menu()
    elif choice == 3:
        clear()
        run_arithmetic_operations_menu()
    elif choice == 4:
        clear()
        run_show_numbers('show_numbers')
        return_main_menu()
    elif choice== 5:
        clear()
        run_boolean_expression('boolean expression')
        return_main_menu()
    elif choice == 6:
        clear()
        print(good_bye_banner)

def run_arithmetic_operations_menu(path='arithmetic expressions'):
    os.makedirs(path, exist_ok=True)
    print_menu(arithmetic_operations_options)
    choice = int(input('Enter your choice: '))
    while choice not in arithmetic_operations_options:
        clear()
        print_menu(arithmetic_operations_options)
        choice = int(input('Invalid choice. Enter your choice: '))
    if choice == 1:
        clear()
        print("Voici le terme: "+ logic.to_string(app_functions.ADD))
        logic.captureImage(app_functions.ADD,path,'ADD', False)
        choix=(input("Do you want to try an example? (Y/n) : "))
        while choix not in ['y','n','']:
            choix = input('Invalid choice. Do you want to try an example? (Y/n): ')
        if choix=='y' or choix=='':
            clear()
            print("you are going to try n+m")
            n=int(input("give n : "))
            m=int(input("give m : "))
            while n < 0 or m < 0:
                clear()
                print('Relative addition is not possible. Try again.')
                n=int(input("give n : "))
                m=int(input("give m : "))
            app_functions.add(app_functions.dec_to_church(n),app_functions.dec_to_church(m))
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)
        return_main_menu()
    elif choice == 2:
        clear()
        print("Voici le terme: "+ logic.to_string(app_functions.SUB))
        logic.captureImage(app_functions.SUB,path,'SUB', False)
        choix=(input("Do you want to try an example? (Y/n) : "))
        while choix not in ['y','n','']:
            choix = input('Invalid choice. Do you want to try an example? (Y/n): ')
        if choix=='y' or choix=='':
            clear()
            print("you are going to try n-m")
            n=int(input("give n : "))
            m=int(input("give m : "))
            while m > n:
                clear()
                print('Relative substraction is not possible. Try again.')
                n=int(input("give n : "))
                m=int(input("give m : "))
            app_functions.sub(app_functions.dec_to_church(n),app_functions.dec_to_church(m))
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['Y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images of the reduction? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)
        return_main_menu()
    elif choice == 3:
        clear()
        print("Voici le terme: "+ logic.to_string(app_functions.MUL))
        logic.captureImage(app_functions.MUL,path,'MUL',False)
        choix=(input("Do you want to try an example? (Y/n) : "))
        while choix not in ['y','n','']:
            choix = input('Invalid choice. Do you want to try an example? (Y/n): ')
        if choix=='y' or choix=='':
            clear()
            print("you are going to try n*m")
            n=int(input("give n : "))
            m=int(input("give m : "))
            while m < 0 or n < 0:
                clear()
                print('Relative multiplication is not possible. Try again.')
                n=int(input("give n : "))
                m=int(input("give m : "))
            app_functions.multiplication(app_functions.dec_to_church(n),app_functions.dec_to_church(m))
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)
        return_main_menu()
    elif choice==4:
        clear()
        print("Voici le terme: "+ logic.to_string(app_functions.POW))
        logic.captureImage(app_functions.POW,path,'POWER',False)
        choix=(input("Do you want to try an example? (Y/n) : "))
        while choix not in ['y','n','']:
            choix = input('Invalid choice. Do you want to try an example? (Y/n): ')
        if choix=='y' or choix=='':
            clear()
            print("you are going to try n puiss m")
            n=int(input("give n : "))
            m=int(input("give m : "))
            while m < 0 or n < 0:
                clear()
                print('Relative power is not possible. Try again.')
                n=int(input("give n : "))
                m=int(input("give m : "))
            app_functions.power(app_functions.dec_to_church(n),app_functions.dec_to_church(m))
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images of the reduction? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)
        return_main_menu()
    elif choice==5:
        clear()
        print("Voici le terme: "+ logic.to_string(app_functions.SUCCS))
        logic.captureImage(app_functions.SUCCS,path,'SUCCS',False)
        choix=(input("Do you want to try an example? (Y/n) : "))
        while choix not in ['y','n','']:
            choix = input('Invalid choice. Do you want to try an example? (Y/n): ')
        if choix=='y'or choix=='':
            clear()
            print("you are going to try n+1")
            n=int(input("give n : "))
            while n<0:
                clear()
                print('Relative integers not possible. Try again.')
                n=int(input("give n : "))
            app_functions.succ(app_functions.dec_to_church(n))
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images ? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)
        return_main_menu()
    elif choice==6:
        clear()
        print("Voici le terme: "+ logic.to_string(app_functions.PRED))
        logic.captureImage(app_functions.PRED,path,'PRED',False)
        choix=(input("Do you want to try an example? (Y/n) : "))
        while choix not in ['y','n','']:
            choix = input('Invalid choice. Do you want to try an example? (Y/n): ')
        if choix=='y' or choix=='':
            clear()
            print("you are going to try n-1")
            n=int(input("give n : "))
            while n<0:
                clear()
                print('Relative integers not possible. Try again.')
                n=int(input("give n : "))
            app_functions.predec(app_functions.dec_to_church(n))
        save_image_choice = input('Do you want to save the images? (Y/n): ')
        while save_image_choice not in ['y','n','']:
                save_image_choice = input('Invalid choice. Do you want to save the images? (Y/n): ')
        if save_image_choice == 'y' or save_image_choice=='' or save_image_choice=='Y':
            os.makedirs("./sauvegarde/"+path, exist_ok=True)
            moveImages(path,'./sauvegarde/'+path)
            os.rmdir(path)
        elif save_image_choice == 'n':
            delete_images(path)
            os.rmdir(path)
        return_main_menu()
    elif choice == 7:
        clear()
        run_main_menu()

run_main_menu()