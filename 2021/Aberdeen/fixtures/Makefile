all: presentation.html pres_short.html

presentation.html: presentation.md
	cat parts/pres_start.html presentation.md parts/pres_stop.html > presentation.html

pres_short.html: pres_short.md
	cat parts/pres_start.html pres_short.md parts/pres_stop.html > pres_short.html

open: presentation.html
	open presentation.html

short: pres_short.html
	open pres_short.html

clean:
	rm -f presentation.html pres_short.html	
