from flask import Flask, render_template, request

import requests

# Ceny dostupných produktů (CZK a kusy)
CENY = {
    "A":1500,
    "B":2500,
    "C":2000
}

def vypocet_dph(mezisoucet: int) -> int:
    
    """Funkce pro výpočet DPH 21 %. Tato funkce vrací hodnoty dph a cenu s DPH. """
    
    dph = mezisoucet * 0.21
    cena_s_dph = mezisoucet + dph
    return dph, cena_s_dph

def kurz_cnb(kod_meny: str) -> float:
    
    """Tato funke načte denní kurzovní lístek EURA z ČNB a vrací kurz zadané měny."""
    
    adresa = "https://www.cnb.cz/en/financial_markets/foreign_exchange_market/exchange_rate_fixing/daily.txt"
    
    odpoved = requests.get(adresa)
    radky = odpoved.text.splitlines()
    
    # Forcyklus pro nalezení kódu měny
    
    for radek in radky:
        if kod_meny in radek:
            rozdeleny_radek = radek.split("|")
            hledany_kurz = rozdeleny_radek[4].replace(",",".")
            return float(hledany_kurz)   
            
    
# Inicializace Flask aplikace    
orders = Flask(__name__)

@orders.route("/")
def home():
    """Zobrazí hlavní objednávkový formulář"""
    
    return render_template("index.html")

@orders.route("/order", methods=["POST"])
def order():
    """Zpracuje odeslaný formulář, vypočte ceny a zobrazí rekapitulaci"""
    
    # Načtení údajů z formuláře
    jmeno_prijmeni = request.form.get("jmeno_prijmeni")
    ico = request.form.get("ico")
    adresa = request.form.get("adresa")
    tel = request.form.get("telefon")
    email = request.form.get("email")
    datum = request.form.get("datum")
    produkt = request.form.get("produkt")
    kusy = int(request.form.get("kusy"))
    
    # Získání ceny za kus dle vybraného produktu.
    cena_za_kus = CENY[produkt]
    
    #Výpočet mezisoučtu
    mezisoucet = cena_za_kus * kusy
    
    #Výpočet DPH a ceny s DPH
    dph, cena_s_dph = vypocet_dph(mezisoucet)
    
    #Kurz eura dle ČNB    
    kurz_eura = kurz_cnb("EUR")
    
    #Přepočet ceny z CZK na EUR    
    cena_v_eurech = round(cena_s_dph / kurz_eura, 2)
    
    #Zobrazení stránky s rekapitulací objednávky
    return render_template("shrnuti_objednavky.html",
            jmeno_prijmeni=jmeno_prijmeni,
            ico=ico,
            adresa=adresa,
            telefon=tel,
            email=email,
            datum=datum,
            dph=dph,
            cena_s_dph=cena_s_dph,
            mezisoucet=mezisoucet,
            kurz_eura=kurz_eura,
            cena_v_eurech=cena_v_eurech            
            )  

      


if __name__ == "__main__":
    orders.run(debug=True)

