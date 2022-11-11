let items = document.getElementById("items"); 
let para;

class Purchase {
  constructor(namn, prefix, tid = [], veckodag = []) {
    this.today = new Date()
    this.today_date = this.today.getFullYear() + "-" + (this.today.getMonth()+1) + "-" + this.today.getDate() 
    this.namn = namn;
    this.prefix = prefix;
    this.tid = tid
    this.tid2 = new Date(this.today_date + " " + this.tid)
    this.veckodag = veckodag;
  }
};

function timeLeft(object) {
    let today = new Date()
    var diff = (object - today);
    var diffHours = Math.floor(Math.abs(((diff % 86400000) / 3600000)));
    var diffMinutes= Math.floor(Math.abs(((diff % 86400000) % 3600000) / 60000));
    var diffSeconds = Math.floor(Math.abs((((diff % 86400000) % 3600000) % 60000) / 1000));
    if (diff < 0) {
      var fullDiff = (diffHours + "h" + diffMinutes + "m" + diffSeconds + "s");
      return fullDiff + " FÖRSENAD";  
    } else {
      var fullDiff = (diffHours + "h" + diffMinutes + "m" + diffSeconds + "s");
      return fullDiff; 
    }

  }




let list = [];
var today = new Date()
let weekday = today.getDay();

const fristads = new Purchase("Fristads", "FI", ['15:00:00'], [2, 5]);
list.push(fristads);
const blaklader = new Purchase("Blåkläder", "BL", ['15:00:00'], [1, 5]);
list.push(blaklader);

for(const lev of list) {
  var today = new Date()
  if(lev.veckodag.includes(weekday)){
    para = document.createElement("p");
    para.innerHTML = lev.namn + " " + "Tid kvar: " + timeLeft(lev.tid2);
    items.appendChild(para);                               
  }
};

function update() {
  for(const lev of list) {
    para.innerHTML = lev.namn + " " + "Tid kvar: " + timeLeft(lev.tid2);
    console.log(lev.namn + " " + "Tid kvar: " + timeLeft(lev.tid2))
  } 
};

setInterval(update, 300);