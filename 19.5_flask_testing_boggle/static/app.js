const $resContainer = $(document.getElementsByClassName('results'))
const $answerInput = $(document.getElementsByClassName('answerInput'))
const $timer = $(document.getElementsByClassName('timer'))
const $message = $(document.createElement('h3')).addClass('resultMsg')
const $points = $(document.getElementsByClassName('pointsDiv'))
const $startDiv = $(document.getElementsByClassName('start'))
const $startBtn = $(document.getElementsByClassName('startBtn'))

//create set to track words used
let entries = new Set() 

//start timer on start btn click
$startBtn.on('click', function (e) {
    e.preventDefault()
    $startBtn.toggle()
    $answerInput.toggle()
    countdownTimer()
})

//countdown 60 secs of guessing, reset afterwards
function countdownTimer() {
    var counter = 60;
    var countdown = setInterval(function () {
        $timer.text(counter)
        counter--
        if (counter === -1) {
            clearInterval(countdown);
            $answerInput.toggle()
            $timer.text("Game over!")
        }
    }, 1000);
}

//reload page when start button is clicked


//handle form data and response request
$('form').on('submit', async function (e) {
    e.preventDefault()
    $startDiv.toggle()

    //save input value
    let $answer = $('input').val()

     // send form input value to server using axios
    let input = {"submitted": $answer}
    const res = await axios.get("/answers", { params: { "submitted": $answer } })
    
    //save server response data
    let word = res.data.word
    let result = res.data.result

    //handle result response
    function results() {
        if (result == 'ok') {
        return "is a word! Great job"
    }
    else if( result == 'not-on-board'){
        return "isn't  a word, did you misspell?"
    }
    else{
       return "isn't a word buddy. Try again"
    }
    }
    msg = results()

    //removes any current result message
    $('.resultMsg').empty()

    //append response data to page
    $message.text(`"${word}" ${msg}`)
    $resContainer.append($message)

    //clear input after submitting 
    $('input').val('') 

    keepScore(word, msg, entries)
    
})

function keepScore(word, msg) {
    
    //add point with every new guess
    if (msg == "is a word! Great job") {
        entries.add(word)
        $points.text(`Current points: ${entries.size}`)
    }

}


let menu = {
    width: 200,
    height: 300,
    title: "My menu"
};

function multiplyNumeric(menu) {
    for (let item in menu) {
        if (typeof(menu[item] == "number")){
            menu[item] *= 2;
        }
    }
}
multiplyNumeric(menu)