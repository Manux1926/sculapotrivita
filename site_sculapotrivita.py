from build import AFF_NOTE

JS = r"""
(function(){
function $(s,c){return (c||document).querySelector(s)}
var P={
 parkside:{n:'Parkside X20V (Lidl)',hobby:3,reno:1,pro:0,gard:2,cost:3,d:'Cea mai ieftină intrare. Bună pentru treburi ocazionale; gama și stocul depind de ofertele Lidl.'},
 einhell:{n:'Einhell Power X-Change 18V',hobby:3,reno:2,pro:0,gard:3,cost:3,d:'Gamă foarte largă pentru casă și grădină la prețuri mici; o baterie pentru zeci de scule.'},
 ryobi:{n:'Ryobi ONE+ 18V',hobby:3,reno:2,pro:0,gard:3,cost:2,d:'Platformă foarte largă și compatibilă de ani buni; bună pentru bricolaj și grădină.'},
 boschg:{n:'Bosch 18V (verde) / Power for All',hobby:3,reno:2,pro:0,gard:3,cost:2,d:'Linia pentru casă; aceleași baterii merg și la alte branduri din alianța Power for All (de ex. Gardena).'},
 makita:{n:'Makita LXT 18V',hobby:2,reno:3,pro:3,gard:3,cost:1,d:'Una dintre cele mai mari game de scule pe 18V, inclusiv grădină; calitate semi-profesională și profesională.'},
 dewalt:{n:'DeWalt XR 18V / FlexVolt',hobby:1,reno:3,pro:3,gard:1,cost:1,d:'Orientată pe construcții; FlexVolt pentru scule mari (fierăstraie, polizoare de 230 mm).'},
 milw:{n:'Milwaukee M18',hobby:1,reno:2,pro:3,gard:1,cost:0,d:'Preferată de instalatori și electricieni; scule specializate foarte bune, preț ridicat.'},
 boschp:{n:'Bosch Professional 18V (albastru)',hobby:1,reno:3,pro:3,gard:1,cost:1,d:'Linia profesională Bosch (alianța AMPShare); robustă, service bun în România.'}
};
var c=$('#calc');if(!c)return;
function run(){var u=$('#uz').value,b=+$('#bg').value,g=+$('#gd').value,sc=[];
 for(var k in P){var p=P[k];var s=p[u]*3+p.gard*g+p.cost*b;sc.push([s,k])}
 sc.sort(function(a,b){return b[0]-a[0]});
 var top=sc.slice(0,3).map(function(x,i){var p=P[x[1]];return '<div class="kpi'+(i===0?' main':'')+'"><span>'+(i===0?'Recomandarea 1':'Alternativa '+i)+'</span><b style="font-size:20px">'+p.n+'</b><span style="display:block;margin-top:6px;font-weight:500">'+p.d+'</span></div>'}).join('');
 $('#rTop').innerHTML=top;
 var tips=[];if(u==='pro')tips.push('Ia scule fără perii (brushless) și baterii de 5 Ah sau mai mari.');if(u==='hobby')tips.push('Un kit cu 2 baterii de 2–4 Ah și încărcător e suficient; cumpără apoi scule „fără acumulator” (body only).');if(g>=2)tips.push('Pentru grădină (trimmer, motocoasă, mașină de tuns) contează mult gama de scule de grădină din aceeași platformă.');
 $('#rTips').innerHTML=tips.map(function(t){return '<li>'+t+'</li>'}).join('');}
c.addEventListener('change',run);run();
})();
"""

TOOL = """<div class="tool"><form id="calc" onsubmit="return false"><h2>Ce platformă de acumulatori ți se potrivește?</h2>
<p class="note" style="margin-top:-6px">Bateriile nu sunt compatibile între branduri. Alegi o dată platforma, apoi cumperi ani de zile scule fără baterie, mult mai ieftine.</p>
<div class="grid3">
<div><label class="f" for="uz">Cum folosești sculele</label><select id="uz"><option value="hobby">Ocazional, prin casă</option><option value="reno" selected>Renovări și bricolaj serios</option><option value="pro">Profesional, zilnic</option></select></div>
<div><label class="f" for="bg">Cât contează prețul</label><select id="bg"><option value="3">Foarte mult</option><option value="2" selected>Contează</option><option value="0">Calitatea primează</option></select></div>
<div><label class="f" for="gd">Scule de grădină pe aceeași baterie</label><select id="gd"><option value="0">Nu mă interesează</option><option value="1">Poate, ceva</option><option value="3" selected>Da, trimmer, tuns, suflantă</option></select></div>
</div>
<div class="res"><div class="big" id="rTop"></div><ul id="rTips" style="margin-top:14px"></ul></div></form></div>"""

