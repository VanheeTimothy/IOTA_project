# "IOTA Project"
## Proof of Concept
### Concept
Just like people share data, machines do it too. 
Nowadays security has reached an unseen level of awareness. The need of tamperproof systems is higher now than ever before. Here's were [IOTA](https://https://www.iota.org) comes in. IOTA’s distributed ledger, by contrast, does not consist of transactions grouped into blocks and stored in sequential chains, but as a stream of individual transactions entangled together.

### Proof 
This project will demonstrate how to send sensor data from a Raspberry Pi to the Tangle. All data will be displayed on a dashboard which is running on a Flask webserver.

### Project structure
```bash
IoT_IOTA/
├── IOTA_monitor
│   ├── credentials.py
│   ├── get_new_address.py
│   ├── IOTA_monitor.py
│   ├── launch
│   │   ├── launchflask.sh
│   │   ├── logfetcher.sh
│   │   └── updatedatabase.sh
│   ├── logs
│   │   ├── cronlog
│   │   ├── flask.log
│   │   ├── logfetchlog
│   │   ├── logfetch.log
│   │   ├── sensor.log
│   │   └── updatedatabase.log
│   ├── model
│   │   ├── FetchIotaTxs.py
│   │   └── Logreader.py
│   ├── static
│   │   ├── dropdownbutton.js
│   │   ├── graphs.js
│   │   ├── img
│   │   │   ├── iotalogo.png
│   │   │   ├── iota_monitor.png
│   │   │   └── iota.png
│   │   ├── insightscharts.js
│   │   ├── lib
│   │   │   └── mam.client.js
│   │   ├── reset.css
│   │   ├── sensorcharts.js
│   │   └── style.css
│   ├── templates
│   │   ├── Analytics.html
│   │   ├── GraphsDaily.html
│   │   ├── GraphsMonthly.html
│   │   ├── GraphsWeekly.html
│   │   ├── index.html
│   │   ├── Logs.html
│   │   ├── Settings.html
│   │   ├── TangleExplorer.html
│   │   └── Transactions.html
│   └── update_database.py
├── IOTA_sensor
│   ├── credentials.py
│   ├── generate_seed.py
│   ├── launch
│   │   └── launchsendiota.sh
│   ├── led.py
│   ├── logs
│   │   ├── cronlog
│   │   └── main.log
│   ├── main.py
│   └── model
│       ├── DHT11.py
│       ├── OneWire.py
│       ├── OneWire.pyc
│       ├── RGBmixer.py
│       └── TransferIotaTxs.py
├── projectstructure.txt
├── README.md
└── requirements.txt

12 directories, 49 files

```