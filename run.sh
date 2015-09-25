#!/bin/bash

python normad.py
neo4j-shell --file nodelink.cyp
