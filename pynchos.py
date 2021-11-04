import googlemaps
from html import escape
from enum import Enum
from secret import GMAPS_API_KEY


class Pincho(Enum):
    SALAD = 1
    SWEET = 2


NATIONAL_PINCHOS = [
    [
        "Andalucía", "Cádiz", "Juan Antonio Pérez Vital", "LA LONJA", "Red Hot Chili Peppers", "Belmondo", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/andalucia_la-lonja.jpg", Pincho.SALAD,
    ],
    [
        "Andalucía", "Málaga", "Daniel García Peinado", "HOTEL EL PILAR ANDALUCÍA", "El mundo en mis manos", "Ole con Ole", "https://www.info.valladolid.es/blog/wp-content/uploads/2021/10/andalucia_el-mundo-esta-en-mis-manos.jpg", Pincho.SALAD,
    ],
    [
        "Andalucía", "Sevilla", "Loli Rincón Diéguez", "MANOLO MAYO", "Taco esencias del Guadalquivir", "Herbe", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/andalucia_manolo-mayo.jpg", Pincho.SALAD,
    ],
    [
        "Aragón", "Huesca", "Ramon Jesus Lapuyade Burro", "RESTAURANTE EL PORTAL", "Descendiendo el Cinca Compi(L`Ainsa-Alcolea-Belver)", "Puerto Chico", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/aragon-_-el-portal.jpg", Pincho.SALAD,
    ],
    [
        "Aragón", "Zaragoza", "Raul Pobo Rabadan", "FRIDA", "Vermut de domingo", "Utopia", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/aragon_frida.jpg", Pincho.SWEET,
    ],
    [
        "Aragón", "Zaragoza", "JULIA MERCADO TORON", "ALBERGUE MORATA DE JALON", "La Catrina Aragonesa", "Chester British", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/aragon_albergue-morata.jpg", Pincho.SALAD,
    ],
    [
        "Asturias", "Asturias", "Daniela Vázquez Monge", "BAZAAR GASTRO TZ", "Kahatsa’", "Lunatico", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/asturias_bazaar.jpg", Pincho.SALAD,
    ],
    [
        "Asturias", "Asturias", "Mario Fernández Argüelles", "TC28 BEBER Y COMER", "El mundo es un buñuelo", "Las Cabañas", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/asturias_tc28.jpg", Pincho.SALAD,
    ],
    [
        "Baleares", "Ibiza", "Aingeru Etxebarria Abascal", "CAN TERRA IBIZA", "Don Churra", "Don Bacalao", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/can-terra.jpg", Pincho.SWEET,
    ],
    [
        "Baleares", "Mallorca", "Igor Rodriguez Sanz", "RST EL BANDARRA", "Xuxo de Porc Amb  Anfós", "Suite 22", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/baleares_el-bandarra.jpg", Pincho.SALAD,
    ],
    [
        "Baleares", "Mallorca", "José Miguel Martínez Pilar", "RESTAURANTE BALEARIC. CAP VERMELL GRAN HOTEL", "Bellota ibérica de jamón", "Caroba", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/balerares_balearic-can-vermell.jpg", Pincho.SALAD,
    ],
    [
        "Baleares", "Mallorca", "Andrés Moreno Castellano", "SA PUNTA", "El capricho del Demonio", "La Criolla", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/baleares_sa-terra.jpg", Pincho.SALAD,
    ],
    [
        "Baleares", "Menorca", "Juan Carlos García Carrera", "THE TAPAS GASTROBAR", "Metamorfosis", "Talavera", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/baleares_the-tapas.jpg", Pincho.SALAD,
    ],
    [
        "Canarias", "Las Palmas", "David Espinel Armas", "LA MARQUESINA", "Explosión Volcánica", "Los Guajes", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/canarias_the-marquesina.jpg", Pincho.SALAD,
    ],
    [
        "Cantabria", "Cantabria", "Rubén Abascal Sainz", "RESTAURANTE IBIDEM", "La hora del café", "Moka", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/cantabria_the-ibidem.jpg", Pincho.SWEET,
    ],
    [
        "Castilla y León", "Burgos", "Isaac Montoya Carretero", "PAQUITA MARIVI", "Ceviche de lubina y sopa de tomate verde", "Zvumo", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/cyl-paquita-marivi.jpg", Pincho.SALAD,
    ],
    [
        "Castilla y León", "Valladolid", "Alejandro San José", "HABANERO TAQUERIA", "Salbut Criollo", "Habanero Taquería", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/cyl-habanero-taquieria.jpg", Pincho.SALAD,
    ],
    [
        "Castilla y León", "Valladolid", "Juan Carlos Jiménez Pradas", "VERDE OLIVA", "Perenne", "Verde Oliva", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/cyl-verde-oliva.jpg", Pincho.SALAD,
    ],
    [
        "Castilla y León", "Valladolid", "Jon Melgosa San José", "LA TETA Y LA LUNA", "Marbacoa", "La teta y la luna", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/cyl-la-teta-y-la-luna.jpg", Pincho.SALAD,
    ],
    [
        "Castilla y León", "Valladolid", "Ana María García Blanco", "LA PARRILLA DE SAN LORENZO", "Churro de lechazo", "LA PARRILLA DE SAN LORENZO", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/cyl-Parrilla-de-San-Lorenzo.jpg", Pincho.SALAD,
    ],
    [
        "Castilla y León", "Salamanca", "Helio Flores Gutiérrez", "LOS ÁLAMOS", "Al centro de la diana", "Don Bacalao", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/cyl-los-alamos.jpg", Pincho.SALAD,
    ],
    [
        "Castilla-La Mancha", "Albacete", "Mauro Javier Franco", "ALALIMON", "Volcano", "Alquimia", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/CLamancha-_-Alalimon.jpg", Pincho.SALAD,
    ],
    [
        "Cataluña", "Barcelona", "Sergio Martínez Montero", "EL JARDÍ DE CAN FIGUERES", "Una tapa de libro", "5 gustos", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/catalu%C3%B1a_el-jardin-de-can-figuers.jpg", Pincho.SALAD,
    ],
    [
        "Cataluña", "Barcelona", "Gerard Trilles Chillida", "ADOBO", "Empanadilla de atún adobado", "Gastrobar Sabores", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/catalu%C3%B1a-_-adobo.jpg", Pincho.SALAD,
    ],
    [
        "Cataluña", "Barcelona", "JUAN CARLOS REYES MORENO", "RESTAURANTE ABAC", "Apología al Cochino Ibérico", "Restaurante Angela", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/catalu%C3%B1a-_-abad.jpg", Pincho.SALAD,
    ],
    [
        "Cataluña", "Barcelona", "Antonia Massanet Perelló", "PASTELERÍA ESCRIBÁ", "Pansobrassada", "Atypikal", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/catalu%C3%B1a_pasteleria-escriba.jpg", Pincho.SALAD,
    ],
    [
        "Extremadura", "Badajoz", "Rocío Maya Díaz", "LA TABERNA DE NOA GASTROBAR", "Dona Carrillera", "Suite 22", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/extremadura-taberna-de-noa.jpg", Pincho.SALAD,
    ],
    [
        "Extremadura", "Cáceres", "Alberto Montes Pereira", "ATRIO", "Hasta el filo de la navaja", "Los Zagales", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/extremadura-atrio.jpg", Pincho.SALAD,
    ],
    [
        "Galicia", "La Coruña", "Sheila Barbeito Aradas", "ROOTS CORUÑA", "Falso saam de panceta y mejillón", "Ocho Apellidos Catellanos", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/galicia-roots.jpg", Pincho.SALAD,
    ],
    [
        "Galicia", "La Coruña", "Miguel Salanova Montes", "CENTRAL PARK CORUÑA", "Bunfrito relleno de sarrete, higos y parmertier de San Simón", "Brasería Poniente", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/galicia_central-park.jpg", Pincho.SALAD,
    ],
    [
        "La Rioja", "La Rioja", "Monica Loro Romero", "DIVINA CROQUETA", "Divinino", "Shushimore", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/rioja-divina-croqueta.jpg", Pincho.SALAD,
    ],
    [
        "La Rioja", "La Rioja", "Ana Rosa Lasheras Manzanares", "CAFE RESTAURANTE TIZONA", "Deep Impact", "Miel y Mostaza", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/rioja-tizona.jpg", Pincho.SALAD,
    ],
    [
        "Madrid", "Madrid", "Iñaki Rodaballo Rodrigo Rojas", "HUMMA", "Tul y Pan", "La Criolla", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/madrid-humma.jpg", Pincho.SALAD,
    ],
    [
        "Madrid", "Madrid", "Ernesto Ventos", "BAR HERMANOS VINAGRE", "La Naranja que Quería Ser Vermut", "Gastrobar Sabores", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/madrid-hermanos-vinagre.jpg", Pincho.SWEET,
    ],
    [
        "Murcia", "Murcia", "Alvaro Vicente González", "AV KATERING", "De la panocha hasta los andares", "", "", Pincho.SALAD,
    ],
    [
        "Navarra", "Navarra", "Veronica Montespier Foti", "LA HUERTA DE CHICHA", "La Huerta de Chicha", "La Pícara", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/Navarra-la-huerta-de-chicha.jpg", Pincho.SALAD,
    ],
    [
        "Navarra", "Navarra", "Sonia Zaratiegui Sagardoy", "BAR NUEVO HOSTAF", "Nube Picantona", "El Postal", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/navarra-hostaf.jpg", Pincho.SALAD,
    ],
    [
        "País Vasco", "Álava", "Carlos Dávalos Helgar", "WASKA", "KM 0", "Eddy Beer", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/pais-vasco-waska.jpg", Pincho.SALAD,
    ],
    [
        "País Vasco", "Álava", "Mitxel Suarez Suso", "BORDA BERRI", "Txingurri", "La Teja", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/pais-vasco-borda-berri.jpg", Pincho.SALAD,
    ],
    [
        "País Vasco", "Vizcaya", "Juan María Diaz Llanos", "CASA DE MARINOS URIBEKOSTA", "Raíces", "Rioluz Gastronomía", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/pais-vasco-casa-de-marinos.jpg", Pincho.SALAD,
    ],
    [
        "País Vasco", "Vizcaya", "Iñigo Kortabitarte Bilbao", "KOBIKA", "Txerriflower", "Gastrobar Sabores", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/pais-vasco-kobika.jpg", Pincho.SALAD,
    ],
    [
        "País Vasco", "Vizcaya", "Aitor del Olmo Saez", "AMAREN", "Gilda amaren", "Aquarium", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/pais-vasco-amaren.jpg", Pincho.SALAD,
    ],
    [
        "País Vasco", "Vizcaya", "Iker Carrillo Moro", "LA OLLA DE LA PLAZA NUEVA", "Ama", "Mosquera", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/pais-vasco-la-olla-plaza-nueva.jpg", Pincho.SALAD,
    ],
    [
        "Valenciana", "Alicante", "Josep Palomares Albert", "RESTAURANTE XIRI", "Croqueta de gamba al ajillo, su tartar, aceite de maltoser", "La Cacatúa", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/valencia_xiri.jpg", Pincho.SALAD,
    ],
    [
        "Valenciana", "Alicante", "Álvaro Abad García", "EL PLANTIO GOLF RESORT", "…de la Loles", "Moka", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/valencia_el-plantio.jpg", Pincho.SALAD,
    ],
    [
        "Valenciana", "Castellón", "Aitor Martínez Ros", "CAN ROS RESTAURANT", "¿Que fue antes? ¿El huevo o la gallina?", "Aquarium", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/valencia_can-ros.jpg", Pincho.SWEET,
    ],
]