PLATF = """<div class="tw"><table class="t"><tr><th>Platformă</th><th>Nivel</th><th>Punct forte</th><th>De reținut</th></tr>
<tr><td>Parkside X20V</td><td>Hobby</td><td>Preț foarte mic</td><td>Disponibilitate doar în promoțiile Lidl</td></tr>
<tr><td>Einhell Power X-Change</td><td>Hobby–bricolaj</td><td>Gamă uriașă casă + grădină</td><td>Nu e pentru folosire zilnică pe șantier</td></tr>
<tr><td>Ryobi ONE+</td><td>Hobby–bricolaj</td><td>Compatibilitate de lungă durată</td><td>Mai puțin prezent în magazinele din România</td></tr>
<tr><td>Bosch 18V verde (Power for All)</td><td>Hobby–bricolaj</td><td>Baterii comune cu alte branduri din alianță</td><td>Nu e compatibil cu Bosch Professional (albastru)</td></tr>
<tr><td>Makita LXT 18V</td><td>Bricolaj serios–profesional</td><td>Gamă foarte mare, inclusiv grădină</td><td>Mai scump</td></tr>
<tr><td>DeWalt XR / FlexVolt</td><td>Profesional</td><td>Scule puternice pentru construcții</td><td>Grădină limitată</td></tr>
<tr><td>Milwaukee M18</td><td>Profesional</td><td>Scule de instalații și electrice</td><td>Cel mai scump</td></tr>
<tr><td>Bosch Professional 18V (AMPShare)</td><td>Profesional</td><td>Robustețe, service</td><td>Baterii diferite de linia verde</td></tr></table></div>"""

INDEX_BODY = TOOL + """
<section class="sec"><h2>Platformele de 18 V pe scurt</h2>""" + PLATF + """
<p>Comparația completă, cu criteriile de alegere, în <a href="/platforme-acumulatori-18v.html">ghidul platformelor</a>.</p></section>
<section class="sec"><h2>Ghiduri</h2><div class="cards">
<a class="c" href="/platforme-acumulatori-18v.html"><span class="tag">Comparație</span><b>Makita, DeWalt, Bosch, Einhell sau Parkside?</b><span>Cum alegi platforma de 18 V pe termen lung.</span></a>
<a class="c" href="/bormasina-autofiletanta-sau-rotopercutor.html"><span class="tag">Ghid</span><b>Bormașină, autofiletantă sau rotopercutor?</b><span>Ce sculă pentru ce lucrare.</span></a>
<a class="c" href="/brushless-ah-volti-explicate.html"><span class="tag">Explicat</span><b>Brushless, Ah și volți</b><span>Ce înseamnă cifrele și când merită.</span></a></div></section>"""

FAQ = [
    ('Bateriile Makita merg pe scule DeWalt?', 'Nu oficial. Fiecare producător are propriul sistem de baterii. Adaptoarele neoficiale există, dar anulează de obicei garanția și pot fi riscante.'),
    ('Bateriile Bosch verzi merg pe Bosch Professional?', 'Nu. Linia verde (pentru casă) și linia albastră (profesională) au sisteme de baterii diferite, fiecare în propria alianță de branduri compatibile.'),
    ('Merită să cumpăr scule fără acumulator?', 'Da, după ce ai 2 baterii și un încărcător. Variantele „body only” costă mult mai puțin, iar bateriile se folosesc la toate sculele platformei.'),
]

