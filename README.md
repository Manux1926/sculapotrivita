# SculaPotrivită

Site: https://sculapotrivita.online — conținut în `site_sculapotrivita.py` (ghiduri, selector) și `site_sculapotrivita_p.py` (produse, comparator, portada), generat automat de GitHub Actions (build.py din Manux1926/dronaagricola).

`og-image.jpg` (1200×630, imagine pentru rețele sociale) și `logo.png` (256×256, logo pentru Google) se copiază automat în site la build. Fotografiile oficiale de presă ale produselor (dicționarul `PRESS` din build.py) se descarcă și se micșorează la fiecare build.

Verificare Profitshare: etichetele `PS_META` în `<head>` și fișierele `<cod>.html` (`PS_CODES` din build.py) în rădăcina site-ului.

Opțional, `site_<sid>_a.py` adaugă articole noi (`PAGES`), corecturi de produse (`PATCH`) și actualizări ale ghidurilor (câmpul `modified` pentru data actualizării).
