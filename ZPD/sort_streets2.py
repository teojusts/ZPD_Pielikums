import json

# ATKARTOJOSAS S
#Augusta Deglava  (1-39 avoti) (39-74 Darzciems) (75-290 Pļavnieki)
#Brīvības (1-119 Centrs) (120-200 Brasa) (201-332 Teika) (333-429 Jugla)
#Biķernieku  (1-107 teika) (108-170 Mežciems)
#Daugavgrīvas  (1-50 Āgenskalns) (51-130 Dzirciems jeb dzegužkalns)
#Ganību dambis (1-30 Andrejsala) (31-90 Sarkandaugava)
#Jūrmalas  (1-15 Dzirciems) (16-190 Imanta)
#Kārļa Ulmaņa  (1-20 Torņakalns) (21-94 Pleskonade) (22-162 Zolitude)
#Kr. Valdemāra  (1-123 Centrs) (124-170 Brasa)
#Krišjāņa Barona  (1-95 Centrs) (96-150 Grīziņkalns)
#Lielvārdes  (1-75 Teika) (76-140 Purvciems)
#Lubānas  (1-51 Latgale (Maskavas forštate)) (52-200 Pļavnieki)
#Stabu  (1-50 Centrs) (51-210 Avoti)
#Vienības  (1-90 Ziepniekkalns) (91-200 Torņakalns)
#Aleksandra Čaka  (1-112 Centrs) (123-220 Grīziņkalns)
#Bruņinieku  (1-59 Centrs) (60-200 Avoti)
#Latgales  (1-230 Latgale (Maskavas forštate)) (231-427 Ķengarags) (428-455 Rumbula) (456-590 Dārziņi)
#Dzirciema  (1-59 Dzirciems) (60- 200 Iļģuciems)
#Dzirnavu  (1-110 Centrs) (111-200 Latgale (Maskavas forštate))
#Gustava Zemgala  (1-80 Teika) (80-200 Čiekurkalns)
#Matīsa  (1-35 Centrs) (36-200 Avoti)
#Nīcgales  (1-30 Purvciems) (31- 200 Dārzciems)
#Ģertrūdes  (1-47 Centrs) (48-220 Avoti)
#Lāčplēša  (1- 51 Centrs) (52-80 Avoti) (81- 150 Latgale (Maskavas forštate))

