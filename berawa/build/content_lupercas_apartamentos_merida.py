# Contenido de la demo Lupercas Apartamentos Turísticos (Mérida) (es/en/fr/de). Hechos de lupercasapartamentosturisticos.es leidos el 02/11/2026 (ver berawa/sources.json). Sin precios, sin valoraciones ni reseñas; sin plantas de cada apartamento (la web se contradice) salvo Anna (planta baja accesible, igual en sus dos paginas).
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran los apartamentos reales.','en':' Images are illustrations and do not show the actual apartments.','fr':' Les images sont des illustrations et ne montrent pas les appartements réels.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Apartments.'}
H={'es':['Apartamentos para una o dos personas','Apartamentos para dos a cuatro personas'],'en':['Apartments for one or two guests','Apartments for two to four guests'],'fr':['Appartements pour une ou deux personnes','Appartements pour deux à quatre personnes'],'de':['Apartments für eine oder zwei Personen','Apartments für zwei bis vier Personen']}
RD={
'es':['Minerva, con cama de matrimonio de 150, y Diana, con dos camas individuales. Salón-cocina, baño privado con ducha y cafetera Nespresso.','Anna, Felicitas y Juno, con sofá o sofá-cama. Anna está en planta baja accesible y tiene un patio interior de uso exclusivo.'],
'en':['Minerva, with a 150 double bed, and Diana, with two single beds. Living room with kitchen, private bathroom with shower and Nespresso machine.','Anna, Felicitas and Juno, with sofa or sofa bed. Anna is on an accessible ground floor and has a private inner patio.'],
'fr':['Minerva, avec un lit double de 150, et Diana, avec deux lits simples. Salon-cuisine, salle de bains privée avec douche et machine Nespresso.','Anna, Felicitas et Juno, avec canapé ou canapé-lit. Anna est au rez-de-chaussée accessible et dispose d’un patio intérieur privatif.'],
'de':['Minerva mit 150er Doppelbett und Diana mit zwei Einzelbetten. Wohnküche, eigenes Bad mit Dusche und Nespresso-Maschine.','Anna, Felicitas und Juno mit Sofa oder Schlafsofa. Anna liegt im barrierefreien Erdgeschoss und hat einen eigenen Innenhof.']}
ART={
'hero':('columns',7411,['#1d1612','#b0704a','#efd9bf','#6b4a36','#47322a','#261b16']),
'intro':('arches',7412,['#f4eee7','#fbf7f1','#9a5a3c','#66402c','#2e1f18']),
'r1':('arches',7421,['#f0e8df','#cf9a74','#9a5a3c','#66402c','#2e1f18']),
'r2':('columns',7422,['#1d1612','#c08058','#f0dcc4','#74503b','#4d362b','#2a1e18']),
'g1':('hills',7431,['#efe6da','#f2e2cc','#cf9a74','#a2876a','#76604c','#4c3e32']),
'g2':('arches',7432,['#1d1612','#b0704a','#efd9bf','#6b4a36','#47322a','#261b16']),
'g3':('skyline',7433,['#f2ebe3','#faf5ee','#a8653f','#6b4a36','#2e1f18']),
'g4':('waves',7434,['#1d1612','#c08058','#f0dcc4','#74503b','#4d362b','#2a1e18'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Lupercas · Apartamentos turísticos en Mérida',see_rooms='Ver los apartamentos',hero_k='Mérida · Rambla Mártir Santa Eulalia, 53',hero_t='Vuestro refugio en el corazón de Mérida',hero_s='Siete apartamentos turísticos inspirados en la leyenda de la loba de Roma.',
 intro_t='Un hogar con garra en Mérida',intro_p1='Lupercas es un edificio de 7 apartamentos con decoración elegante y acogedora, que mezcla lo restaurado y lo moderno. Cada apartamento lleva el nombre de una diosa.',
 intro_p2='Todos tienen balcón o ventanas al exterior y baño privado. Hay una zona de estar común y una cocina grande y bien equipada.',
 stats=['7 apartamentos','En pleno centro','Cocina común equipada','Aerotermia y placas solares'],nav_rooms='Apartamentos',rooms_t='Los apartamentos',rooms_s='Apartamentos diáfanos con salón-cocina, ropa de cama, toallas, TV y baño privado con ducha.',
 svcs=['Salón-cocina en cada apartamento','Cafetera Nespresso','Ropa de cama y toallas','Zona de estar común','Cocina común grande','Apartamento accesible en planta baja'],
 loc_p='Rambla Mártir Santa Eulalia, 53 · 06800 Mérida (Badajoz). Teléfonos: 681 19 35 87 y 689 71 30 34. Correo: info@lupercasapartamentosturisticos.es.',
 chips=['¿Qué apartamentos tenéis?','¿Hay cocina?','¿Es accesible?','¿Cómo reservo?']),
'en':dict(title='Lupercas · Tourist apartments in Mérida',see_rooms='See the apartments',hero_k='Mérida · Rambla Mártir Santa Eulalia, 53',hero_t='Your retreat in the heart of Mérida',hero_s='Seven tourist apartments inspired by the legend of the she-wolf of Rome.',
 intro_t='A home with character in Mérida',intro_p1='Lupercas is a building of 7 apartments with elegant, welcoming decor that mixes the restored and the modern. Each apartment is named after a goddess.',
 intro_p2='All have a balcony or windows to the outside and a private bathroom. There is a shared lounge and a large, well-equipped kitchen.',
 stats=['7 apartments','Right in the centre','Equipped shared kitchen','Aerothermal and solar panels'],nav_rooms='Apartments',rooms_t='The apartments',rooms_s='Open-plan apartments with living room and kitchen, bed linen, towels, TV and private bathroom with shower.',
 svcs=['Living room with kitchen in each apartment','Nespresso machine','Bed linen and towels','Shared lounge','Large shared kitchen','Accessible ground-floor apartment'],
 loc_p='Rambla Mártir Santa Eulalia, 53 · 06800 Mérida (Badajoz). Phones: +34 681 19 35 87 and +34 689 71 30 34. Email: info@lupercasapartamentosturisticos.es.',
 chips=['Which apartments do you have?','Is there a kitchen?','Is it accessible?','How do I book?']),
'fr':dict(title='Lupercas · Appartements touristiques à Mérida',see_rooms='Voir les appartements',hero_k='Mérida · Rambla Mártir Santa Eulalia, 53',hero_t='Votre refuge au cœur de Mérida',hero_s='Sept appartements touristiques inspirés de la légende de la louve de Rome.',
 intro_t='Un foyer de caractère à Mérida',intro_p1='Lupercas est un immeuble de 7 appartements à la décoration élégante et chaleureuse, entre restauré et moderne. Chaque appartement porte le nom d’une déesse.',
 intro_p2='Tous ont un balcon ou des fenêtres sur l’extérieur et une salle de bains privée. Il y a un salon commun et une grande cuisine bien équipée.',
 stats=['7 appartements','En plein centre','Cuisine commune équipée','Aérothermie et panneaux solaires'],nav_rooms='Appartements',rooms_t='Les appartements',rooms_s='Appartements ouverts avec salon-cuisine, linge de lit, serviettes, TV et salle de bains privée avec douche.',
 svcs=['Salon-cuisine dans chaque appartement','Machine Nespresso','Linge de lit et serviettes','Salon commun','Grande cuisine commune','Appartement accessible au rez-de-chaussée'],
 loc_p='Rambla Mártir Santa Eulalia, 53 · 06800 Mérida (Badajoz). Téléphones : +34 681 19 35 87 et +34 689 71 30 34. E-mail : info@lupercasapartamentosturisticos.es.',
 chips=['Quels appartements avez-vous ?','Y a-t-il une cuisine ?','Est-ce accessible ?','Comment réserver ?']),
'de':dict(title='Lupercas · Ferienapartments in Mérida',see_rooms='Apartments ansehen',hero_k='Mérida · Rambla Mártir Santa Eulalia, 53',hero_t='Ihr Rückzugsort im Herzen von Mérida',hero_s='Sieben Ferienapartments, inspiriert von der Legende der Wölfin Roms.',
 intro_t='Ein Zuhause mit Charakter in Mérida',intro_p1='Lupercas ist ein Haus mit 7 Apartments, elegant und gemütlich eingerichtet, zwischen Restauriertem und Modernem. Jedes Apartment trägt den Namen einer Göttin.',
 intro_p2='Alle haben Balkon oder Fenster nach außen und ein eigenes Bad. Es gibt einen gemeinsamen Aufenthaltsbereich und eine große, gut ausgestattete Küche.',
 stats=['7 Apartments','Mitten im Zentrum','Ausgestattete Gemeinschaftsküche','Aerothermie und Solarmodule'],nav_rooms='Apartments',rooms_t='Die Apartments',rooms_s='Offene Apartments mit Wohnküche, Bettwäsche, Handtüchern, TV und eigenem Bad mit Dusche.',
 svcs=['Wohnküche in jedem Apartment','Nespresso-Maschine','Bettwäsche und Handtücher','Gemeinsamer Aufenthaltsbereich','Große Gemeinschaftsküche','Barrierefreies Apartment im Erdgeschoss'],
 loc_p='Rambla Mártir Santa Eulalia, 53 · 06800 Mérida (Badajoz). Telefon: +34 681 19 35 87 und +34 689 71 30 34. E-Mail: info@lupercasapartamentosturisticos.es.',
 chips=['Welche Apartments gibt es?','Gibt es eine Küche?','Ist es barrierefrei?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
BOOK=dict(mode='mail',email='info@lupercasapartamentosturisticos.es')
D=dict(name='Lupercas Apartamentos',ac='#2b1f19',ac2='#9a5a3c',ac2_a11y='#7a4529',book=BOOK,around=[],foot=FOOT,
 address='Rambla Mártir Santa Eulalia, 53 · 06800 Mérida (Badajoz)',phones=['+34 681 19 35 87','+34 689 71 30 34'],emails=['info@lupercasapartamentosturisticos.es'],maps='Lupercas Apartamentos Turísticos, Rambla Mártir Santa Eulalia 53, 06800 Mérida',t=T)
META=dict(repo='demo-lupercas-apartamentos-merida',name='Lupercas Apartamentos Turísticos',legal_name='MSRUIZ 2021 SL, CIF B67628388 (aviso legal de su web)',registry_ids=['B67628388'],
 url='https://www.lupercasapartamentosturisticos.es/',domain='lupercasapartamentosturisticos.es',municipality='Mérida',province='Badajoz',sector='apartamentos turisticos en el centro de Merida',
 read_at='2026-11-02T07:12:00+01:00',created_at='2026-11-02T07:11:00+01:00',built_at='2026-11-02T07:25:00+01:00',audit_date='2026-11-02T07:11:00+01:00',
 rating=dict(value=4.9,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Lupercas+Apartamentos+Tur%C3%ADsticos/@38.9200288,-6.3419107,17z'),
 book=dict(mode='mail',url='mailto:info@lupercasapartamentosturisticos.es',note='sin motor de reservas verificable: el menu «Reservas» de su web lleva a una pagina vacia (/lupercas-apartamentos-turisticos-merid/) y su pagina de contacto da telefonos y correo. Los botones Reservar abren un correo a info@lupercasapartamentosturisticos.es (correo de su pagina de contacto) y los telefonos reales 681 19 35 87 y 689 71 30 34 van en tel:.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué apartamentos tenéis?','K01'),('¿Para cuántas personas son?','K02'),('¿Hay cocina?','K03'),('¿Es accesible?','K04'),('¿Tienen patio o balcón?','K05'),('¿Dónde estáis?','K06'),('¿Cómo reservo?','K07'),('¿Podéis confirmarme disponibilidad para mañana?','K07'),('¿Qué festivales hay en Mérida?','K08'),('¿Cuál es vuestro teléfono?','K09'),('¿Tienen aire acondicionado?','K10'),('¿Se puede fumar?','K11'),('¿Cuánto cuesta la noche?',None),('¿Hay parking?',None)],
'en':[('Which apartments do you have?','K01'),('How many people can stay?','K02'),('Is there a kitchen?','K03'),('Is it accessible?','K04'),('Do they have a patio or balcony?','K05'),('Where are you?','K06'),('How do I book?','K07'),('Can you confirm availability for tomorrow?','K07'),('Which festivals are there in Mérida?','K08'),('What is your phone number?','K09'),('Is there air conditioning?','K10'),('Can I smoke?','K11'),('How much is a night?',None),('Is there parking?',None)],
'fr':[('Quels appartements avez-vous ?','K01'),('Pour combien de personnes ?','K02'),('Y a-t-il une cuisine ?','K03'),('Est-ce accessible ?','K04'),('Y a-t-il un patio ou un balcon ?','K05'),('Où êtes-vous ?','K06'),('Comment réserver ?','K07'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K07'),('Quels festivals y a-t-il à Mérida ?','K08'),('Quel est votre numéro de téléphone ?','K09'),('Y a-t-il la climatisation ?','K10'),('Peut-on fumer ?','K11'),('Combien coûte la nuit ?',None),('Y a-t-il un parking ?',None)],
'de':[('Welche Apartments gibt es?','K01'),('Für wie viele Personen?','K02'),('Gibt es eine Küche?','K03'),('Ist es barrierefrei?','K04'),('Gibt es einen Innenhof oder Balkon?','K05'),('Wo liegt das Haus?','K06'),('Wie kann ich buchen?','K07'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K07'),('Welche Festivals gibt es in Mérida?','K08'),('Wie ist Ihre Telefonnummer?','K09'),('Gibt es eine Klimaanlage?','K10'),('Darf man rauchen?','K11'),('Was kostet eine Nacht?',None),('Gibt es Parkplätze?',None)]}
