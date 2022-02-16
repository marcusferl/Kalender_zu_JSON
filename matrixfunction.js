function muell_event() {
    const fs = require('fs');
    var obj = JSON.parse(fs.readFileSync('muell.json'))

    const date = new Date();
    const date_day = String(date.getDate()).padStart(2, '0')
    const date_month = String(date.getMonth() + 1).padStart(2, '0')
    const date_year = date.getFullYear()


    console.log(obj.length)

    for (i = 0; i < obj.length; i++) {
        if ((obj[i].date['day'] == date_day) && (obj[i].date['month'] == date_month) && (obj[i].date['year'] == date_year)) {
            return obj[i].name
        }
    }
}