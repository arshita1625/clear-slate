from flask import Flask, request, jsonify, render_template
from database import db, init_db
from models import Location
from flask_cors import CORS
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///safe_spaces.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
CORS(app)
sample_location = [
    {"id": 1, "name": "The 519", "type": "LGBTQ+ Community Center", "address": "519 Church St, Toronto, ON M4Y 2C9, Canada"},
    {"id": 2, "name": "Woody's", "type": "LGBTQ+ Bar/Club", "address": "467 Church St, Toronto, ON M4Y 2C5, Canada"},
    {"id": 3, "name": "Oasis AquaGolf", "type": "LGBTQ+ Friendly Outdoor Club", "address": "3001 Davenport Rd, Toronto, ON M6N 4X8, Canada"},
    {"id": 4, "name": "Church-Wellesley Village", "type": "LGBTQ+ District/Area", "address": "Toronto, ON M4Y 1J3, Canada"},
    {"id": 5, "name": "The Gladstone Hotel", "type": "LGBTQ+ Friendly Hotel/Club", "address": "1214 Queen St W, Toronto, ON M6J 1J6, Canada"},
    {"id": 6, "name": "Buddies in Bad Times Theatre", "type": "LGBTQ+ Theatre/Performance Venue", "address": "12 Alexander St, Toronto, ON M4Y 1B7, Canada"},
    {"id": 7, "name": "Pride Toronto Office", "type": "LGBTQ+ Community Organization", "address": "519 Church St, Toronto, ON M4Y 2C9, Canada"},
    {"id": 8, "name": "Steamworks Baths", "type": "LGBTQ+ Sauna/Restroom", "address": "478 Queen St E, Toronto, ON M5A 1T3, Canada"},
    {"id": 9, "name": "Glad Day Bookshop", "type": "LGBTQ+ Bookstore/Cafe", "address": "499 Church St, Toronto, ON M4Y 2C6, Canada"},
    {"id": 10, "name": "The Artful Dodger", "type": "LGBTQ+ Bar/Club", "address": "24 Wellesley St W, Toronto, ON M4Y 1L5, Canada"},
    {"id": 11, "name": "The Garrison", "type": "LGBTQ+ Club/Live Music Venue", "address": "1197 Dundas St W, Toronto, ON M6J 1X3, Canada"},
    {"id": 12, "name": "The Drake Hotel", "type": "LGBTQ+ Friendly Hotel/Bar", "address": "1150 Queen St W, Toronto, ON M6J 1J3, Canada"},
    {"id": 13, "name": "The Casa Loma", "type": "LGBTQ+ Friendly Historic Site", "address": "1 Austin Terrace, Toronto, ON M5R 1X8, Canada"},
    {"id": 14, "name": "Soma Toronto", "type": "LGBTQ+ Bar", "address": "170 Spadina Ave, Toronto, ON M5T 2C2, Canada"},
    {"id": 15, "name": "The Black Eagle", "type": "LGBTQ+ Bar", "address": "457 Church St, Toronto, ON M4Y 2C6, Canada"},
    {"id": 16, "name": "Q Space", "type": "LGBTQ+ Community Space", "address": "21 Dovercourt Rd, Toronto, ON M6J 3C1, Canada"},
    {"id": 17, "name": "The Swan", "type": "LGBTQ+ Bar", "address": "758 Queen St E, Toronto, ON M4M 1H4, Canada"},
    {"id": 18, "name": "Remington's", "type": "LGBTQ+ Bar", "address": "432 Church St, Toronto, ON M4Y 2C6, Canada"},
    {"id": 19, "name": "Xtra", "type": "LGBTQ+ Bar", "address": "58 Church St, Toronto, ON M5C 2G1, Canada"},
    {"id": 20, "name": "Village Vanguard", "type": "LGBTQ+ Bar", "address": "533 Church St, Toronto, ON M4Y 2C9, Canada"},
    {"id": 21, "name": "Bar Bovine", "type": "LGBTQ+ Friendly Bar", "address": "1348 Queen St W, Toronto, ON M6K 1L4, Canada"},
    {"id": 22, "name": "Pride House Toronto", "type": "LGBTQ+ Resource Center", "address": "140 Jarvis St, Toronto, ON M5C 2H3, Canada"},
    {"id": 23, "name": "Rainbow Health Ontario", "type": "LGBTQ+ Health Services", "address": "400 University Ave, Toronto, ON M5G 1S5, Canada"},
    {"id": 24, "name": "Bimbo's", "type": "LGBTQ+ Club", "address": "1268 Dundas St W, Toronto, ON M6J 1X6, Canada"},
    {"id": 25, "name": "The Beaver", "type": "LGBTQ+ Bar", "address": "1192 Queen St W, Toronto, ON M6J 1J6, Canada"},
    {"id": 26, "name": "The Gladstone Hotel", "type": "LGBTQ+ Bar/Hotel", "address": "1214 Queen St W, Toronto, ON M6J 1J6, Canada"},
    {"id": 27, "name": "Big Primpin' Bar", "type": "LGBTQ+ Nightclub", "address": "1471 Queen St W, Toronto, ON M6K 1L3, Canada"},
    {"id": 28, "name": "The Front", "type": "LGBTQ+ Friendly Restaurant", "address": "64 Front St W, Toronto, ON M5J 1E6, Canada"},
    {"id": 29, "name": "F*ck Cancer Foundation", "type": "LGBTQ+ Nonprofit Organization", "address": "305 Richmond St W, Toronto, ON M5V 1X2, Canada"},
    {"id": 30, "name": "Hot Dog Café", "type": "LGBTQ+ Bar", "address": "3 Gerrard St E, Toronto, ON M5B 1Z5, Canada"},
    {"id": 31, "name": "The Wellington", "type": "LGBTQ+ Friendly Pub", "address": "520 Wellington St W, Toronto, ON M5V 1G1, Canada"},
    {"id": 32, "name": "Jungle", "type": "LGBTQ+ Bar", "address": "240 Victoria St, Toronto, ON M5B 1V4, Canada"},
    {"id": 33, "name": "Goldies", "type": "LGBTQ+ Club", "address": "168 King St W, Toronto, ON M5V 1J2, Canada"},
    {"id": 34, "name": "The Pilot", "type": "LGBTQ+ Friendly Pub", "address": "22 Cumberland St, Toronto, ON M4W 1J5, Canada"},
    {"id": 35, "name": "Homo Brunch", "type": "LGBTQ+ Event", "address": "1334 Bay St, Toronto, ON M5R 2H2, Canada"},
    {"id": 36, "name": "Vivid Nightclub", "type": "LGBTQ+ Nightclub", "address": "181 Richmond St W, Toronto, ON M5V 1W1, Canada"},
    {"id": 37, "name": "Club 120", "type": "LGBTQ+ Club", "address": "120 Church St, Toronto, ON M5C 2G5, Canada"},
    {"id": 38, "name": "Peaches", "type": "LGBTQ+ Bar", "address": "1100 Queen St E, Toronto, ON M4M 1J3, Canada"},
    {"id": 39, "name": "Black Eagle", "type": "LGBTQ+ Bar", "address": "457 Church St, Toronto, ON M4Y 2C6, Canada"},
    {"id": 40, "name": "Thompson Toronto", "type": "LGBTQ+ Friendly Hotel", "address": "550 Wellington St W, Toronto, ON M5V 2V4, Canada"},
    {"id": 41, "name": "Vivid Lounge", "type": "LGBTQ+ Lounge", "address": "123 Queen St W, Toronto, ON M5H 2M9, Canada"},
    {"id": 42, "name": "The Steel", "type": "LGBTQ+ Friendly Venue", "address": "7 Dundas St E, Toronto, ON M5B 2H4, Canada"},
    {"id": 43, "name": "Taco Tiki", "type": "LGBTQ+ Friendly Restaurant", "address": "1372 Yonge St, Toronto, ON M4T 1X7, Canada"},
    {"id": 44, "name": "Gay Village", "type": "LGBTQ+ District", "address": "Toronto, ON M4Y 2C6, Canada"},
    {"id": 45, "name": "Rainbow Bistro", "type": "LGBTQ+ Bar", "address": "141A Rideau St, Ottawa, ON K1N 5X1, Canada"},
    {"id": 46, "name": "Fairmont Royal York", "type": "LGBTQ+ Friendly Hotel", "address": "100 Front St W, Toronto, ON M5J 1E3, Canada"},
    {"id": 47, "name": "LGBTQ+ Sanctuary", "type": "LGBTQ+ Safe Space", "address": "1040 Yonge St, Toronto, ON M4W 2J2, Canada"},
    {"id": 48, "name": "Buddies in Bad Times Theatre", "type": "LGBTQ+ Theatre", "address": "12 Alexander St, Toronto, ON M4Y 1B7, Canada"},
    {"id": 49, "name": "Sunset Grill", "type": "LGBTQ+ Friendly Restaurant", "address": "200 Queen St W, Toronto, ON M5V 3M5, Canada"},
    {"id": 50, "name": "Waterloo LGBTQ+ Community Centre", "type": "LGBTQ+ Community Center", "address": "100 King St N, Waterloo, ON N2J 4A8, Canada"},
    {"id": 51, "name": "Club Abstract", "type": "LGBTQ+ Club", "address": "45 King St W, Waterloo, ON N2J 1P4, Canada"},
    {"id": 52, "name": "The Barrel Restaurant & Lounge", "type": "LGBTQ+ Friendly Restaurant", "address": "142 King St N, Waterloo, ON N2J 2Z4, Canada"},
    {"id": 53, "name": "LGBTQ+ Resource Centre", "type": "LGBTQ+ Resource Center", "address": "200 University Ave W, Waterloo, ON N2L 3G1, Canada"},
    {"id": 54, "name": "Café 58", "type": "LGBTQ+ Friendly Café", "address": "58 Erb St E, Waterloo, ON N2J 1L6, Canada"},
    {"id": 55, "name": "The Museum", "type": "LGBTQ+ Friendly Venue", "address": "10 King St N, Waterloo, ON N2J 1N8, Canada"},
    {"id": 56, "name": "Waterloo Pride House", "type": "LGBTQ+ Pride Organization", "address": "50 Victoria St S, Waterloo, ON N2J 4P6, Canada"},
    {"id": 57, "name": "The Yeti Bar", "type": "LGBTQ+ Bar", "address": "142 Erb St E, Waterloo, ON N2J 1S5, Canada"},
    {"id": 58, "name": "The Multicultural Centre", "type": "LGBTQ+ Community Space", "address": "46 Erb St E, Waterloo, ON N2J 1L3, Canada"},
    {"id": 59, "name": "Club Waterloo", "type": "LGBTQ+ Bar/Club", "address": "45 King St W, Waterloo, ON N2J 1P4, Canada"},
    {"id": 60, "name": "Cafe Pyrus", "type": "LGBTQ+ Friendly Café", "address": "16 King St N, Waterloo, ON N2J 2W7, Canada"},
    {"id": 61, "name": "Waterloo Queer Film Festival", "type": "LGBTQ+ Film Festival", "address": "200 University Ave W, Waterloo, ON N2L 3G1, Canada"},
    {"id": 62, "name": "Kitchener-Waterloo LGBTQ+ Choir", "type": "LGBTQ+ Community Choir", "address": "53 Queen St N, Kitchener, ON N2H 2H4, Canada"},
    {"id": 63, "name": "Outreach Program Waterloo", "type": "LGBTQ+ Outreach Organization", "address": "100 Columbia St W, Waterloo, ON N2L 3K7, Canada"},
    {"id": 64, "name": "LGBTQ+ Youth Centre", "type": "LGBTQ+ Youth Resource Centre", "address": "420 Weber St N, Waterloo, ON N2L 4E7, Canada"},
    {"id": 65, "name": "The Church Street Night Club", "type": "LGBTQ+ Nightclub", "address": "147 King St N, Waterloo, ON N2J 1P8, Canada"},
    {"id": 66, "name": "Waterloo LGBTQ+ Pride Parade", "type": "LGBTQ+ Parade", "address": "100 King St N, Waterloo, ON N2J 4A8, Canada"},
    {"id": 67, "name": "Kitchener-Waterloo Pride Office", "type": "LGBTQ+ Pride Organization", "address": "201 King St W, Kitchener, ON N2G 1C6, Canada"},
    {"id": 68, "name": "Starlight Lounge", "type": "LGBTQ+ Lounge", "address": "8 Queen St N, Kitchener, ON N2H 2G2, Canada"},
    {"id": 69, "name": "The Workshop", "type": "LGBTQ+ Art Space", "address": "300 King St W, Waterloo, ON N2J 1A9, Canada"},
    {"id": 70, "name": "Bar Dojo", "type": "LGBTQ+ Friendly Bar", "address": "145 King St W, Waterloo, ON N2J 1P5, Canada"},
    {"id": 71, "name": "Waterloo Arts Hub", "type": "LGBTQ+ Art Gallery", "address": "80 King St N, Waterloo, ON N2J 2Z4, Canada"},
    {"id": 72, "name": "The Duke of Wellington", "type": "LGBTQ+ Friendly Pub", "address": "400 King St W, Waterloo, ON N2J 2Y8, Canada"},
    {"id": 73, "name": "The Transgender Support Group", "type": "LGBTQ+ Support Group", "address": "9 King St S, Waterloo, ON N2J 1P3, Canada"},
    {"id": 74, "name": "Pride at Work Waterloo", "type": "LGBTQ+ Workplace Group", "address": "5 King St N, Waterloo, ON N2J 4A9, Canada"},
    {"id": 75, "name": "The Social Butterfly", "type": "LGBTQ+ Club", "address": "140 Erb St W, Waterloo, ON N2L 1Z6, Canada"},
    {"id": 76, "name": "LGBTQ+ Health Centre", "type": "LGBTQ+ Health Services", "address": "270 King St W, Kitchener, ON N2G 1C5, Canada"},
    {"id": 77, "name": "The Rainbow Lounge", "type": "LGBTQ+ Lounge", "address": "325 King St E, Waterloo, ON N2J 2L5, Canada"},
    {"id": 78, "name": "Cross-Dressing Meet-up Group", "type": "LGBTQ+ Support Group", "address": "19 King St S, Waterloo, ON N2J 2Y4, Canada"},
    {"id": 79, "name": "The Lavender Door", "type": "LGBTQ+ Friendly Pub", "address": "67 King St N, Waterloo, ON N2J 1P7, Canada"},
    {"id": 80, "name": "Sunset Club", "type": "LGBTQ+ Nightclub", "address": "150 King St N, Waterloo, ON N2J 1P9, Canada"},
    {"id": 81, "name": "The Garden", "type": "LGBTQ+ Friendly Cafe", "address": "134 Erb St E, Waterloo, ON N2J 1S7, Canada"},
    {"id": 82, "name": "Waterloo Social Club", "type": "LGBTQ+ Social Club", "address": "140 Victoria St S, Waterloo, ON N2J 1B8, Canada"},
    {"id": 83, "name": "Kitchener LGBTQ+ Youth Centre", "type": "LGBTQ+ Youth Centre", "address": "115 King St W, Kitchener, ON N2G 1C9, Canada"},
    {"id": 84, "name": "The Rainbow Connection", "type": "LGBTQ+ Community Group", "address": "400 King St W, Kitchener, ON N2G 2H2, Canada"},
    {"id": 85, "name": "Diversity Dance", "type": "LGBTQ+ Event", "address": "89 Queen St N, Waterloo, ON N2J 2Y3, Canada"},
    {"id": 86, "name": "Waterloo LGBTQ+ Resource Centre", "type": "LGBTQ+ Resource Centre", "address": "300 University Ave W, Waterloo, ON N2L 3G1, Canada"},
    {"id": 87, "name": "Transgender Equality Group", "type": "LGBTQ+ Support Group", "address": "45 Victoria St S, Waterloo, ON N2J 4N5, Canada"},
    {"id": 88, "name": "LGBTQ+ Allies Cafe", "type": "LGBTQ+ Friendly Cafe", "address": "23 King St N, Waterloo, ON N2J 1P7, Canada"},
    {"id": 89, "name": "Out in the Open", "type": "LGBTQ+ Support Group", "address": "10 King St N, Waterloo, ON N2J 2Y3, Canada"},
    {"id": 90, "name": "Rainbow Book Club", "type": "LGBTQ+ Book Club", "address": "22 King St N, Waterloo, ON N2J 1P7, Canada"},
    {"id": 91, "name": "Lesbian Bookstore", "type": "LGBTQ+ Bookstore", "address": "70 King St N, Waterloo, ON N2J 2Y3, Canada"},
    {"id": 92, "name": "Rainbow Healing Centre", "type": "LGBTQ+ Healing Space", "address": "132 Erb St E, Waterloo, ON N2J 2L3, Canada"},
    {"id": 93, "name": "LGBTQ+ Family Support Centre", "type": "LGBTQ+ Family Support", "address": "20 King St N, Waterloo, ON N2J 1P8, Canada"},
    {"id": 94, "name": "Queer Potluck Group", "type": "LGBTQ+ Social Group", "address": "150 King St S, Waterloo, ON N2J 1B8, Canada"},
    {"id": 95, "name": "LGBTQ+ Safe Space", "type": "LGBTQ+ Safe Space", "address": "80 Erb St E, Waterloo, ON N2J 2L2, Canada"},
    {"id": 96, "name": "Waterloo Queer Night", "type": "LGBTQ+ Night", "address": "250 University Ave W, Waterloo, ON N2L 3G1, Canada"},
    {"id": 97, "name": "The Pride Place", "type": "LGBTQ+ Pride Venue", "address": "320 King St N, Waterloo, ON N2L 3Z5, Canada"},
    {"id": 98, "name": "LGBTQ+ Dance Party", "type": "LGBTQ+ Dance Event", "address": "23 Victoria St N, Waterloo, ON N2L 2J5, Canada"},
    {"id": 99, "name": "The Safe Zone", "type": "LGBTQ+ Friendly Venue", "address": "100 Erb St W, Waterloo, ON N2L 1S7, Canada"},
    {"id": 100, "name": "Rainbow Collective", "type": "LGBTQ+ Community Group", "address": "52 Queen St N, Waterloo, ON N2J 4A9, Canada"}
    
]
@app.route('/')
def home():
    return "Welcome to Space fyndr app."
@app.route("/locations", methods=["GET"])
def get_locations():
    # locations = Location.query.all()
    return jsonify(sample_location)

@app.route("/add_location", methods=["POST"])
def add_location():
    data = request.get_json()
    new_location = Location(name=data["name"], type=data["type"], address=data["address"])
    db.session.add(new_location)
    db.session.commit()
    return jsonify(new_location.to_dict()), 201

if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)
