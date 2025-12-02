FAPI – Objednávkový systém (testovací úkol)

Tento projekt je jednoduchý objednávkový systém vytvořený jako součást přijímacího řízení.  
Aplikace je postavena na Pythonu, Flasku a využívá HTML a CSS.


Funkce aplikace

1. Objednávkový formulář
Uživatel může vyplnit:
- Jméno a příjmení / Společnost  
- IČO  
- Adresu  
- Telefon  
- Email  
- Datum objednávky  
- Výběr produktu  
- Počet kusů

Formulář obsahuje HTML validace.

Součástí je také automatický výpočet celkové ceny podle produktu a počtu kusů.
Formulář má funkční tlačítko odeslat.

2. Rekapitulace objednávky
Po odeslání formuláře se uživateli zobrazí rekapitulace:
- Celý seznam zadaných údajů
- Mezisoučet ceny
- DPH (21 %)
- Cena s DPH
- Kurz EUR podle ČNB
- Cena v EUR po přepočtu

V rekapitulaci objednávky dojde k výpočtu DPH a přičtení tohoto DPH k mezisoučtu.

Součástí rekapitulace je také výpis aktuálního kurzu eura a přepočt ceny z CZK na EUR.

