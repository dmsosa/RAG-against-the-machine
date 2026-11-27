This project vas developed as part of the 42 curriculum by _durisosa_

# R.A.G: 
`>>$ retrieval-augmented-generation`

-- 26-11-2026 --
Qu'est que c'est le RAG?

Le premier pas est avoir le codebase, ou le font d'information d'ou on extraere la information, dans notre case, c'est le source code et documentation du vLLMs.

Comment indexer une ficher? Quelles sont les objectifs de faire l'indexation?
L'indexation d'une fichier est une storage de donnés qui permait acceser l'information relevant on fonction de la requete avec une SimilaritySearch.

Comment est ce que je peux representer le Indexation comment une object, comment une pipeline?

-- Madrid, 27-11-2026 --

Maintenant, je pense que ca que il faut faire d'abbord est lire les ressources qu'on veut consommer one fois, et les lasses prepares pour touts les prompts qui le program receveira.

Mes questions sont les suivants:

- Est ce que le RAG est une program qui permettre consommer une numero fisse de prompts, et a la fin ca ecris les resultats sur une file output.txt?


# Chapitre Une: Les chunks

on doit garde les fichiers pertinents pour le projet dans le dossier /data/, ou /data/raw/ est l'endroit pour les fichiers crus qui n'ont etet trates.

Aussi, /data/processed/ est la place pour les fichiers apres le loading, chunking and indexing.

S'il y a des echecs pendant la creation d'une chunk, mon program continuerait avec le chunk prochaine, on creerait si chunks qui possible pour donner le plus de context.