INTERNATIONAL_PINCHOS = [
    [
        "Argentina", "Argentina", "Carlos Emilio Salazar", "Corte Comedor", "La Reina", "Puerto Chico", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/argentina.jpg", Pincho.SALAD,
    ],
    [
        "Canadá", "Canadá", "Aicia Colacci", "Fou D’ici", "Otoño en Canadá", "Trasto", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/canada.jpg", Pincho.SALAD,
    ],
    [
        "Chile", "Chile", "Pilar Astorga", "La Cava del Somelier", "Brava de mar", "Doña Pendeja", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/chile.jpg", Pincho.SALAD,
    ],
    [
        "Dinamarca", "Dinamarca", "Zhara Mian", "The Transient Chef", "L.A.M., Love & Memories", "Los ilustres", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/dinamarca.jpg", Pincho.SALAD,
    ],
    [
        "Ecuador", "Ecuador", "Juan Pablo Holguín", "Tapatú", "Aya/Huma/Cabeza de Diablo", "La Teja", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/ecuador.jpg", Pincho.SALAD,
    ],
    [
        "Emiratos ", "Emiratos Árabes", "Forster Oru", "Me Dubai Hotel", "Canelón de Apio Nabo", "La Corrala del Val", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/emiratos.jpg", Pincho.SALAD,
    ],
    [
        "España", "España", "Emilio Martín", "Suite 22", "Corchifrito", "Suite 22", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/espa%C3%B1a.jpg", Pincho.SALAD,
    ],
    [
        "Estados Unidos", "Estados Unidos", "Joseph Mc Fadden", "Margaritaville", "Pato en tres texturas", "Alquimia", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/espa%C3%B1a.jpg", Pincho.SALAD,
    ],
    [
        "Francia", "Francia", "Delphine Robert", "Super Café", "Caminata en el bosque", "Caroba", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/francia.jpg", Pincho.SALAD,
    ],
    [
        "India", "India", "Angad Rana", "Bikaner Express", "Shammi from the Old Souk", "Los Zagales", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/india.jpg", Pincho.SALAD,
    ],
    [
        "Irlanda", "Irlanda", "Rafael Andrés Pérez", "McGeough’s", "Irish Cacerole", "Gastrobar Sabores", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/irlanda.jpg", Pincho.SALAD,
    ],
    [
        "Japón", "Japón", "Takuya Yuri", "Restaurante Pablo", "Rebozado de Lubina con Salsa de Trufa", "Wabi Sabi Taberna japonesa", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/japon.jpg", Pincho.SALAD,
    ],
    [
        "México", "México", "David Quevedo", "Viñedo San Miguel", "Chile Ceremonial", "La viña de Patxi", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/mexico.jpg", Pincho.SALAD,
    ],
    [
        "Panamá", "Panamá", "Alcides Segovia", "Masi Hotel JW Marriott", "Pescado rebozado en yuca", "Belmondo", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/panama.jpg", Pincho.SALAD,
    ],
    [
        "Portugal", "Portugal", "Manuel Sánchez Noya", "Vintage-Douro", "Rabo de Buey y Alheira", "Don Bacalao", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/portugal.jpg", Pincho.SALAD,
    ],
    [
        "Ucrania", "Ucrania", "Hryhorii Zvirhzde", "Parmigiano", "Lubina y vieira", "5 Gustos", "https://www.info.valladolid.es/blog/wp-content/uploads/2011/10/ucrania.jpg", Pincho.SALAD,
    ],
]

output = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Pinchos de Valladolid 2021</name>
    <Style id="icon-salad-labelson">
      <IconStyle>
        <scale>1</scale>
        <Icon>
          <href>images/salad.png</href>
        </Icon>
      </IconStyle>
    </Style>
    <Style id="icon-salad-labelson-nodesc">
      <IconStyle>
        <scale>1</scale>
        <Icon>
          <href>images/salad.png</href>
        </Icon>
      </IconStyle>
      <BalloonStyle>
        <text><![CDATA[<h3>$[name]</h3>]]></text>
      </BalloonStyle>
    </Style>
    <Style id="icon-sweet-labelson">
      <IconStyle>
        <scale>1</scale>
        <Icon>
          <href>images/sweet.png</href>
        </Icon>
      </IconStyle>
    </Style>
    <Style id="icon-international-labelson">
      <IconStyle>
        <scale>1</scale>
        <Icon>
          <href>images/international.png</href>
        </Icon>
      </IconStyle>
    </Style>
"""

gmaps = googlemaps.Client(GMAPS_API_KEY)
cached_places = {
    'mosquera': {'lat': 41.65028, 'lng': -4.74093},
    'zvumo': {'lat': 41.65166, 'lng': -4.72942},
}


def generate_pincho(pincho):
    global output
    [region, province, chef, restaurante, name, bar, img, kind] = pincho

    location = cached_places.get(bar.lower())
    address = ''
    if bar:
        if not location:
            places = gmaps.find_place(
                f"{bar}, Valladolid, España", "textquery")

            if 'candidates' in places and places['candidates']:
                place_id = places['candidates'][0]['place_id']
                place = gmaps.place(place_id)['result']
                address = place['formatted_address']
                print(f'{bar} in', address)
                location = place['geometry']['location']
                for other_candidate in places['candidates'][1:]:
                    candidate = gmaps.place(
                        other_candidate['place_id'])['result']
                    print(' -> ', candidate['name'], candidate['formatted_address'],
                          candidate['url'])
                cached_places[bar.lower()] = location

    if not location:
        print('WARNING: Using dummy location for', bar)
        location = {'lat': 41.65201, 'lng': -4.72855}

    icon = "icon-salad-labelson"
    if pincho in INTERNATIONAL_PINCHOS:
        icon = "icon-international-labelson"
    elif kind == Pincho.SWEET:
        icon = "icon-sweet-labelson"

    output += f"""
      <Placemark>
        <name>{escape(bar)} - {escape(name)}</name>
        <description><![CDATA[{escape(address)}<br>{escape(name)}<br>{escape(region)} - {escape(province)}<br>Chef: {escape(chef)}<br>{escape(restaurante)}]]></description>
        <styleUrl>#{icon}</styleUrl>
        <ExtendedData>
          <Data name="gx_media_links">
            <value><![CDATA[{img}]]></value>
          </Data>
        </ExtendedData>
        <Point>
          <coordinates>
            {location['lng']},{location['lat']}
          </coordinates>
        </Point>
      </Placemark>"""


def pinchos_category(name, pinchos):
    global output
    output += f"""
    <Folder>
      <name>{name}</name>"""

    for pincho in pinchos:
        generate_pincho(pincho)

    output += "    </Folder>"


pinchos_category("Pinchos Nacionales", filter(
    lambda pincho: pincho[7] == Pincho.SALAD, NATIONAL_PINCHOS))

pinchos_category("Pinchos Nacionales Dulces", filter(
    lambda pincho: pincho[7] == Pincho.SWEET, NATIONAL_PINCHOS))

pinchos_category("Pinchos Internacionales", INTERNATIONAL_PINCHOS)

output += """
  </Document>
</kml>
"""

with open('doc.kml', 'w') as f:
    f.write(output)
