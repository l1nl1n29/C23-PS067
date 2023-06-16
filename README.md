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
  <ul>
    <li>Gathering Sea Trash and Coral Dataset for Training and Validation</li>
    <li>Cleaning Sea Trash and Coral Dataset for Training and Validation</li>
    <li>Export Clean Sea Trash and Coral Dataset to Kaggle</li>
    <li>Making Local Environment for Kaggle Dataset</li>
    <li>Preprocess Dataset using Numpy and ImageDataGenerator</li>
    <li>Preprocessing Classification Dataset model with Convolutional Neural Network and MaxPooling</li>
    <li>Building and Training Classification Model using Sequential Tensorflow Keras Model</li>
    <li>Adding Camera Feature on model</li>
    <li>Making prediction model for classification</li>
    <li>Deploying Classification Model to Tflite, *. json, *.h5 extension</li>
  </ul>
		
## Mobile Development Documentation
<p>Tasks that have been completed by mobile development: </p>
<ul>
  <li>Created a user flow using draw.io</li>
  <li>Created Wireframe using Figma</li>
  <li>Analyzed the Design</li>
  <li>Created Prototype using Figma</li>
  <li>Implemented the Design into the Application using Android Studio and Jetpack Library</li>
  <li>Created Authentication Code for Users using Android Studio</li>
  <li>Created Validation Code for EditText on Login and Register section using Android Studio</li>
  <li>Used Lotie-Airbnb loading animation on the button</li>
  <li>Created viewmodels and adapters for each activity and fragment using Android Studio</li>
  <li>Created Room Database so that user data can be saved if the application is closed</li>
  <li>Created code for Intent Camera and Intent Gallery on Android Studio</li>
  <li>Created code to connect the application to the Cloud using retrofit</li>
  <li>Tested the application</li>
</ul>

## Cloud Computing Documentation

<ul>
    <li>Create a local database using PHP MyAdmin</li>
    <li>Create Private API Endpoint for register, login, predict, logout, and user</li>
    <li>Connecting Private API with machine learning models using Flask</li>
    <li>Create a database in Cloud SQL</li>
    <li>Building a docker image in a cloud shell</li>
    <li>Deploying the build image to Cloud Run</li>
</ul>


## 3. Team Member of C23-PS067
<ol>
	<li>M040DSX2846 - Edward Al Faruq Purba</li>
	<li>M040DSX0003 - Ongky Setia Nugraha</li>
	<li>M040DSX1549 - Dien Manarul Aliem</li>
	<li>C339DSY3680 - Lin Lin Herlina</li>
	<li>C339DSX4889 - Gilang Gumelar Ramadan</li>
	<li>A214DSX3713 - Bridhoyoan Sinaga</li>
<ol>
	