district_streets = {
#    'Atgāzene': [
#        'Graudu ', 'Vienības '
#    ],
    "Avoti": [ 'Avotu ', 'Augusta Deglava ', 'Matīsa ', 'Satekles ', 'Valmieras ', "Artilērijas ", "Bruņinieku ", "Lāčplēša", "Visvalža", "Visvalža",
    "Ernesta Birznieka-Upīša ", "Stabu ", "Vagonu ","Ģertrūdes ", "Kurbada", "Ādmiņu", "Mūrnieku", 
    "Zaķu", "Pļavas", "Lienes", "Krāsotāju", "Sparģeļu", "Vagonu", "Strenču", "Narvas", "Suntažu", "Rūjienas", 
    ],
    'Āgenskalns': [
        'Bāriņu ', 'Daugavgrīvas ', 'Kalnciema ', 'Mārupes ', 'Melnsila ', "Ernestīnes ", "Klīveru ", "Meža ",
        'Nometņu ', 'Raņķa dambis', 'Uzvaras bulvāris', "Eduarda Smiļģa ", "Kapseļu ", "Margrietas ", "Pilsoņu ", "Valguma "
    ],
# NEIZMANTOT    'Beberbeķi': [
#        'Beberbeķu ', 'Beberbeķu 5. līnija', 'Beberbeķu 9. līnija', 'Kārļa Ulmaņa ',
#        'Krotes '
#    ],
    'Berģi/Bukulti': [
        'Berģu ', 'Rožu ', 'Upesciema ', 'Jaunciema ', 'Kanāla ',
    ],
    'Bieriņi': [
        'Cēres ', 'Kantora ', 'Tēriņu ', "Mežotnes "
    ],
    'Bišumuiža/Katlakalns': [
        'Bauskas ', 'Ceraukstes ', 'Jāņa Čakstes ', 'Bukaišu ', 'Lejupes ',
    ],
    'Bolderāja': [
        'Gobas ', 'Lielā ', 'Lielupes ', 'Silikātu ', 'Stūrmaņu ', "Mežrozīšu ", 
    ],
   'Brasa': [
       'Brīvības ', 'Cēsu ', 'Kr. Valdemāra ', 'Miera ', 'Senču ', 'Zirņu ', "Hospitāļu ", "Invalīdu ", "Klijānu ", "Ēveles", "Jāņa Daliņa", "Vesetas",
       "Mēness ", "Kazarmu", "Ieroču", "Kareivju", "Lejas", "Upes", "Klusā", "Lāču iela", "Straumas", "Laktas", "Kaspara", "Etnas",  "Indrānu", "Silmaču"
    ],
    'Brekši': [
        'Nautrēnu '
    ],
#    'Bukulti': [
#        'Brīvības ', 'Jaunciema ', 'Kanāla '
#    ],
#    'Buļļi': [
#        'Dzintara ', 'Ilmeņa ', 'Rojas '
#    ],
   'Centrs': [
        'Brīvības ', 'Brīvības bulvāris', 'Krišjāņa Barona ', 'Kr. Valdemāra ', "Dzirnavu ", "Elizabetes ", "Jaņa Rozentāla laukums", "Skolas ", "Satekles", 
        "Pļavu", "Alfrēda Kalniņa", "Pērses", "Stabu", "Skolas", "Zaļā", "Antonijas", "Ganu", "Alberta", "Strēlnieku",
        'Lāčplēša ', 'Marijas ', 'Merķeļa ', 'Raiņa bulvāris', "Alberta ", "Baznīcas ", "Blaumaņa ", "Bruņinieku ", "Jeruzalemes ", "Tērbatas", "Akas", 
        "Radio", "Daines", "Martas", "Zaubes", "Annas", "Arhitektu", "Inžinieru", "Palīdzības", "Akas", "Šarlotes", "Maiznīcas",  
        "Kalpaka bulvāris", "Matīsa ", "Nikolaja Rēriha ", "Pērses ", "Stabu ", "Tērbatas ", "Zaļā ", "Ģertrūdes ", "Stacijas laukums", "Pērses", 
        "Sakaru "," Vilandes",  "Valkas", "Veru", "Hanzas", "Vidus", "Veru", "Mednieku", "Ganu", "Lenču", "Jura Alunāna", "Andreja Pumpura",
        "Tomsona", "Alojas", "Nītaures", "Aristida Briāna", "Zaubes", "Emiļaa Melngaiļa", 
   ],
    'Čiekurkalns': [
        'Čiekurkalna 1. līnija', 'Čiekurkalna 2. līnija', 'Gaujas ', 'Krustabaznīcas ', "Krustabaznīcas ", "Tēraudlietuves ",
        'Ķīšezera ', 'Viskaļu ', "Abulas ", "Džutas ", "Gustava Zemgala ", "Lizuma ", "Rusova ",
    ],
    'Daugavgrīva': [
        'Birzes ', 'Flotes ', 'Parādes ', 'Slimnīcas '
    ],
    'Dārzciems': [
        'Augusta Deglava ', 'Dārzciema ', 'Lubānas ', 'Nīcgales ',
        'Piedrujas ', 'Vestienas ', "Pildas ", "Zebiekstes ",
    ],
    'Dārziņi': [
        'Cidoniju ', 'Dārziņu ', 'Jāņogu ', 'Latgales ', 'Taisnā '
    ],
    'Dreiliņi': [
         'Ēvalda Valtera ',
        'Ulbrokas '
    ],
    'Dzirciems jeb dzegužkalns': [
        'Buļļu ', 'Daugavgrīvas ', 'Dzirciema ', "Dārza ", "Sēlpils ", "Usmas "
    ],
    'Grīziņkalns': [
        'Aleksandra Čaka ', 'Jāņa Asara ', 'Krišjāņa Barona ', 'Pērnavas ',
        'Tallinas ', "Sapieru ", "Zvaigžņu ",
    ],
    'Iļģuciems': [
        'Buļļu ', 'Dagmāras ', 'Daugavgrīvas ', 'Dzirciema ', 'Lidoņu ', "Riekstu ", "Skandu ", "Spilves "
    ],
    'Imanta': [
        'Anniņmuižas bulvāris', 'Bebru ', 'Dammes ', 'Jūrmalas ', 'Kleistu ', "Lazdu ",
        'Kurzemes prospekts', 'Slokas ', 'Zentenes ', "Imanta", "Imantas 15. līnija", "Imantas 18. līnija", "Imantas 8. līnija", "Čuguna "
    ],
    'Jaunciems': [
        'Jaunciema '
    ],
    'Jugla': [
        'Brīvības ', 'Juglas ', 'Murjāņu ', 'Malienas ', 'Kvēles ', 'Silciema ', "Braila ", "Juglas ", "Šmerļa ", "Brīvības "
    ],
#    'Katlakalns': [
#        'Bukaišu ', 'Lejupes '
#    ],
    'Kleisti': [
        'Kleistu ', 'Rātsupītes '
    ],
    'Kundziņsala': [
        'Kundziņsalas 1. šķērslīnija', 'Kundziņsalas 3. līnija', 'Kundziņsalas 6. šķērslīnija', 
    ],
    'Ķengarags': [
        'Aglonas ', 'Ikšķiles ', 'Ķengaraga ', 'Latgales ', 'Lokomotīves ', "Mazā Rencēnu ",
        'Prūšu ', 'Salaspils ', "Aglonas ", "Kaņiera "
    ],
    'Ķīpsala': [
        'Āzenes ', 'Balasta dambis', 'Kr. Valdemāra ', 'Ķīpsalas ', 'Matrožu ',
        'Ogļu ', 'Zvejnieku ', "Tīklu ",
    ],
    'Latgale (Maskavas forštate)': [
        'Emīlijas Benjamiņas ', 'Kalna ', 'Krasta ', 'Lastādijas ', 'Latgales ', "Daugavpils ", "Dzirnavu ", "Dzērvju ", "Firsa Sadovņikova ",
        'Ludzas ', 'Valērijas Seiles ', "Aiviekstes ", "Akadēmijas laukums", "Centrāltirgus ", "Elijas ",
        "Gaiziņa ", "Gogoļa ", "Grēdu ", "Kalna ", "Kojusalas ", "Krasta ", "Lomonosova ", "Maskavas ", "Mazā Krasta ", "Nēģu ", "Firsa Sadovņikova"
    ],
    'Mangaļsala': [
        'Albatrosu ', 'Mangaļsalas ', 'Stāvvadu ', 'Traleru ', 'Veiksmes '
    ],
    'Mežaparks': [
        'Ezermalas ',  'Kokneses prospekts', 'Meža prospekts', 'Varoņu ', "Cimzes ", "Sudrabu Edžus "
    ],
    'Mežciems': [
        'Biķernieku ', 'Sergeja Eizenšteina ', 'Hipokrāta ', 'Juglas ',  "Gaiļezera ", "Linezera "
    ],
#    'Mīlgrāvis': [
#        'Ezera ', 'Lēdurgas ', 'Mīlgrāvja '
#    ],
#  NEIZMANTOT  'Mūkupurvs': [
#        'Gramzdas ', 'Kārļa Ulmaņa ', 'Mūkupurva '
#    ],
    'Andrejsala': [
        'Eksporta ', 'Ganību dambis', 'Katrīnas dambis', 'Lugažu ', 'Pētersalas ', "Andrejostas", "Kaķasēkļa", "Mazā Vējzaķsala",
        "Pulkveža Brieža", "Mastu ", "Mihaila Tāla ", "Ausekļa", "Katrīnas", "Rūpniecības", "Alūksnes", "Vēžu", "Ūmeo", "Sermaliņu", "Lugažu", "Piena", "Mazā Piena", "Ilzenes",
    ],
#    'Pleskodāle': [
#        'Apuzes ', 'Jūrkalnes ', 'Kārļa Ulmaņa ', 'Krūzes ', 'Lielirbes ',
#        'Ventspils '
#    ],
    'Pļavnieki': [
        'Andreja Saharova ', 'Augusta Deglava ', 'Brāļu Kaudzīšu ', 'Lubānas ',
        'Salnas ', 'Ulbrokas ', "Dzeņu ", "Ilūkstes ", "Jasmuižas ", "Kupriču "
    ],
    'Purvciems': [
        'Augusta Deglava ', 'Braslas ', 'Dzelzavas ', 'Gunāra Astras ', 'Ieriķu ', "Varavīksnes ",
        'Lielvārdes ', 'Nīcgales ', 'Purvciema ', "Braslas ", "Induļa ", "Vaidavas ", "Ūnijas "
    ],
    'Rumbula': [
        'Krustpils ', 'Latgales ', 'Višķu '
    ],
#  NEIZMANTOT  'Salas': [
#        'Lucavsalas ', 'Zaķusalas krastmala'
#    ],
    'Sarkandaugava': [
        'Aptiekas ',  'Ganību dambis', 'Tilta ', 'Tvaika ', "Uriekstes ",
        'Viestura prospekts', "Ilzenes ", "Patversmes ", "Rankas ", "Sarkandaugavas ", "Sāremas iela"
    ],
    'Skanste': [
        'Duntes ', 'Ganību dambis', 'Grostonas ', 'Skanstes ', 'Sporta ', "Vesetas",
        'Vesetas ', "Hanzas ", "Mālpils", "Grostonas", "Roberta Hirša", "Gustava Kluča","Mihaila Tāla", "Martas Staņas", "Aleksandra Laimes", "Lapeņu", "Lapeņu 7", 
        "Vilhelma Ostvalda", "Jāņa Dikmaņa", "Arēnas", "Laktas", 
    ],
# NEIZMANTOT    'Spilve': [
#        'Daugavgrīvas ', 'Daugavgrīvas šoseja'
#    ],
# NEIZMANTOT    'Suži': [
#        'Jaunciema '
#    ],
    'Šampēteris/Pleskonade': [
        'Lielirbes ', 'Šampētera ', 'Volguntes ', 'Zasulauka ', 'Apuzes ', 'Jūrkalnes ', 'Kārļa Ulmaņa ', 'Krūzes ', 
        'Ventspils ', "Jaunmoku ", "Kalnciema "
    ],
    'Šķirotava': [
        'Granīta ', 'Katlakalna ', 'Krustpils ', 'Lubānas ', 'Rencēnu ', "Cesvaines ",
    ],
    'Teika': [
        'Biķernieku ', 'Brīvības ', "Brīvības ", 'Gustava Zemgala ', 'Lielvārdes ', "Ieriķu ", "Vairoga ",
        'Ropažu ', 'Tālivalža ', "Aizkraukles ", "Burtnieku ", "Raunas ", "Starta ", "Vidrižu "
    ],
    'Torņakalns': [
        'Bauskas ', 'Kārļa Ulmaņa ', 'Mūkusalas ', 'Vienības ', 'Torņakalna ', "Jelgavas ", "Satiksmes ",
         "Altonavas ", "Bieķensalas ", "Biešu ", "Dēļu ", "Ojāra Vācieša "
    ],
    'Trīsciems': [
        'Jaunciema '
    ],
    'Vecāķi': [
        'Mangaļu prospekts', 'Pludmales ', 'Vecāķu prospekts'
    ],
    'Vecdaugava': [
        'Atlantijas ', 'Vecāķu prospekts'
    ],
    'Vecmīlgrāvis/Mīlgrāvis': [
        'Augusta Dombrovska ', 'Emmas ', 'Kriemeņu ', 'Meldru ', 'Vecāķu prospekts', 'Ezera ', 'Lēdurgas ', 'Mīlgrāvja ', "Birztalu ", 
        "Gāles ",  "Meldru ", "Zivju ",
    ],
    'Vecrīga': [
        '11. novembra krastmala', 'janvāra ', 'Audēju ', 'Kalēju ', 'Kaļķu ', "Citadeles ", "Grēcinieku ", "Latviešu strēlnieku laukums", "Palasta ",
        'Kungu ', 'Smilšu ', 'Torņu ', 'Zigfrīda Annas Meierovica bulvāris', "Aspazijas bulvāris", "Kronvalda bulvāris", "Mazā Smilšu ",  "Noliktavas ",
        "Peldu ", "Pils ", "Republikas laukums", "Riharda Vāgnera ", "Skārņu ", "Smilšu ", "Vaļņu ", "Šķūņu "
    ],
    'Voleri': [
        'Krēmeru ', 'Voleru '
    ],
    'Zasulauks': [
        'Vīlipa ', "Kandavas "
    ],
    'Ziepniekkalns/Atgāzne': [
        'Garozes ', 'Graudu ', 'Valdeķu ', 'Ziepniekkalna ', 'Graudu ', 'Vienības ', "Bauskas ", "Beverīnas ", "Dižozolu ",
        "Mežkalna ", "Skaistkalnes "
    ],
    'Zolitūde': [
        'Anniņmuižas ', 'Gramzdas ', 'Jūrkalnes ', 'Kārļa Ulmaņa ',
        'Rostokas ', 'Zolitūdes ', "Lidosta", "Paula Lejiņa ", "Priedaines "
    ]
}

