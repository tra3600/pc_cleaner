# pc_cleaner
nettoie les fichiers temp optimise la RAM et les perf du PC

Créer un programme qui imite les fonctionnalités de PC Cleaner nécessitera plusieurs étapes et l'utilisation de différentes bibliothèques pour gérer la mémoire, nettoyer les fichiers temporaires, et optimiser les performances.

1. Nettoyage des fichiers temporaires
Pour nettoyer les fichiers temporaires, nous pouvons utiliser Python pour accéder et supprimer ces fichiers.

2. Gestion de la mémoire vive
Pour gérer la mémoire vive, nous pouvons utiliser des bibliothèques comme psutil pour surveiller et libérer la mémoire.

3. Optimisation des performances
Pour optimiser les performances, nous pouvons implémenter des fonctionnalités comme la gestion des processus et la désactivation des programmes au démarrage.

Prérequis
Installez les bibliothèques nécessaires :

pip install psutil

Explications
Nettoyage des fichiers temporaires :

clean_temp_files : Cette fonction nettoie les fichiers temporaires dans les dossiers spécifiés par les variables d'environnement TEMP et TMP.
Optimisation de la mémoire :

optimize_memory : Cette fonction optimise l'utilisation de la mémoire en vidant le cache du système. Notez que l'utilisation de /proc/sys/vm/drop_caches est spécifique aux systèmes UNIX/Linux et nécessite des privilèges root. Pour Windows, vous devrez utiliser des méthodes spécifiques à Windows pour gérer la mémoire.
Fonction principale :

main : Cette fonction appelle les fonctions de nettoyage et d'optimisation et affiche un message une fois l'optimisation terminée.
Notes
Permissions : Certaines opérations, comme la gestion de la mémoire avec /proc/sys/vm/drop_caches, nécessitent des privilèges administratifs.
Compatibilité : Le code ci-dessus est principalement pour les systèmes UNIX/Linux. Pour Windows, vous devrez utiliser des API spécifiques à Windows comme ctypes ou pywin32 pour accéder aux fonctionnalités système.
Précautions : Soyez prudent lors de la suppression de fichiers et de la gestion de la mémoire. Assurez-vous de ne pas supprimer des fichiers critiques du système.
Ce programme offre une base pour nettoyer et optimiser un PC. Vous pouvez l'étendre pour inclure des fonctionnalités supplémentaires comme la gestion des processus au démarrage, la défragmentation du disque, etc.
