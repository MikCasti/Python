
import Negozio
from exe05a import CapoAbbigliamento

try: 
    capomaglietta=CapoAbbigliamento("Maglietta","Nike",10,"S",5)
    capopantalone=CapoAbbigliamento("Jeans","Levis",20,"32",7)
    print(capomaglietta.get_marca())
    print(capopantalone.get_marca())
  
    print(capopantalone.get_tipo())

    capomaglietta.stampacosto()
    capomaglietta.cambiaprezzo(-10)
    capomaglietta.stampatocosto()

    capomaglietta.applicasconto(10)
    capomaglietta.stampacosto()

    print(capomaglietta)



except ValueError:
    print("Not valid")


negozio=Negozio("Negozio di Mario")
negozio.aggiungicapo(capomaglietta)
negozio.aggiungicapo(capopantalone)
print(negozio.stampaesistenze())

print(negozio.totalquantità())

 
