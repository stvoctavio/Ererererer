#Almacenar
meme_dict ={ "LOL": "una respuesta a algo gracioso, en pocas palabra, riendo fuerte", "CRINGE": "algo raro o embarazoso", "ROFL": "una respuesta a una broma", "SHEESH": "ligera desaprobación", "CREEPY": "aterrador, siniestro", "AGGRO": "ponerse agresivo/enojado"}

#Hacer una solicitud
dic = input("que quieres saber hoy? con mayusculas porfa")

#procesar su solicitud
if dic in meme_dict.keys():
    print(meme_dict[dic])
else:
    print("Esta palabra no se encuentra")
