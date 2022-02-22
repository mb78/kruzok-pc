Krúžok PC pre deti
==================

Príklady a návody na stiahnutie sú rozložené po hodinách - nájdete to na stránke [github.com/mb78/kruzok-pc](https://github.com/mb78/kruzok-pc).

Budeme programovať hlavne vo verzii 3 jazyka Python, odkaz na [wikipédiu](https://sk.wikipedia.org/wiki/Python_(programovac%C3%AD_jazyk)),
verzia 2 je od roku 2020 neudržovaná. Rozdiely medzi týmito verziami sú na stránke [guru99.com/python-2-vs-python-3.html](https://www.guru99.com/python-2-vs-python-3.html) (anj).

Nainštalovanie softvéru (anj. software, programov) prejdeme na druhej hodine a popritom spravíme prvé pokusy.
Na ďalších preskúmame zložitejšie úlohy, niečo bude vždy nachystané, niečo si vymyslia deti alebo nás na hodine napadne.

Domáce úlohy nie sú, skôr ak majú deti doma možnosť a chuť, môžu skúsiť niečo vlastné. Čo nepôjde, pomôžeme na hodine.

Užitočné odkazy:
* [geo-inf.sk/materialy-k-pythonu](geo-inf.sk/materialy-k-pythonu)
* inštalácia interpretra jazyka Python
  * Linux (Ubuntu) - apt-get install python3
  * Windows 8 a vyššie (64 bit) - https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe
  * Windows 7 (32 bit) - https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe
  * poznámka: po spustení si zvoľte prvú možnosť - inštalovať s prostredím IDLE a tiež zaškrtnite voľbu na spodnej časti (pridať python do cesty pre spustenie)
* nainštalovanie knižnice `pygame`
  * Linux
    * `sudo python3 -m pip install pygame`
  * Windows
    * stlačte `Win` kláves spolu s `R` a do okna, ktoré sa zobrazí, odošlite `cmd`, zobrazí sa okno terminálu
    * v ňom instalovanie prebehne po spustené `py -m pip install pygame`

Adresáre
* elektronika - pár napadov, ako oživiť hodiny s použitím elektroniky - niekoľkých LED diód alebo matíc
* hodina-1, hodina-2, ... - mini projekty na každú hodinu
* hra - možete sa pohrať vo dvojici, originál hry je na adrese https://github.com/techwithtim/PygameForBeginners.git, spustíte ju pomocou `python3 main.py`
  * ďalšia hra je priamo v balíku `pygame`, spustíte ju príkazom `python3 -m pygame.examples.aliens`
