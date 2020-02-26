import glob

from pykml import parser

with open("all_countries.csv", "w+") as o_file:
    o_file.write('name,web,lat,long,country\n')
    for kml_file in glob.glob('*.kml'):
        region_country = kml_file.strip('.kml')
        print(region_country + "...")
        with open(kml_file, 'r') as i_file:
            kml_obj = parser.parse(i_file)
            for placemark in kml_obj.findall('.//{http://www.opengis.net/kml/2.2}Placemark'):
                name = str(placemark.name).strip()
                try:
                    web = str(placemark.description).strip()
                except:
                    # if there's no description, there's no description.
                    web = ''
                try:
                    lat, long, _ = placemark.Point.coordinates.text.split(',')
                except:
                    # nothing to be done if we can't find a point for it
                    continue
                lat = str(lat).strip()
                long = str(long).strip()
                o_file.write(','.join([name, web, lat, long, region_country]))
                o_file.write('\n')
        print("done")
