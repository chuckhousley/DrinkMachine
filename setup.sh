#!/bin/bash

if [ ! -f drink.db]; then
    sqlite3 drink.db < setup/createtable.sql
fi
