from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
import mysql.connector

app = Flask(__name__)
app.secret_key = 'Atp@4466'  # Required for flashing messages

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "Atp@4466"),
        database=os.getenv("DB_NAME", "battery_sells_db"),
        port=3306
    )

# Route to handle form submission
@app.route('/add', methods=['GET', 'POST'])
def index():
    print("inside the index ")
    print(request.method)
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        mobile_number = request.form['mobile_number']
        sale_date = request.form['sale_date']
        # print(sale_date)
        battery_id = request.form['battery_id']
        battery_name = request.form['battery_name']
        # print(battery_name)
        ampires = request.form['ampires']
        price = request.form['price']
        warranty = request.form['warranty']

        conn = get_db_connection()
        c = conn.cursor()

        # Check if battery ID already exists
        c.execute('SELECT * FROM battery_sales WHERE battery_id = %s', (battery_id,))
        existing_battery = c.fetchone()

        if existing_battery:
            # Flash message for duplicate battery ID
            flash(f"सीरियल नंबर वाली बैटरी पहले से मौजूद है : {battery_id}", 'error')
        else:
                # Insert the new battery sale data
            c.execute('''
                INSERT INTO battery_sales (customer_name, mobile_number, sale_date, battery_name, battery_id, ampires, price, warranty)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (customer_name, mobile_number, sale_date, battery_name, battery_id, ampires, price, warranty))
            conn.commit()

            # Flash success message
            flash("बैटरी डेटा सफलतापूर्वक जोड़ा गया!", 'success')

        conn.close()

        return redirect(url_for('index'))

    return render_template('index.html')

# Route to handle searching for data by battery ID
@app.route('/search', methods=['GET', 'POST'])
def search():
    result = None
    session.clear()
    if request.method == 'POST':
        battery_id = request.form['battery_id']
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM battery_sales WHERE battery_id = %s', (battery_id,))
        result = c.fetchone()
        conn.close()
        if result:
            
            return render_template('search.html', result=result)
        else:
            flash("Not Found")
            return render_template('search.html', result=result)
    return render_template('search.html', result=result)


@app.route("/")
def main():
    return render_template("main.html") 

port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
