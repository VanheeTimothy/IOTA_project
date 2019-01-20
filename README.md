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
│   │   ├── Logreader.py
│   │   └── __pycache__
│   │       ├── FetchIotaTxs.cpython-35.pyc
│   │       └── Logreader.cpython-35.pyc
│   ├── __pycache__
│   │   ├── FetchIotaTransfers.cpython-35.pyc
│   │   ├── FetchIotaTransfers.cpython-36.pyc
│   │   ├── FetchIotaTxs.cpython-35.pyc
│   │   └── FetchIotaTxs.cpython-36.pyc
│   ├── static
│   │   ├── dropdownbutton.js
│   │   ├── graphs.js
│   │   ├── img
│   │   │   ├── iotalogo.png
│   │   │   ├── iota_monitor.png
│   │   │   └── iota.png
│   │   ├── lib
│   │   │   └── mam.client.js
│   │   ├── reset.css
│   │   └── style.css
│   ├── templates
│   │   ├── Analytics.html
│   │   ├── GraphsDaily.html
│   │   ├── GraphsMonthly.html
│   │   ├── GraphsWeekly.html
│   │   ├── index.html
│   │   ├── Logs.html
│   │   ├── Settings.html
│   │   └── Transactions.html
│   └── update_database.py
├── IOTA_sensor
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
│       ├── __pycache__
│       │   ├── DHT11.cpython-35.pyc
│       │   ├── DHT11.cpython-36.pyc
│       │   ├── OneWire.cpython-35.pyc
│       │   ├── RGBmixer.cpython-35.pyc
│       │   └── TransferIotaTxs.cpython-35.pyc
│       ├── RGBmixer.py
│       └── TransferIotaTxs.py
├── projectstructure.txt
├── README.md
└── requirements.txt

15 directories, 55 files
```