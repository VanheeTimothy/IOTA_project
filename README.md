# "IOTA Project"
## Proof of Concept
### Concept
Just like people share data, machines do it too. 
Nowadays security has reached an unseen level of awareness. The need of tamperproof systems is higher now than ever before. Here's were [IOTA](https://https://www.iota.org) comes in. IOTA’s distributed ledger, by contrast, does not consist of transactions grouped into blocks and stored in sequential chains, but as a stream of individual transactions entangled together.

### Proof 
This project will demonstrate how to send sensor data from a Raspberry Pi to the Tangle. All data will be displayed on a dashboard which is running on a Flask webserver.

### Project structure
+---.idea
+---IOTA_monitor
|   |   get_new_address.py
|   |   IOTA_monitor.py
|   |   update_database.py
|   +---.idea
|   |   \---inspectionProfiles
|   +---model
|   |       FetchIotaTxs.py
|   |       Logreader.py
|   +---static
|   |   +---img
|   |   \---lib
|   +---templates
|   \---__pycache__
\---IOTA_sensor
    |   generate_seed.py
    |   led.py
    |   main.py
    +---.idea
    |   \---inspectionProfiles
    \---model
        |   DHT11.py
        |   OneWire.py
        |   RGBmixer.py
        |   TransferIotaTxs.py
        \---__pycache__
