from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import plotly

db = SQLAlchemy()


class Airbnb(db.Model):
    __tablename__ = 'airbnbs'
    id = db.Column(db.Integer, primary_key=True)
    neighbourhood = db.Column(db.String(255))
    latitude = db.Column(db.Numeric)
    longitude = db.Column(db.Numeric)
    room_type = db.Column(db.String(255))
    price = db.Column(db.Numeric)

class Crime(db.Model):
    __tablename__ = 'crime_data'
    SORT_ORDER = db.Column(db.Integer, primary_key=True)
    Crime = db.Column(db.Text)
    ADAMS_NORTH = db.Column(db.Integer)
    ALLIED_GARDENS = db.Column(db.Integer)
    ALTA_VISTA = db.Column(db.Integer)
    AZALEA_HOLLYWOOD_PARK = db.Column(db.Integer)
    BALBOA_PARK = db.Column(db.Integer)
    BARRIO_LOGAN = db.Column(db.Integer)
    BAY_HO = db.Column(db.Integer)
    BAY_PARK = db.Column(db.Integer)
    BAY_TERRACES = db.Column(db.Integer)
    BIRDLAND = db.Column(db.Integer)
    BLACK_MOUNTAIN_RANCH = db.Column(db.Integer)
    BORDER = db.Column(db.Integer)
    BROADWAY_HEIGHTS = db.Column(db.Integer)
    BURLINGAME = db.Column(db.Integer)
    CARMEL_MOUNTAIN = db.Column(db.Integer)
    CARMEL_VALLEY = db.Column(db.Integer)
    CASTLE = db.Column(db.Integer)
    CHEROKEE_POINT = db.Column(db.Integer)
    CHOLLAS_CREEK = db.Column(db.Integer)
    CHOLLAS_VIEW = db.Column(db.Integer)
    CLAIREMONT_MESA_EAST = db.Column(db.Integer)
    CLAIREMONT_MESA_WEST = db.Column(db.Integer)
    COLINA_DEL_SOL = db.Column(db.Integer)
    COLLEGE_AREA_EAST = db.Column(db.Integer)
    COLLEGE_AREA_WEST = db.Column(db.Integer)
    CORE_COLUMBIA = db.Column(db.Integer)
    CORRIDOR = db.Column(db.Integer)
    CORTEZ = db.Column(db.Integer)
    DEL_CERRO = db.Column(db.Integer)
    DEL_MAR_HEIGHTS = db.Column(db.Integer)
    EAST_VILLAGE = db.Column(db.Integer)
    EGGER_HIGHLANDS = db.Column(db.Integer)
    EL_CERRITO = db.Column(db.Integer)
    EMERALD_HILLS = db.Column(db.Integer)
    ENCANTO = db.Column(db.Integer)
    FAIRMOUNT_PARK = db.Column(db.Integer)
    FAIRMOUNT_VILLAGE = db.Column(db.Integer)
    FOX_CANYON = db.Column(db.Integer)
    GASLAMP = db.Column(db.Integer)
    GOLDEN_HILL = db.Column(db.Integer)
    GRANT_HILL = db.Column(db.Integer)
    GRANTVILLE = db.Column(db.Integer)
    HARBORVIEW = db.Column(db.Integer)
    HILLCREST = db.Column(db.Integer)
    HORTON_PLAZA = db.Column(db.Integer)
    ISLENAIR = db.Column(db.Integer)
    JAMACHA_LOMITA = db.Column(db.Integer)
    KEARNY_MESA = db.Column(db.Integer)
    KENSINGTON = db.Column(db.Integer)
    LA_JOLLA = db.Column(db.Integer)
    LA_PLAYA = db.Column(db.Integer)
    LAKE_MURRAY = db.Column(db.Integer)
    LINCOLN_PARK = db.Column(db.Integer)
    LINDA_VISTA = db.Column(db.Integer)
    LITTLE_ITALY = db.Column(db.Integer)
    LOGAN_HEIGHTS = db.Column(db.Integer)
    LOMA_PORTAL = db.Column(db.Integer)
    MARINA = db.Column(db.Integer)
    MIDTOWN = db.Column(db.Integer)
    MIDWAY_DISTRICT = db.Column(db.Integer)
    MIRA_MESA = db.Column(db.Integer)
    MIRAMAR = db.Column(db.Integer)
    MIRAMAR_RANCH_NORTH = db.Column(db.Integer)
    MISSION_BAY_PARK = db.Column(db.Integer)
    MISSION_BEACH = db.Column(db.Integer)
    MISSION_HILLS = db.Column(db.Integer)
    MISSION_VALLEY_EAST = db.Column(db.Integer)
    MISSION_VALLEY_WEST = db.Column(db.Integer)
    MORENA = db.Column(db.Integer)
    MOUNTAIN_VIEW = db.Column(db.Integer)
    MT_HOPE = db.Column(db.Integer)
    NESTOR = db.Column(db.Integer)
    NORMAL_HEIGHTS = db.Column(db.Integer)
    NORTH_CITY = db.Column(db.Integer)
    NORTH_CLAIREMONT = db.Column(db.Integer)
    NORTH_PARK = db.Column(db.Integer)
    OAK_PARK = db.Column(db.Integer)
    OCEAN_BEACH = db.Column(db.Integer)
    OCEAN_CREST = db.Column(db.Integer)
    OLD_TOWN = db.Column(db.Integer)
    OTAY_MESA = db.Column(db.Integer)
    OTAY_MESA_WEST = db.Column(db.Integer)
    PACIFIC_BEACH = db.Column(db.Integer)
    PALM_CITY = db.Column(db.Integer)
    PARADISE_HILLS = db.Column(db.Integer)
    PARK_WEST = db.Column(db.Integer)
    PETCO_PARK = db.Column(db.Integer)
    POINT_LOMA_HEIGHTS = db.Column(db.Integer)
    QUALCOMM = db.Column(db.Integer)
    RANCHO_BERNARDO = db.Column(db.Integer)
    RANCHO_ENCANTADA = db.Column(db.Integer)
    RANCHO_PENASQUITOS = db.Column(db.Integer)
    REDWOOD_VILLAGE_ROLANDO_PARK = db.Column(db.Integer)
    RIDGEVIEW_WEBSTER = db.Column(db.Integer)
    ROLANDO = db.Column(db.Integer)
    ROSEVILLE_FLEET_RIDGE = db.Column(db.Integer)
    SABRE_SPRINGS = db.Column(db.Integer)
    SAN_CARLOS = db.Column(db.Integer)
    SAN_PASQUAL = db.Column(db.Integer)
    SAN_YSIDRO = db.Column(db.Integer)
    SCRIPPS_RANCH = db.Column(db.Integer)
    SERRA_MESA = db.Column(db.Integer)
    SHELLTOWN = db.Column(db.Integer)
    SHERMAN_HEIGHTS = db.Column(db.Integer)
    SKYLINE = db.Column(db.Integer)
    SORRENTO_VALLEY = db.Column(db.Integer)
    SOUTH_PARK = db.Column(db.Integer)
    SOUTHCREST = db.Column(db.Integer)
    STOCKTON = db.Column(db.Integer)
    SUNSET_CLIFFS = db.Column(db.Integer)
    SWAN_CANYON = db.Column(db.Integer)
    TALMADGE = db.Column(db.Integer)
    TERALTA_EAST = db.Column(db.Integer)
    TERALTA_WEST = db.Column(db.Integer)
    TIERRASANTA = db.Column(db.Integer)
    TIJUANA_RIVER_VALLEY = db.Column(db.Integer)
    TORREY_HIGHLANDS = db.Column(db.Integer)
    TORREY_PINES = db.Column(db.Integer)
    TORREY_PRESERVE = db.Column(db.Integer)
    UNDEFINED = db.Column(db.Integer)
    UNIVERSITY_CITY = db.Column(db.Integer)
    UNIVERSITY_HEIGHTS = db.Column(db.Integer)
    VALENCIA_PARK = db.Column(db.Integer)
    WOODED_AREA = db.Column(db.Integer)
    Total = db.Column(db.Integer)
    

