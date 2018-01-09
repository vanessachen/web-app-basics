# quizapp
a Word Quiz flask app 

##Notes for the Quiz App

The purpose of this app is to teach full stack web development.  quizapp is a Flask application (written in Python 3) which demonstrates the use of MongoDB with pymongo.  In order to run this code on your local machine, follow these steps:

* clone the repo

git clone <>

* set up a virtual environment

`virtualenv -p python3 qenv`

* start the virtualenv

`. qenv/bin/activate`

* upgrade pip immediately to avoid installation errors

`pip install --upgrade pip`

* install required packages:

`pip install -r requirements.txt`

You'll need to create a `secure.py` file in order for this app to run.

Here is a sample `secure.py` file.

APP_SECRET_KEY = "whoa this is a 53crEt K3Y!!!"

MONGO_USERNAME = "dev"
MONGO_PASSWORD = "really secure passw0rd"





Next, we need to set up the users inside MongoDB.

at the prompt, run this:

mongo

> use admin
db.createUser(  
  {
    user: "admin1",
    pwd: "some other re@lly secure passw0rd",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)

use aprender

db.createUser(
  {
    user: "dev",
    pwd: "really secure passw0rd",
    roles: [ { role: "readWrite", db: "aprender" },]
  }
)


* in a new terminal window, start a MongoDB instance

`mongod`

* import the example data!
(edit this command to include the proper filepath)

`mongoimport --db aprender --collection thingstolearn --type csv --headerline --file /file/path/to/the/CSV/quizwords.csv`

* run the db setup file (ONLY ONCE)

`python dbsetup.py`

* run the app

`python app.py`

If successful, you should then see a message such as:

```
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: (numbers)
```


First, go to:

http://0.0.0.0:8080/demo

This is just a plain HTMl page.  Can you find the files inside /templates which you need to edit in order to modify this page?  
##Run you Flask server on the local network:

* start your flask server with this command: 

`flask run --host=0.0.0.0`

* Then run this command in the terminal and scroll up some:

`ifconfig`

* Copy the number in bold (it will be different for you) and share it with your friends. It is your local ip for the day:

(wenv)  xxxxxxx  ~/src  ifconfig <br/>
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384 <br/>
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP> <br/>
	inet 127.0.0.1 netmask 0xff000000 <br/>
	inet6 ::1 prefixlen 128 <br/>
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 <br/>
	nd6 options=201<PERFORMNUD,DAD> <br/>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280 <br/>
stf0: flags=0<> mtu 1280 <br/>
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500 <br/>
	ether dc:a9:04:90:78:25 <br/>
	inet6 fe80::14d5:6136:f806:1ff9%en0 prefixlen 64 secured scopeid 0x4 <br/>
	inet **10.1.111.111** netmask 0xfffff800 broadcast 10.1.111.111 <br/>
	nd6 options=201<PERFORMNUD,DAD> <br/>
	media: autoselect <br/>
	status: active <br/>
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500 <br/>
	options=60<TSO4,TSO6> <br/>
	ether 0000000000000000000000000000000 <br/>
	media: autoselect <full-duplex> <br/>
	status: inactive <br/>
en2: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500 <br/>
	options=60<TSO4,TSO6> <br/>
	ether 0000000000000000000000000000000 <br/>
	media: autoselect <full-duplex> <br/>
	status: inactive <br/>
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304 <br/>
	ether 0000000000000000000000000000000 <br/>
	media: autoselect <br/>
	status: inactive <br/>
awdl0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1484 <br/>
	ether 0000000000000000000000000000000 <br/>
	inet6 0000000000000000000000000000000 64 scopeid 0x8 <br/>
	nd6 options=201<PERFORMNUD,DAD> <br/>
	media: autoselect <br/>
	status: active <br/>
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500 <br/>
	options=63<RXCSUM,TXCSUM,TSO4,TSO6> <br/>
	ether fe:00:a4:62:90:00 <br/>
	Configuration: <br/>
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0 <br/>
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200 <br/>
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0 <br/>
		ipfilter disabled flags 0x2 <br/>
	member: en1 flags=3<LEARNING,DISCOVER> <br/>
	        ifmaxaddr 0 port 5 priority 0 path cost 0 <br/>
	member: en2 flags=3<LEARNING,DISCOVER> <br/>
	        ifmaxaddr 0 port 6 priority 0 path cost 0 <br/>
	nd6 options=00<PERFORMNUD,DAD> <br/>
	media: <unknown type> <br/>
	status: inactive <br/>
utun0: flags=000<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 000 <br/>
	inet6 000000000000000000 prefixlen 0 scopeid 00 <br/>
	nd6 options=00<PERFORMNUD,DAD> <br/>
(wenv)  xxxxxxx  ~/src  <br/>

* Your friends can type this ip in their browsers, with a colon and the port number you were using before
`yourip:sameport`
