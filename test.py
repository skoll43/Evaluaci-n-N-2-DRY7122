
'''
B.	Consumo de API Pública
Utilizando el sitio de MapQuest y el token generado en laboratorio respectivo, deberá crear un código en VisualStudio Code de la máquina virtual DEVASC, donde el programa realice lo siguiente:

•	Medir la distancia en kilómetros entre Santiago y Ovalle.
•	Solicitar “Ciudad de Origen” y “Ciudad de Destino”
•	Mostrar la duración del viaje en horas, minutos y segundos
•	Mostrar el combustible requerido para el viaje representado en litros
•	Todos los valores deben utilizar dos decimales.
•	Debe imprimir la narrativa del viaje.
•	Agregar una salida del programa con la letra “q”
•	Subir el script creado en un repositorio público en GitHub con el nombre de “Evaluación N°2 DRY7122” y en la descripción los nombres de los integrantes. Debe incluir un commit con el nombre de “Consumo de API Pública”

'''


import urllib.parse
import requests

while True:
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    orig = input("ingrese ciudad de origen:\n")
    dest = input("ingrese ciudad de destino:\n")
    key = "tKJdyWn9sR1b4HmByXAiej0rI5ksKmRr"
    if orig == "q" or dest == "q":
        break
    
    url = main_api + urllib.parse.urlencode({"key" :key, "from" :orig, "to" :dest})

    json_data = requests.get(url).json()
    json_status = json_data ["info"] ["statuscode"]

    print(url,"es la url")

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")

        break
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

