````mermaid
classDiagram
class Silksong_waiter {
    -nom: str
    -sanity: int
    
    +pass_day(sanity)
    +kms(sanity) 
    }

class Compagnie {
    nom: str
    nombre_fan: int
    
    +annoncer()
    +shadowdrop_song()
    +generer_bait()
    +lie()
    +cancelled()
    
    }
Silksong_waiter "1" --> "1" Compagnie: relation toxique
````