ART_PLAT = """<p>Când cumperi prima sculă cu acumulator, de fapt alegi o platformă pentru următorii 10 ani. Bateriile și încărcătorul sunt partea scumpă, iar ele funcționează doar cu sculele aceluiași sistem.</p>
<h2>Cele mai răspândite platforme în România</h2>""" + PLATF + """
<h2>Criteriile care contează</h2><ol><li><strong>Gama de scule:</strong> verifică dacă platforma are toate sculele pe care le vei vrea peste câțiva ani (inclusiv de grădină).</li><li><strong>Disponibilitatea în România:</strong> service, piese și baterii de schimb în magazinele de lângă tine.</li><li><strong>Prețul bateriilor:</strong> o baterie de schimb poate costa cât o sculă de bază.</li><li><strong>Ergonomia:</strong> ține scula în mână înainte de cumpărare, dacă poți.</li></ol>
<h2>Alianțele de baterii</h2><p>Unele branduri au format alianțe în care bateriile sunt compatibile între producători: de exemplu, linia verde Bosch face parte din alianța Power for All, iar linia Bosch Professional din alianța AMPShare. Avantajul: mai multe scule pe aceeași baterie, de la producători diferiți.</p>
<h2>Recomandarea pe profil</h2><ul><li><strong>Casa și grădina, buget mic:</strong> Einhell Power X-Change sau Parkside.</li><li><strong>Bricolaj serios plus grădină:</strong> Makita LXT.</li><li><strong>Construcții:</strong> DeWalt sau Bosch Professional.</li><li><strong>Instalații și electrice:</strong> Milwaukee M18.</li></ul>
<div class="box info">Nu ești sigur? Răspunde la trei întrebări în <a href="/">selectorul de platformă</a>.</div>""" + AFF_NOTE

ART_BORM = """<p>Cele trei scule arată asemănător, dar fac lucruri diferite. Alegerea greșită înseamnă fie o sculă care nu face față betonului, fie una prea grea pentru montat mobilă.</p>
<h2>Mașina de înșurubat (autofiletanta)</h2><p>Are mandrină și ambreiaj reglabil. Perfectă pentru șuruburi și găuri în lemn, metal subțire sau gips-carton. Ușoară, se folosește cu o mână. <strong>Pentru:</strong> mobilă, rafturi, montaj.</p>
<h2>Bormașina cu percuție</h2><p>Aceeași sculă, cu funcție de percuție pentru găuri în cărămidă. În beton armat se descurcă greu. <strong>Pentru:</strong> diblu în cărămidă, BCA, găuri ocazionale în perete.</p>
<h2>Ciocanul rotopercutor (SDS-plus)</h2><p>Lovește cu un mecanism pneumatic, nu cu clicheți. Face găuri în beton fără efort și poate dăltui. <strong>Pentru:</strong> beton, renovări, montat obiecte grele în pereți de beton.</p>
<h2>Și mașina de înșurubat cu impact</h2><p>Strânge șuruburi lungi și piulițe cu forță mare, fără să-ți răsucească încheietura. Nu e pentru găurit precis. <strong>Pentru:</strong> construcții din lemn, terase, șuruburi lungi.</p>
<h2>Ce cumperi primul</h2><ul><li>Apartament nou, mobilă: bormașină-înșurubător cu percuție.</li><li>Bloc cu pereți din beton: adaugă un rotopercutor SDS-plus.</li><li>Casă, terasă, lemn: înșurubător cu impact.</li></ul>""" + AFF_NOTE

ART_TECH = """<p>Cifrele de pe cutie spun multe, dacă știi să le citești.</p>
<h2>Volți (V)</h2><p>Arată clasa platformei: 12 V pentru scule compacte, 18 V (sau 20 V „max”, aceeași clasă) pentru majoritatea sculelor, 36 V sau 54 V pentru scule mari. Între 18 V și 20 V max nu e diferență reală; e doar mod de marketing.</p>
<h2>Amperi-oră (Ah)</h2><p>Arată cât ține bateria. Energia în Wh = volți × Ah: o baterie de 18 V și 5 Ah are 90 Wh. Bateriile de 2 Ah sunt ușoare, bune pentru înșurubat; cele de 5 Ah sau mai mari sunt pentru polizoare, fierăstraie și scule de grădină.</p>
<h2>Motor fără perii (brushless)</h2><p>Motoarele brushless au randament mai bun, deci mai multă autonomie pe aceeași baterie, mai multă putere și uzură mai mică. La sculele folosite des, merită diferența de preț. Pentru o bormașină folosită de câteva ori pe an, un motor cu perii e suficient.</p>
<h2>Cuplul (Nm)</h2><p>Forța de strângere. 30–50 Nm ajung pentru mobilă; 60 Nm sau mai mult pentru șuruburi lungi în lemn și găurit cu burghie mari.</p>
<h2>Încărcătorul</h2><p>Încărcătoarele rapide încarcă o baterie de 5 Ah în mai puțin de o oră. Pentru lucru continuu, ia două baterii și un încărcător rapid.</p>"""

