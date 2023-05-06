# les importations
import os
import socket
clear = lambda: os.system('cls')


#les actions autorisées par le serveur pour chaque client

# 1- 
def ConsulterVols(client):
  clear()
  client.sendall(bytes("ConsulterVols",'UTF-8'))  

# 2-
def ConsulterHistoriqueTransaction(client):
  clear()
  client.sendall(bytes("ConsulterHistoriqueTransaction",'UTF-8'))  

# 3-
def ConsulterFacture(client):
  clear()
  print("\nEntrez la reference du l'agence pour consulter facture :")
  ref=input()
  client.sendall(bytes("ConsulterFacture,{}".format(ref),'UTF-8'))  


# une des actions effectue par l'agenece : transaction qui présente la demande et l'annulation
# en faisant les mise a jour necessaires 

def transactionVol(client):
  clear()
  print("\n1- faire une demande ")
  print("\n2- faire une anulation")
  print("\n3- quitter")
  rsp=input()
  while(int(rsp) not in [1,2,3]):
    print("\nVotre choix est invalide , essayez de nouveau [1,2,3] !")
    rsp=input()
  msg=""
  if int(rsp)==1:
    print("\nentrez reference de vol")
    refVol=input()
    print("\nentrez reference de l'agence")
    refAg=input()
    print("\nentrez le nombre de place demandé")
    nbplace=input()
    msg="demande,{},{},{}".format(refVol,refAg,nbplace)
    client.sendall(bytes(msg,'UTF-8'))  

  if int(rsp)==2:
    print("entrez code reference de vol")
    refVol=input()
    print("entrez reference de l'agence")
    refAg=input()
    print("\nentrez le nombre de places Annulées")
    nbplace=input()
    msg="Annulation,{},{},{}".format(refVol,refAg,nbplace)
    client.sendall(bytes(msg,'UTF-8'))  

  if int(rsp)==3:
    actionClient(client)


# actions effectuees pour un client 

def actionClient(client):
  clear()
  response=0
  print("1- consulter la liste des vol")
  print("2- consulter l'historique du transaction des vols")
  print("3- consulter la facture à payer")
  print("4- etablir une trasaction")
  print("choix d'action :",end="")
  response=input()
  while int(response)not in [1,2,3,4]:
    print("Votre choix est invalide , essayez de nouveau [1,2,3,4] !")
    response=input()
  if(int(response) ==1):
    ConsulterVols(client)
  if(int(response) ==2):
    ConsulterHistoriqueTransaction(client)
  if(int(response) ==3):
    ConsulterFacture(client)
  if(int(response) ==4):
    transactionVol(client)




# le type du socket : SOCK_STREAM pour le protocole TCP
# le type du socket : SOCK_DGRAM pour le protocole UDP

SERVER = " 172.18.0.23"
PORT = 8084
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("Salut",'UTF-8'))
in_data =  client.recv(30720)
print("Connecting to server {}:{}".format(SERVER, PORT))

while True:

  actionClient(client) 
  in_data =  client.recv(5072)
  if(in_data.decode()!="Salut"):
    clear()
    print("From Server :" ,in_data.decode())
    input("Press Enter to continue...")
  
  if(in_data.decode()=="exit"):

    break
client.close()
