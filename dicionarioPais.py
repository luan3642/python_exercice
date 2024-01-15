pais_capital = [
    {
    "Pais": "Brasilia",
},
    {
        "Pais": "Washington",
    },
    {
       "Pais" : "Berlim", 
    },

    {
       "Pais" : "Buenos Aires", 
    },
    
    {
        "Pais" : "Camberra",
    },
    
    {
       "Pais" : "Viena", 
    },
    
    {
        "Pais" : "Nassau"
    }

]

ordena = sorted(pais_capital, key=lambda pais_capital : pais_capital["Pais"])

for x in ordena:
    print(x)