# Function to classify addresses into districts
def classify_addresses(addresses, district_streets):
    district_results = {district: [] for district in district_streets}

    street_intervals = {
        "Augusta Deglava": [(1, 39, "Avoti"), (40, 74, "Dārzciems"), (75, 290, "Pļavnieki")],
        "Brīvības": [(1, 119, "Centrs"), (120, 200, "Brasa"), (201, 332, "Teika"), (333, 429, "Jugla")],
        "Biķernieku": [(1, 107, "Teika"), (108, 170, "Mežciems")],
        "Daugavgrīvas": [(1, 50, "Āgenskalns"), (51, 130, "Dzirciems jeb dzegužkalns")],
        "Ganību dambis": [(1, 30, "Andrejsala"), (31, 90, "Sarkandaugava")],
        "Jūrmalas": [(1, 15, "Dzirciems"), (16, 190, "Imanta")],
        "Kārļa Ulmaņa": [(1, 20, "Torņakalns"), (21, 94, "Pleskonade"), (95, 162, "Zolitūde")],
        "Krišjāņa Valdemāra": [(1, 123, "Centrs"), (124, 170, "Brasa")],
        "Krišjāņa Barona": [(1, 95, "Centrs"), (96, 150, "Grīziņkalns")],
        "Lielvārdes": [(1, 75, "Teika"), (76, 140, "Purvciems")],
        "Lubānas": [(1, 51, "Latgale (Maskavas forštate)"), (52, 200, "Pļavnieki")],
        "Stabu": [(1, 50, "Centrs"), (51, 210, "Avoti")],
        "Vienības": [(1, 90, "Ziepniekkalns"), (91, 200, "Torņakalns")],
        "Aleksandra Čaka": [(1, 112, "Centrs"), (123, 220, "Grīziņkalns")],
        "Bruņinieku": [(1, 59, "Centrs"), (60, 200, "Avoti")],
        "Latgales": [(1, 230, "Latgale (Maskavas forštate)"), (231, 427, "Ķengarags"), (428, 455, "Rumbula"), (456, 590, "Dārziņi")],
        "Dzirciema": [(1, 59, "Dzirciems"), (60, 200, "Iļģuciems")],
        "Dzirnavu": [(1, 110, "Centrs"), (111, 200, "Latgale (Maskavas forštate)")],
        "Gustava Zemgala": [(1, 80, "Teika"), (81, 200, "Čiekurkalns")],
        "Matīsa": [(1, 35, "Centrs"), (36, 200, "Avoti")],
        "Nīcgales": [(1, 30, "Purvciems"), (31, 200, "Dārzciems")],
        "Ģertrūdes": [(1, 47, "Centrs"), (48, 220, "Avoti")],
        "Lāčplēša": [(1, 51, "Centrs"), (52, 80, "Avoti"), (81, 150, "Latgale (Maskavas forštate)")],
    }


    for entry in addresses:
        address = entry.get("location", "")
        wage = entry.get("wage", 0)

        # Extract street name and number from the address
        if ',' in address:
            street_part = address.split(',')[0]
        else:
            street_part = address

        street_name = street_part.rsplit(' ', 1)[0]
        try:
            street_number = int(street_part.rsplit(' ', 1)[1])
        except (ValueError, IndexError):
            street_number = None

        # Check for specific street intervals first
        if street_name in street_intervals and street_number is not None:
            for start, end, district in street_intervals[street_name]:
                if start <= street_number <= end:
                    district_results[district].append({"address": address, "value": wage})
                    break
        else:
            # Match street name to a district
            for district, streets in district_streets.items():
                if any(street_name in street for street in streets):
                    district_results[district].append({"address": address, "value": wage})
                    break

    return district_results

# Load the JSON file with addresses
with open('location_wage_data_riga_filtered.json', 'r', encoding='utf-8') as file:
    address_data = json.load(file)

# Classify the addresses using the classify_addresses function
classified_addresses = classify_addresses(address_data, district_streets)

# Prepare the data to be saved to a new JSON file
district_prices = {}

for district, data in classified_addresses.items():
    # Extract the prices for each district
    prices = [entry['value'] for entry in data]
    district_prices[district] = prices

# Save the results to a new JSON file
with open('classified_district_prices.json', 'w', encoding='utf-8') as output_file:
    json.dump(district_prices, output_file, ensure_ascii=False, indent=4)

print("Classified district prices have been saved to 'classified_district_prices.json'.")
