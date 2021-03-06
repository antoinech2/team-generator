
import random

#["psuedo",staff 0/1, dispo 1-5, [liste ami], [liste ennemi]]

data = 	[ \
        #SYNTAXE: ["Pseudo", rang (0/1), coefficient de disponibilité (1-5), [liste ami], [liste ennemi]]
		["antoinech",1,4,["Erhoss", "Aquariium", "Kiillua_","Crowning"],["Armadindon","LaTartOP0ireS_","Kazuyo"]], \
        ]

continue_calculate = True
number_generation = 0
max_diff = 100
max_time_distance = 3

def GenerateRandomTeam():
	global continue_calculate, number_generation, max_diff
	equipes = [[],[],[],[],[],[]]
	equipe_player = {}
	number_generation += 1
	if number_generation%10000 == 0:
		print("Génération n°",number_generation,"...")
	#Génération totalement aléatoire:
	for player_data in data:
		rand = random.randint(0,5)
		while (len(equipes[rand]) >= 4):
			rand = random.randint(0,5)
		equipes[rand].append(player_data[0])
		equipe_player[player_data[0]] = rand

	#Vérification des ennemis:
	for player_data in data:
		for ennemis in player_data[4]:
			if ennemis in equipes[equipe_player[player_data[0]]]:
				#print("Ennemi non respecte. Abandon...")
				return

	#Vérification des amis:
	for player_data in data:
		if len(player_data[3]) > 0:
			amis = 0
			for ami in player_data[3]:
				if ami in equipes[equipe_player[player_data[0]]]:
					amis += 1
			if amis == 0:
				#print("Ami non respecté. Abandon...")
				return

	#Vérification de l'équilibre staff/joueur
	staffs = [0]*6
	joueurs = [0]*6
	total_play_time = [0]*6
	for player_data in data:
		if player_data[1] == 1:
			staffs[equipe_player[player_data[0]]] += 1
		else:
			joueurs[equipe_player[player_data[0]]] += 1
	for equipe in range (6):
		if staffs[equipe] == 0 or staffs[equipe] == 4 or joueurs[equipe] == 0 or joueurs[equipe] == 4:
			#print("Equité staff/joueur non respectée. Abandon...")
			return

	#Calcul des temps de jeu
	for player_data in data:
		total_play_time[equipe_player[player_data[0]]] += player_data[2]
	max_diff = abs(min(total_play_time)-max(total_play_time))


	if max_diff <= max_time_distance:
		continue_calculate = False
		print("CWS2 Random Team Generator v1.2 for Windalia by antoinech (Python 3.7)")
		print("Génération n°",number_generation)
		print("Equipe validée. Respect de tous les critères.")
		for equipe in range (6):
			print("Equipe n°",equipe+1,": ",equipes[equipe], "      Temps de jeu total: ",total_play_time[equipe], sep="")
		print("Différence de temps de jeu maximal entre équipes:", max_diff)
		print("Equipe valide trouvée en", number_generation, "générations.")
	return


while continue_calculate:
	GenerateRandomTeam()
