# TOC Project 2017

Tennis Good Good Bot

A telegram bot based on a finite state machine,

which provide service of searching ATP / WTA rankings

also introduction of Tennis Grand Slam.

## Setup

### Prerequisite
* Python 3

#### Install Dependency
```sh
pip install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
./ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

* user
	* Input: "/start" --> state0
    * Go to: state0
		![fsm](./img/readme1.jpg)

    * Input: string contains "ATP" or "Men" or "1"
    * Go to: state2
        ![fsm](./img/readme2.jpg)
        ![fsm](./img/readme3.jpg)
        ![fsm](./img/readme4.jpg)
    

* state0
    * Go Back: user
    


## Author
[Lee-W](https://github.com/Lee-W)
[Andy Tseng](https://github.com/a0952866367)
