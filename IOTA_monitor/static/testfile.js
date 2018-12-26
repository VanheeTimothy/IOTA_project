'use strict';

function _asyncToGenerator(fn) { return function () { var gen = fn.apply(this, arguments); return new Promise(function (resolve, reject) { function step(key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { return Promise.resolve(value).then(function (value) { step("next", value); }, function (err) { step("throw", err); }); } } return step("next"); }); }; }

var Mam = require('./lib/mam.client.js');
var IOTA = require('iota.lib.js');
var moment = require('moment');
var iota = new IOTA({ provider: 'https://nodes.testnet.iota.org:443' });

var MODE = 'restricted'; // public, private or restricted
var SIDEKEY = 'mysecret'; // Enter only ASCII characters. Used only in restricted mode
var SECURITYLEVEL = 3; // 1, 2 or 3
var TIMEINTERVAL = 30; // seconds

// Initialise MAM State
var mamState = Mam.init(iota, undefined, SECURITYLEVEL);

// Set channel mode
if (MODE == 'restricted') {
    var key = iota.utils.toTrytes(SIDEKEY);
    mamState = Mam.changeMode(mamState, MODE, key);
} else {
    mamState = Mam.changeMode(mamState, MODE);
}

// Publish data to the tangle
var publish = function () {
    var _ref = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee(packet) {
        var trytes, message;
        return regeneratorRuntime.wrap(function _callee$(_context) {
            while (1) {
                switch (_context.prev = _context.next) {
                    case 0:
                        // Create MAM Payload

                        trytes = iota.utils.toTrytes(JSON.stringify(packet));
                        message = Mam.create(mamState, trytes);
                        message.address = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD";
                        // Save new mamState

                        mamState = message.state;
                        console.log('Root: ', message.root);
                        console.log('Address: ', message.address);

                        // Attach the payload.
                        _context.next = 7;
                        return Mam.attach(message.payload, message.address);

                    case 7:
                        return _context.abrupt('return', message.root);

                    case 8:
                    case 'end':
                        return _context.stop();
                }
            }
        }, _callee, this);
    }));

    return function publish(_x) {
        return _ref.apply(this, arguments);
    };
}();

var generateJSON = function generateJSON() {
    // Generate some random numbers simulating sensor data
    var data = Math.floor(Math.random() * 89 + 10);
    var dateTime = moment().utc().format('DD/MM/YYYY hh:mm:ss');
    var json = { "data": data, "dateTime": dateTime };
    return json;
};

var executeDataPublishing = function () {
    var _ref2 = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee2() {
        var json, root;
        return regeneratorRuntime.wrap(function _callee2$(_context2) {
            while (1) {
                switch (_context2.prev = _context2.next) {
                    case 0:
                        json = generateJSON();

                        console.log("json=", json);

                        _context2.next = 4;
                        return publish(json);

                    case 4:
                        root = _context2.sent;

                        console.log('dateTime: ' + json.dateTime + ', data: ' + json.data + ', root: ' + root);

                    case 6:
                    case 'end':
                        return _context2.stop();
                }
            }
        }, _callee2, this);
    }));

    return function executeDataPublishing() {
        return _ref2.apply(this, arguments);
    };
}();

// Start it immediately
executeDataPublishing();

setInterval(executeDataPublishing, TIMEINTERVAL * 1000);