# CGM Glucose Modeling

## Description

This project is designed to extend the diabetes data and insights democratized by the Nightscout project into the realm of real-time streaming, IoT integrations, and data science predictive modeling techniques. 

I was diagnosed with Type 1 Diabetes over 26 years ago, and while the treatment and patient enablement technologies have made measurable leaps over this period of time, I have not been more excited than my recent acquisition of the Dexcom G6 Continuous Glucose Monitoring system. As explained on the [Nightscout project page](https://nightscout.github.io/),

>Nightscout (also known as "CGM in the Cloud") is an open-source cloud application used by people with diabetes and parents of kids with diabetes to visualize, store and share the data from their Continuous Glucose Monitoring sensors in real-time.
>
The Nightscout project provides detailed instructions for building a data pipeline from the Dexcom (or other providers') CGM systems and visualizing/reporting on the data in nearly real-time via an online application.

I used the helpful Nightscout installation guide to set up a MongoDB database and host the web application for real-time viewing on Heroku, and the application is available for viewing at [this link](https://ryan-cgm-iot.herokuapp.com/).

With my sensor data easily accessible through MongoDB Atlas, this project has two aims:

1. Extend the data availability onto IoT technologies visualizing current blood glucose levels and directional trends.
2. Apply cutting edge ML/AI modeling techniques to train novel predictive algorithms and compare performance to current industry standards.

This project is an ongoing effort driven by my personal interest in data science and personal and public health outcomes. While I am happy to share my data in the interest of replicability and furthering research, I ask for general respect regarding the exploration and use of my personal medical data and reserve the right to limit and revoke access for any reason and at any time.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

## Installation

I followed the Nightscout installation guide to establish a Heroku-based application accessing data from a MongoDB Atlas database.

## Usage

The code contained in this repository provides a series of helper utilities for extracting data from MongoDB for regular backup, data cleaning and processing for usage in an IoT application, and a notebook containing my work to-date applying ML/AI techniques to train and tune a predictive model for blood glucose over time.

The scripts are written and tested with Python 3.9 and depend on the libraries and versions specified in the
`requirements.txt` file.

## Credits

Significant credit for this project is owed to the foundational work advancing and democratizing diabetes treatment by these organizations:

- [Nightscout Project](https://nightscout.github.io/)
- [Dexcom](https://www.dexcom.com/)

Additional insights and algorithmic direction was gathered from the organizations and projects listed below.
- [Tidepool](https://www.tidepool.org/) - committed to emplowering the next generation of innovations in diabetes management and encouraging patients to safely achieve great outcomes through more accessible, actionable, and meaningful diabetes data.
- [OpenAPS](https://openaps.org/) - an open and transparent effort to make safe and effective basic Artificial Pancreas System (APS) technology widely available.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

---