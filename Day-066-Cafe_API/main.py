import random
from flask import Flask, jsonify, render_template, request, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from pathlib import Path
import os

app = Flask(__name__)

API_KEY = os.environ["api_key"]


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self,
                                              column.name)  # Create a new dictionary entry; where the key is the name of the column and the value is the value of the column
        return dictionary


# Getting the instance folder path
instance_path = Path(app.instance_path)
db_path = instance_path / 'cafes.db'


def create_database():
    # Checking if the database file exist or not as per that new database will be created
    if not db_path.exists():
        with app.app_context():
            db.create_all()

        print(f'Database created successfully!')

    else:
        try:
            print(f'Database already exists at:, {db_path}')
            print(f'Skipping creation.')

        except OSError:
            pass


def read_cafe_data():
    """this function will read the old database of cafe and return the cafes_obj"""

    cafe_data = db.session.execute(db.select(Cafe).order_by(Cafe.id))  # here we are reading the old movies data so we can use them.
    cafes = cafe_data.scalars()

    return cafes

@app.route("/")
def home():
    """this is a home route and it will render the home page."""

    create_database()
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    """this route will show random cafe details in the web page in json format"""

    cafes_list = []
    cafes_obj = read_cafe_data()
    [cafes_list.append(cafe) for cafe in cafes_obj]
    chosen_cafe = random.choice(cafes_list)
    return jsonify(cafe=chosen_cafe.to_dict())


@app.route("/all")
def all():
    """this route will show all the cafes each details in the web page in json format"""

    cafes_obj = read_cafe_data()
    cafes_list = [cafe for cafe in cafes_obj]
    cafes = [cafe.to_dict() for cafe in cafes_list]
    return jsonify(cafes=cafes)


@app.route("/search")
def search():
    """this route will show all the cafes searched if it found that cafe location in a database"""

    location = request.args.get('loc')  # query parameter

    cafes_obj = read_cafe_data()
    searched_cafes_list = [cafes for cafes in cafes_obj if cafes.location == location]
    cafes = [cafe.to_dict() for cafe in searched_cafes_list]

    if cafes:
        return jsonify(cafes=cafes)
    elif not cafes:
        return jsonify(error="Not Found: Sorry, we don't have a cafe at that location")


@app.route("/add", methods=['POST'])
def add_new_cafe():
    """this route will add the new cafe into a database"""

    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_cafe_price(cafe_id):
    """this route will update the price of cafe."""

    if request.method == "PATCH":

        new_price = request.args.get('new_price')  # query parameter
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()

        if cafe:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."}), 200

        elif not cafe:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_cafe_store(cafe_id):
    """this route will delete the cafe if that cafe is being closed but user required an api key in order to do that thing."""

    if request.method == "DELETE":
        api_key = request.args.get('api-key')  # query parameter

        if api_key == API_KEY:
            delete_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()

            if delete_cafe:
                db.session.delete(delete_cafe)
                db.session.commit()
                return jsonify(response={"success": "Successfully deleted the cafe."}), 200

            elif not delete_cafe:
                return jsonify(error = {"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

        elif api_key != API_KEY:
            print("system")
            return jsonify(error = {"message": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
