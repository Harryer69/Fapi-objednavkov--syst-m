
import sys
import os

#Přidání kořenového dresáře do sys.path, aby bylo možné naimportovat modul orders.py z nadřazené složky
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

#Import testované funkce
from objednavky import vypocet_dph

def test_vypocet_dph():
   
    """Funkce testuje správnost výpočtu DPH a výsledné ceny s DPH.
       Mezisoučet 1000 -> 21% DPH = 210 -> 1210"""
       
    mezisoucet = 1000
    dph, cena_s_dph = vypocet_dph(mezisoucet)
    
    assert dph == 210
    assert cena_s_dph == 1210