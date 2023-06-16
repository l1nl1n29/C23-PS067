# Bangkit Capstone Project C23-PS067 Documentation

This repository contains the documentation for [SeaSee GLOBALE](https://seesea-globalev1-vdrlzglb3q-et.a.run.app) API.

<h2>Table of Contents</h2>
<ol>
  <li>Overview</li>
  <li>How to run?</li>
  <ul>
    <li>Machine Learning Documentation</li>
    <li>Mobile Development Documentation</li>
    <li>Cloud Computing Documentation</li>
  </ul>
  <li>Resource</li>
  <li>Team Member of C23-PS067</li>
</ol>

## 1. Overview

   Marine pollution poses a serious threat to our oceans and marine ecosystems, with humangenerated trash being a major contributor. 
To address this issue, we propose the development of a Sea Trash Detector program called SeaSee GLOBALE. It utilizes computer vision
techniques to detect, track, and classify sea trash in real-time. By analyzing images captured by cameras on boats or drones, the program provides valuable insights into marine pollution sources and enhances pollution prevention efforts. Our goal is to reduce the impact of marine
pollution, protect marine ecosystems, and promote sustainable ocean management.

## 2. How to run?
 This API has been deployed using google cloud (Cloud Run) u can access it here:
  ```
   https://seesea-globalev1-vdrlzglb3q-et.a.run.app
  ```
  If u want to run it locally u need to:
  - Clone this repository `https://github.com/l1nl1n29/C23-PS067.git`
  - Open terminal and create venv using `python -m venv venv`
  - Install all requirement with `pip install -r requirements.txt`
  - Run `python api.py` in terminal to run flask
  - use url `http://127.0.0.1/` to access all api endpoint

## Machine Learning Documentation
<p>The process of Data Preparation and Modeling can be accessed in <a href="https://bit.ly/SeaSeeGLOBALE">this Google Colaboratory</a></p>
<ol>
  <li><h3>Load <a href="https://github.com/Alboneh/flask-main/blob/main/Groceries_dataset.csv">Dataset</a> and Import Necessary Modules</h3></li>
    - Gathering Sea Trash and Coral Dataset for Training and Validation
    - Cleaning Sea Trash and Coral Dataset for Training and Validation
    - Export Clean Sea Trash and Coral Dataset to Kaggle
    - Making Local Environment for Kaggle Dataset
    - Preprocess Dataset using Numpy and ImageDataGenerator
    - Preprocessing Classification Dataset model with Convolutional Neural Network and MaxPooling
    - Building and Training Classification Model using Sequential Tensorflow Keras Model
    - Adding Camera Feature on model
    - Making prediction model for classification
    - Deploying Classification Model to Tflite, *. json, *.h5 extension
		
## Mobile Development Documentation
<p>Here are the features we developed for the Android Application:</p>
<ul>
  <li>Splash screen, in this application there is a splashscreen before entering the main page</li>
  <li>Login Page, you can login using the registered email and password</li>
  <li>Register Page, you can register yourself by fill out the username,email,password form</li>
  <li>Home Page, you can see the list of product and their prediction for today sales</li>
  <li>Detail Page, contains the detail of the product and their prediction up to 14 days</li>
  <li>Add Sales Page, you can input the amount of sold out product in here</li>
</ul>

## Cloud Computing Documentation

![plot](./static/cloudimage2.png)

- ### 1. Creating Flask App to load model from Machine Learning
  - Create simple flask api with the name `api.py`
  - save model and dataset for Machine learning in same directory as `api.py`
  - Load the model in `api.py`
  - create endpoint and test model by running flask using `python api.py` to run it locally and getting predicted data using local ip.
- ### 2. creating Login and Register with Authentication in flask
  - Creating simple Login and Register using dummy database
  - create Json Web Token(JWT) to authenticate login and register
  - create JWT requirement to request prediction
  - change dummy database to cloud sql database
  - Test database to user login and register
  - Test authentication JWT using POSTMAN
- ### 3. Google Cloud Deployment
  - create Dockerfile and requirement.txt to store depedency and place it in root directory
  - clone flask repository `https://github.com/l1nl1n29/C23-PS067` in cloud shell
  - run this command to build container and push it to container registry
      ```
    docker build -t flask-app:v1 .
    docker tag flask-app:v1 gcr.io/western-beanbag-351610/flask-app:v1
    docker push gcr.io/western-beanbag-351610/flask-app:v1
    ```
  - Enable Cloud Run
  - select flask-app image container and deploy to cloud run 

    ```
## 4. Team Member of C22-PS152
<ol>
	<li>M040DSX2846 - Edward Al Faruq Purba</li>
	<li>M040DSX0003 - Ongky Setia Nugraha</li>
	<li>M040DSX1549 - Dien Manarul Aliem</li>
	<li>C339DSY3680 - Lin Lin Herlina</li>
	<li>C339DSX4889 - Gilang Gumelar Ramadan</li>
	<li>A214DSX3713 - Bridhoyoan Sinaga</li>
<ol>
	
