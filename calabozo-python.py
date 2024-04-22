import time, random, os

# ---------------- DRAW FUNCTIONS ----------------

def line(): print("-----------------------------------------------------------------------------------------")



# ---------------- LOGIC FUNCTIONS ----------------

def  yes_no(): # Function that catch a yes or not decision

    while True:

        try:
            decision = str(input("(S/N): "))
        
            if decision == "S" or decision == "s" or decision == "N" or decision == "n": break

            else: print("Opción inválida, solo se acepta \"s\" o \"n\"")
        
        except: print("Opción inválida, solo se acepta \"s\" o \"n\"")
    
    return decision


def next(): next = input("\n --> Presiona Enter para continuar...")


def left_right(): # Function that catch a left or right decision

    while True:
        
        try:

            decision = str(input("(I/D): "))

            if decision == "I" or decision == "i" or decision == "D" or decision == "d": break

            else: print("Opción inválida, solo se acepta \"i\" o \"d\"")

        except: print("Opción inválida, solo se acepta \"i\" o \"d\"")

    return decision


def main():

    # while True:
    title = "Bienvenido a La Pesadilla"
    print("⛧"*len(title*2) + "\n" + title + "\n" + "⛧"*len(title*2))
    
    print("¿Iniciar el calvario?")
    start = yes_no()
    os.system("cls")

    if start == "s" or start == "S": # Start the nightmare
        morte_coin, satana_coin = False, False
        dagger = False
        random_number_1 = random.randint(1,667)
        random_number_2 = random.randint(1,667)
        random_number_3 = random.randint(1,667)

        print("""
              Oye hijo mío, el silencio.
              Es un silencio ondulado, un silencio donde resbalan valles y ecos,
              y que inclina las frentes hacia el suelo.
            """)
        
        next()
        line()

        print("""
            Despiertas en medio de la noche después de haber caído inconsciente a media pijamada por la cantidad de alcohol que tomaste.
            Recuerdas que la fiesta era en el departamento de uno de tus amigos que se mudó a la gran ciudad.
            Sin embargo, solo hay silencio, no hay sonido de autos, de claxons, no hay luz artificial exterior que penetre la penumbra del cuarto donde estás...
            sabes que estás solo, no sientes la presencia de tus amigos.
            """)

        line()
        time.sleep(1)
        
        print("\n ¿Te levantas de la cama?")
        wake_up = yes_no()
        os.system("cls")

        if wake_up == "s" or wake_up == "S":
            
            print("\n Al levantarte de la cama sientes como algo te toma violentamente de los tobillos y quiere arrastrate al fondo.")
            time.sleep(1)
            print("\n Después de forcejear logras librarte apenas.")
            time.sleep(1)
            print("\n Ya conoces la habitación, por lo que huyes a la puerta rogando que lo que sea que se arrastra apresuradamente hacia tí por la espalda no logre alcanzarte.")
            time.sleep(1)
            print("\n Logras salir y cerrar la puerta tras de tí, revisas tus bolsillos y encuentras tu telefono celular con el cual alumbras.")
            time.sleep(1)
            print("\n En el piso, en las paredes, solo humedad y manchas rojizas. Un aire pesado, no sabes que hay a los lados, se te heriza la piel de pensar en que puedes encontrar al voltear. ")
            time.sleep(1)
            print("\n En el piso frente a ti encuentras una moneda de hierro con la inscripción \"in morte ultima veritas. Vincit veritas in omnire\"")
            time.sleep(1)
            line()

            print("\n ¿Tomas la moneda?")
            take_morte_coin = yes_no()

            if take_morte_coin == "s" or take_morte_coin == "S":

                morte_coin = True
                print("\n Tomaste la moneda \"Morte\"")

            else: print("\n Ignoraste la moneda \"Morte\"")

            next()
            os.system("cls")

            print("\n Hay dos caminos, izquierda y derecha, tienes el presentimiento de que algo te observa desde la derecha, por el otro lado (izquierda) solo hay un silencio sepulcral...")
            time.sleep(1)
            line()

            print("\n ¿Qué camino eliges?")
            direction = left_right()
            os.system("cls")

if __name__ == "__main__":
    main()