SITE = {
    'name': 'SculaPotrivită', 'domain': 'sculapotrivita.online',
    'c1': '#2b2d42', 'c2': '#4f5d75', 'accent': '#ef8354',
    'mark': '<rect x="12" y="20" width="30" height="14" rx="4" fill="#fff"/><rect x="42" y="24" width="10" height="6" rx="2" fill="#ef8354"/><rect x="20" y="34" width="10" height="18" rx="3" fill="#fff"/><rect x="18" y="46" width="14" height="8" rx="2" fill="#ef8354"/>',
    'tagline': 'Ghiduri independente pentru scule cu acumulator: platforme de baterii, bormașini și scule de grădină.',
    'badges': ['Selector de platformă', 'Fără reclame mascate', 'Actualizat 2026'],
    'nav': [('/', 'Selector'), ('/platforme-acumulatori-18v.html', 'Platforme 18 V'), ('/bormasina-autofiletanta-sau-rotopercutor.html', 'Ce sculă?'), ('/ghiduri.html', 'Ghiduri')],
    'main_tool': 'Selector platformă de acumulatori',
    'side_title': 'Ce platformă alegi?', 'side_text': 'Răspunde la 3 întrebări și vezi recomandarea.',
    'about': '<p>SculaPotrivită este un site independent pentru cei care își cumpără scule cu acumulator: explicăm diferențele dintre platforme, scule și specificații, ca să cumperi o dată și bine.</p><p>Unele linkuri către magazine pot fi de afiliere și sunt marcate.</p>',
    'js': JS,
    'pages': [
        {'slug': 'index', 'title': 'Scule cu acumulator: ce platformă de baterii alegi?', 'kind': 'tool', 'short': 'Selector platformă', 'appcat': 'LifestyleApplication',
         'desc': 'Makita, DeWalt, Bosch, Einhell, Parkside sau Milwaukee? Află ce platformă de acumulatori de 18 V ți se potrivește după cum folosești sculele și buget.',
         'h1': 'Ce platformă de acumulatori să alegi?', 'toolname': 'Selector platformă acumulatori',
         'lead': 'Bateriile nu sunt compatibile între branduri, așa că prima alegere contează pe 10 ani. Trei întrebări și primești recomandarea.', 'body': INDEX_BODY, 'faq': FAQ},
        {'slug': 'platforme-acumulatori-18v', 'title': 'Acumulatori 18V: Makita vs DeWalt vs Bosch vs Einhell', 'kind': 'article', 'short': 'Platformele de 18 V',
         'desc': 'Comparația platformelor de acumulatori 18 V disponibile în România: pentru cine e fiecare, punctele forte, alianțele de baterii și recomandarea pe profil.',
         'h1': 'Platformele de acumulatori 18 V, comparate', 'lead': 'Makita, DeWalt, Bosch, Milwaukee, Einhell, Ryobi și Parkside: ce alegi pentru următorii 10 ani.', 'body': ART_PLAT},
        {'slug': 'bormasina-autofiletanta-sau-rotopercutor', 'title': 'Bormașină, autofiletantă sau rotopercutor: ce alegi', 'kind': 'article', 'short': 'Bormașină sau rotopercutor?',
         'desc': 'Diferențele dintre mașina de înșurubat, bormașina cu percuție, ciocanul rotopercutor SDS-plus și înșurubătorul cu impact, cu recomandări pe tip de locuință.',
         'h1': 'Bormașină, autofiletantă sau rotopercutor?', 'lead': 'Ce sculă pentru ce lucrare și ce cumperi prima dată.', 'body': ART_BORM},
        {'slug': 'brushless-ah-volti-explicate', 'title': 'Brushless, Ah și volți la sculele cu acumulator', 'kind': 'article', 'short': 'Brushless, Ah, volți',
         'desc': 'Ce înseamnă volții, amperii-oră, cuplul și motorul brushless la sculele cu acumulator și când merită să plătești în plus.',
         'h1': 'Brushless, Ah și volți, explicate simplu', 'lead': 'Cum citești specificațiile ca să nu plătești pentru ce nu îți trebuie.', 'body': ART_TECH},
    ]
}
