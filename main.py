from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
import os
from dotenv import load_dotenv

load_dotenv()


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_CODE')

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.name}>'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = Books.query.all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']

        existing_book = db.session.execute(
            db.select(Books).where(Books.name == title)
        ).scalar()

        if not existing_book:
            db.session.add(
                Books(
                    name=title,
                    author=author,
                    rating=rating
                )
            )
            db.session.commit()
            flash("Book added successfully!", "success")
        else:
            flash(f'\'{title}\' by {author} is already there in your BookShelf', 'warning')

        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit_rating/<int:edit_id>', methods=['GET', 'POST'])
def edit_rate(edit_id):
    if request.method == 'POST':
        book_to_update = db.get_or_404(Books, edit_id)
        new_rating = request.form.get('New Rating')
        if new_rating:
            try:
                book_to_update.rating = round(float(new_rating), 2)
                db.session.commit()
            except ValueError:
                flash("Invalid rating! Please enter a numeric value.", "danger")
                return redirect(url_for('edit_rate', edit_id=edit_id))

        return redirect(url_for('home'))
    book_to_update = db.get_or_404(Books, edit_id)
    return render_template('edit_rating.html', book=book_to_update)


@app.route('/delete')
def delete_book():
    delete_id = request.args.get('delete_id')
    book_to_delete = db.get_or_404(Books, delete_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    flash(f"'{book_to_delete.name}' was successfully deleted.", "success")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
