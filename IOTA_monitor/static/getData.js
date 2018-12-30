console.log("I'm correct loaded");


var IOTA = require('../../node_modules/iota.lib.js/lib/iota'); // load iota.lib.js

// # ctor initialization of the iota.lib.js library
var iota = new IOTA({
    'provider': 'https://nodes.thetangle.org:443'
});

// // basic API call to double check health conditions
// iota.api.getNodeInfo(function (error, success) {
//     if (error) {
//         // unable to perform getNodeInfo call
//         console.error(error);
//     } else {
//         // result is printed out
//         console.log(success);
//
//         // Basic check whether node is in sync or not
//         // Elementary rule is that "latestMilestoneIndex" should equal to "latestSolidSubtangleMilestoneIndex" or be very close
//         if (Math.abs(success['latestMilestoneIndex'] - success['latestSolidSubtangleMilestoneIndex']) > 3) {
//             console.log('\r\nNode is probably not synced!');
//         } else {
//             console.log('\r\nNode is probably synced!');
//         }
//     }
// });




var MySeed = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9";



//Let's generate 3 addresses using default security level=2.
//It is deterministic function - it always generates same addresses as long as the Seed, Security Level and Index are the same

// Please note, it is async method - result is returned via callback function

iota.api.getNewAddress(MySeed,
    { "index": 0, "total": 3, "security": 2 },
    function (error, success) {
        if (error) {
            console.log("Error occured: %s", error);
        } else {
            console.log();
            console.log(success); //returned addresses are printed out
        }
    });


"use strict";

iota.api.getAccountData(MySeed, {
  start: 0,
  security: 2
},function (accountData) {
  var addresses = accountData.addresses,
      inputs = accountData.inputs,
      transactions = accountData.transactions,
      balance = accountData.balance;
  console.log(transactions);
  // ...
    return transactions
});




// iota.api.getTransfers(MySeed);