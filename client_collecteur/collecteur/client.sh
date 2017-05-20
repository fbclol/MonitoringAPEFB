#!/bin/bash

#*/5 * * * * root /home/monitoring/client.sh

# Collecteur bash
./collecteur.sh

# collecteur mixe
./collecteur_mixe.py

# collecteur python
./collecteur_python.py


# merge 
./../stockage_collection/merge.py


exit 0
