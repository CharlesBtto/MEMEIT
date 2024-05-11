from flask import Flask, render_template, request, redirect, url_for, session, send_file
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/')
def exe():
  return render_template("index.html")


@app.route('/index2', methods=['GET', 'POST'])
def image():
  if request.method == 'POST':
    session['image_url'] = request.form['image_url']
    image_url = session['image_url']
  return render_template("index2.html", image_url=image_url)


@app.route('/index3', methods=['GET', 'POST'])
def texte():
  if request.method == 'POST':
    texte_saisi = request.form['texte_saisi']
    image_url = session.get('image_url', None)
  return render_template('index3.html',
                         texte_saisi=texte_saisi,
                         image_url=image_url)


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
  return render_template("gallery.html")


def take_screenshot(url):
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')  # Exécuter Chrome en arrière-plan
  options.add_argument('--no-sandbox')  # Pour éviter les erreurs de sandbox
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
  driver.get(url)
  # Attendre que la page se charge complètement (vous pouvez ajuster le délai si nécessaire)
  time.sleep(2)
  # Prendre un screenshot de la page entière
  screenshot_path = 'screenshot.jpg'
  driver.save_screenshot(screenshot_path)
  driver.quit()
  return screenshot_path




if __name__ == '__main__':
  app.run(debug=True)
