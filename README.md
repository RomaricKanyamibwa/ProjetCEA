# ProjetCEA
Calcul de cycle dans les maillages à topologie non-triviale


Ce projet industriel portant sur le calcul de cycle dans les maillages a été fournit par l'entreprise CEA (Commissariat Énergie Atomique) et s’étend sur toute l’année faisant ainsi participer quatres étudiants (Ramatoulaye NDIAYE, Sophia HAKAM, Romaric KANYAMIBWA et Colette VOISEMBERT) sous la direction de Monsieur Xavier
CLAEYS (LJLL UPMC / INRIA Alpines) et Edouard DEMALDENT (CEA List).\\
La problématique de ce projet est le calcul de cycle dans les maillages à topologie non-triviale.

Pour celà, nous allons procéder comme suit : dans un premier temps, nous proposerons une méthode de « surmaillage » permettant de mettre en conformité deux maillages qui initialement ne sont pas conformes. Dans un second temps, considérant un maillage de surface fermée, nous nous intéresserons à déterminer
de manière automatique de tels chemins fermés, et à les visualiser plus particulièrement en s'intéressant aux cycles (propriétés conservées par déformation continue).

Comment lancer le code pour tester la méthode de surmaillage. 
Aller dans le dossier /ProjetCEA/Fusion_de_maillages/. Définissez les maillages M1 et M2 dont vous voulez calculer le surmaillage dans le fichier ProjetCEA/Fusion_de_maillages/chargement_des_donnees.py. Pour cela vous pouvez choisir comme entrée des fichiers de maillage .msh que vous aurez placé dans le dossier ProjetCEA/Fusion_de_maillages/Fichier_MSH/ au préalable. Ou définir les tableaux des noeuds (nodes, chaque ligne donne le numéro du noeud suivit de ses coordonnées en 3D) et celui des triangles (elems, chaque ligne donne le numéro du triangle suivit des trois numéros de noeuds de ses sommets) pour chaque maillage source. Pour pouvez tester les différents exemples déjà présents dans le fichier ProjetCEA/Fusion_de_maillages/chargement_des_donnees.py, en décommentant les exemples. Ensuite il vous suffit de lancer  ProjetCEA/Fusion_de_maillages/main.py et vous verrez s'afficher le maillage 3 (surmaillage des triangles sources) puis la superposition des deux maillages M1 et M2.

Il faut avoir installer les packages matplotlib et numpy et exécuter le code sous Python 2.7.




