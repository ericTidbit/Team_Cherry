# Overview

Nous sommes Team Cherry et nous avons besoin d'un programme qui simule la vie d'un silksong waiter.
Chaque jour, une option aléatoire parmi les suivantes est généré pour l'utilisateur:
1. Annoncer la date de sortie de Silksong (10%)
2. Shadowdrop Silksong (5%)
3. Générer du bait (70%)
4. Annoncer que nous sommes hard at work (10%)
5. Silksong est cancelled (5%)

À la fin de chaque jour, l'utilisateur a deux options:
- continuer au jour suivant
- se suicider (il perd automatiquement)

L'utilisateur gagne s'il est vivant le jour ou Silksong drop

# Annoncer la release date
La release date doit toujours être dans 5 jours (Silksong peut être cancelled entre temps)

# Shadowdrop
Le jeu shadowdrop demain, le lendemain l'utilisateur gagne (le jeu ne peut pas être cancelled le lendemain)

# Bait
Génère un bait qui peut ou ne peut pas être crédible (50/50). Si le bait est crédible, il a une chance aléatoire de soit
générer une fausse release date ou un faux shadowdrop

# Hard at work
Fait simplement afficher le message 'We are still hard at work'

# Cancelled
Silksong est cancelled, l'utilisateur se suicide immédiatement