{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\csgray\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #How to run this flask project\
\
#Work in your terminal and navigate to the pauseMIT directory\
\
#We need flask, and the way the internet says to run it without fucking with your machine is to activate a virtual environment. \

\f1\fs22 \cf2 \CocoaLigature0 env/bin/activate\
\

\f0\fs24 \cf0 \CocoaLigature1 # we need to download the packages so make sure your pip install shit works and download flask\

\f1\fs22 \cf2 \CocoaLigature0 python3 -m pip install Flask\

\f0\fs24 \cf0 \CocoaLigature1 \
#Now we need to go to where we actually create a flask object, so navigate to the app directory\
export FLASK_APP=__init__.py\
\
# from now on to run just \
flask run\
\
#enter http address in chrome , CTRL + C to quit.\
}