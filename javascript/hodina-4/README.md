Prihlasovaci formular
=====================

Uloha: Vytvorime si maly formular na prihlasenie sa do chatovacej stranky.

1. Zadavat sa bude uzivatelske meno ("username") a heslo ("password").
2. Username musi mat aspon 5 znakov, inac sa formular neodosle
3. Password musi mat 8 znakov a musi obsahovat aspon jedno cislo
4. Styl stranky a JS skript budu ulozene v samostatnych suboroch

Co je formular ("form")
-----------------------
Zoskupenie vstupnych riadkov ("input lines"), tlacitok ("buttons"), zaskrtavacich policok (ano/nie: "checkbox", vyber 1 volby z N: "radio buttons") atd

Vlozenie skriptu do projektu stranky
------------------------------------
* zo samostatneho suboru alebo internetovej adresy ("URL" alebo "URI")
  `<script src="FILE.JS"></script>`
* vlozenim do html kodu do `<head>...</head>`
  `<script>DO SOMETHING</script>`
* vlozenim skriptu do HTML elementu (cokolvek ako `<ABC>`) - po kliknuti sa zavola `FUNCTION()`
  `<input type="button" value="Test" onclick="FUNCTION()"/>`

A vlozenie stylu
----------------
Da sa to aj bez kaskadnych stylov ("CSS" ako "Cascading Style Sheets")
`<p style="color:red; font-size: 20px;">`

Pre paragraf (text bez oddelenia znakom noveho riadku) cize tag `<p>...</p>` sa da nastavit styl pomocou
atributu `style`. Je to pracne, lahko sa urobi chyba a tazko sa robia zmeny, takychto tagov moze mat stranka tisice.

Budeme pouzivat CSS co je subor preddefinovanych stylov, ktore mozeme priradit paragrafom, formularom, tlacitkam, celej stranke...

Styly mozeme definovat "inline" sposobom, ked do html kodu - priamo do `<head>` tagu zapiseme
```code
<style>
p { color: powderblue; }
</style>
```

To je vhodne ak mame jeden html subor, kde chceme mat urcity styl. Ak suborov je viac, pouzijeme "externy CSS":

```code
<link rel="stylesheet" href=mystyle.css>
```
Tym sa pre stranku pouziju styly zo subory `mystyle.css`.
