### Hra VLAKOVY DISPECING

Vitaj na smene vlakoveho dispecera na trati Prievidza - Kralovany.

1. Po spusteni hry sa zobrazi tabulka so zoznamom vlakov, ktory musis cely odbavit.
2. Kazdy vlak ma svoje ID, kategoriu, cislo, vychodziu a konecnu stanicu, meskanie a maximalnu rychlost vlaku.
3. Musis sa rozhodnut, ktory vlak sa rozhodnes odbavit ako prvy. Samozrejme pozor si musis davat sa stanice vlakov. Ak si vyberies vlak napr. s konecnou stanicou Tekovany, 
   tak vlak v stanici ostava pokym si nevyberies vlak s pociatocnou stanicou Tekovany, t.j. hra si pamata stav obsadenia kolaji.
	Doporucene poradie odbavovania vlakov:
		Pociatocna/Konecna stanica: ... -> znamena, ze vlak prichadza/konci z/v oblasti mimo mapu
 		Meskanie: cim vacsie, tym vacsia priorita
		Kategoria: R - Zr - Os

4. Vlak si vyberas napisanim jeho ID.
5. Vypisu sa nacestne stanice a stav obsadenia kolaji v tychto staniciach.
6. Podla schemy, ktora sa otvori po zatvoreni tohto suboru napises cislo kolaje, na ktoru chces vlak poslat.
7. Vlak sa sam vypravi zo stanice.

Po kazdom vyprazdneni tabulky sa zvysi level a za kazdy odbaveny vlak sa zvysi skore o 10.

Moznosti stratenia skore:
* Za vyber neexistujucej kolaje
* Za vyber obsadenej kolaje
* Za zly vyber kolaje v zst. Zilina smer Tekovany

