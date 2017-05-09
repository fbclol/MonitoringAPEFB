#!/bin/bash

## Supprime les sauvegardes et les répértoires  vieux  de plus de 5 jours
find $PDW/archive -name "*.gz" -mtime +5 -delete