class Crash_Locations(db.Model):
    __tablename__ = 'Crash_Locations'
    number = db.Column(db.Integer, primary_key=True)
    accident_year = db.Column(db.Integer)
    collision_date = db.Column(db.String(255))
    collision_time  = db.Column(db.Integer)
    Day_of_week = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    latitude = db.Column(db.Integer) 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mypostgres:postgres@localhost:5432/vacation_safety_db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/airbnb')
def airbnb_data():

    try:
        airbnb_data = Airbnb.query.all()

        results = [{'neighbourhood': data.neighbourhood, 'latitude': data.latitude, 'longitude': data.longitude, 'room_type': data.room_type, 'price': data.price} for data in airbnb_data]
        print(results)
    
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/crime')
def crime_data():
    try:
        crime_data = Crime.query.all()
        data_list = [{'SORT_ORDER': data.SORT_ORDER, 'Crime': data.Crime, 'ADAMS_NORTH': data.ADAMS_NORTH, 'ALLIED_GARDENS': data.ALLIED_GARDENS, 'ALTA_VISTA': data.ALTA_VISTA, 
                      'AZALEA_HOLLYWOOD_PARK': data.AZALEA_HOLLYWOOD_PARK, 'BALBOA_PARK': data.BALBOA_PARK, 'BARRIO_LOGAN': data.BARRIO_LOGAN, 'BAY_HO': data.BAY_HO, 'BAY_PARK': data.BAY_PARK, 
                      'BAY_TERRACES': data.BAY_TERRACES, 'BIRDLAND': data.BIRDLAND, 'BLACK_MOUNTAIN_RANCH': data.BLACK_MOUNTAIN_RANCH, 'BORDER': data.BORDER, 'BROADWAY_HEIGHTS': data.BROADWAY_HEIGHTS, 
                      'BURLINGAME': data.BURLINGAME, 'CARMEL_MOUNTAIN': data.CARMEL_MOUNTAIN, 'CARMEL_VALLEY': data.CARMEL_VALLEY, 'CASTLE': data.CASTLE, 'CHEROKEE_POINT': data.CHEROKEE_POINT, 
                      'CHOLLAS_CREEK': data.CHOLLAS_CREEK, 'CHOLLAS_VIEW': data.CHOLLAS_VIEW, 'CLAIREMONT_MESA_EAST': data.CLAIREMONT_MESA_EAST, 'CLAIREMONT_MESA_WEST': data.CLAIREMONT_MESA_WEST,
                      'COLINA_DEL_SOL': data.COLINA_DEL_SOL, 'COLLEGE_AREA_EAST': data.COLLEGE_AREA_EAST, 'COLLEGE_AREA_WEST': data.COLLEGE_AREA_WEST, 'CORE_COLUMBIA': data.CORE_COLUMBIA, 
                      'CORRIDOR': data.CORRIDOR, 'CORTEZ': data.CORTEZ, 'DEL_CERRO': data.DEL_CERRO, 'DEL_MAR_HEIGHTS': data.DEL_MAR_HEIGHTS, 'EAST_VILLAGE': data.EAST_VILLAGE, 
                      'EGGER_HIGHLANDS': data.EGGER_HIGHLANDS, 'EL_CERRITO': data.EL_CERRITO, 'EMERALD_HILLS': data.EMERALD_HILLS, 'ENCANTO': data.ENCANTO, 'FAIRMOUNT_PARK': data.FAIRMOUNT_PARK,
                      'FAIRMOUNT_VILLAGE': data.FAIRMOUNT_VILLAGE, 'FOX_CANYON': data.FOX_CANYON, 'GASLAMP': data.GASLAMP, 'GOLDEN_HILL': data.GOLDEN_HILL, 'GRANT_HILL': data.GRANT_HILL, 
                      'GRANTVILLE': data.GRANTVILLE, 'HARBORVIEW': data.HARBORVIEW, 'HILLCREST': data.HILLCREST, 'HORTON_PLAZA': data.HORTON_PLAZA, 'ISLENAIR': data.ISLENAIR,
                      'JAMACHA_LOMITA': data.JAMACHA_LOMITA, 'KEARNY_MESA': data.KEARNY_MESA, 'KENSINGTON': data.KENSINGTON, 'LA_JOLLA': data.LA_JOLLA, 'LA_PLAYA': data.LA_PLAYA,
                      'LAKE_MURRAY': data.LAKE_MURRAY, 'LINCOLN_PARK': data.LINCOLN_PARK, 'LINDA_VISTA': data.LINDA_VISTA, 'LITTLE_ITALY': data.LITTLE_ITALY, 'LOGAN_HEIGHTS': data.LOGAN_HEIGHTS,
                      'LOMA_PORTAL': data.LOMA_PORTAL, 'MARINA': data.MARINA, 'MIDTOWN': data.MIDTOWN, 'MIDWAY_DISTRICT': data.MIDWAY_DISTRICT, 'MIRA_MESA': data.MIRA_MESA, 'MIRAMAR': data.MIRAMAR,
                      'MIRAMAR_RANCH_NORTH': data.MIRAMAR_RANCH_NORTH, 'MISSION_BAY_PARK': data.MISSION_BAY_PARK, 'MISSION_BEACH': data.MISSION_BEACH, 'MISSION_HILLS': data.MISSION_HILLS,
                      'MISSION_VALLEY_EAST': data.MISSION_VALLEY_EAST, 'MISSION_VALLEY_WEST': data.MISSION_VALLEY_WEST, 'MORENA': data.MORENA, 'MOUNTAIN_VIEW': data.MOUNTAIN_VIEW, 
                      'MT_HOPE': data.MT_HOPE, 'NESTOR': data.NESTOR, 'NORMAL_HEIGHTS': data.NORMAL_HEIGHTS, 'NORTH_CITY': data.NORTH_CITY, 'NORTH_CLAIREMONT': data.NORTH_CLAIREMONT,
                      'NORTH_PARK': data.NORTH_PARK, 'OAK_PARK': data.OAK_PARK, 'OCEAN_BEACH': data.OCEAN_BEACH, 'OCEAN_CREST': data.OCEAN_CREST, 'OLD_TOWN': data.OLD_TOWN, 'OTAY_MESA': data.OTAY_MESA,
                      'OTAY_MESA_WEST': data.OTAY_MESA_WEST, 'PACIFIC_BEACH': data.PACIFIC_BEACH, 'PALM_CITY': data.PALM_CITY, 'PARADISE_HILLS': data.PARADISE_HILLS, 'PARK_WEST': data.PARK_WEST,
                      'PETCO_PARK': data.PETCO_PARK, 'POINT_LOMA_HEIGHTS': data.POINT_LOMA_HEIGHTS, 'QUALCOMM': data.QUALCOMM, 'RANCHO_BERNARDO': data.RANCHO_BERNARDO, 'RANCHO_ENCANTADA': data.RANCHO_ENCANTADA,
                      'RANCHO_PENASQUITOS': data.RANCHO_PENASQUITOS, 'REDWOOD_VILLAGE_ROLANDO_PARK': data.REDWOOD_VILLAGE_ROLANDO_PARK, 'RIDGEVIEW_WEBSTER': data.RIDGEVIEW_WEBSTER,
                      'ROLANDO': data.ROLANDO, 'ROSEVILLE_FLEET_RIDGE': data.ROSEVILLE_FLEET_RIDGE, 'SABRE_SPRINGS': data.SABRE_SPRINGS, 'SAN_CARLOS': data.SAN_CARLOS, 'SAN_PASQUAL': data.SAN_PASQUAL,
                      'SAN_YSIDRO': data.SAN_YSIDRO, 'SCRIPPS_RANCH': data.SCRIPPS_RANCH, 'SERRA_MESA': data.SERRA_MESA, 'SHELLTOWN': data.SHELLTOWN, 'SHERMAN_HEIGHTS': data.SHERMAN_HEIGHTS,
                      'SKYLINE': data.SKYLINE, 'SORRENTO_VALLEY': data.SORRENTO_VALLEY, 'SOUTH_PARK': data.SOUTH_PARK, 'SOUTHCREST': data.SOUTHCREST, 'STOCKTON': data.STOCKTON, 
                      'SUNSET_CLIFFS': data.SUNSET_CLIFFS, 'SWAN_CANYON': data.SWAN_CANYON, 'TALMADGE': data.TALMADGE, 'TERALTA_EAST': data.TERALTA_EAST, 'TERALTA_WEST': data.TERALTA_WEST, 
                      'TIERRASANTA': data.TIERRASANTA, 'TIJUANA_RIVER_VALLEY': data.TIJUANA_RIVER_VALLEY, 'TORREY_HIGHLANDS': data.TORREY_HIGHLANDS, 'TORREY_PINES': data.TORREY_PINES, 
                      'TORREY_PRESERVE': data.TORREY_PRESERVE, 'UNDEFINED': data.UNDEFINED, 'UNIVERSITY_CITY': data.UNIVERSITY_CITY, 'UNIVERSITY_HEIGHTS': data.UNIVERSITY_HEIGHTS,
                      'VALENCIA_PARK': data.VALENCIA_PARK, 'WOODED_AREA': data.WOODED_AREA, 'Total': data.Total} for data in crime_data]
        return jsonify(data_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/car_crash')
def crash_data():
    try:
        pie_data = Crash_Locations.query.all()

        data_list = [{'number': data.number, 'accident_year': data.accident_year, 'collision_date': data.collision_date, 'collision_time': data.collision_time, 
                      'Day_of_week': data.Day_of_week, 'longitude': data.longitude, 'latitude': data.latitude} for data in pie_data]
        
        return jsonify(data_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)