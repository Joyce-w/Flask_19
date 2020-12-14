const $resContainer = $(document.getElementsByClassName('results'))
const $answerInput = $(document.getElementsByClassName('answerInput'))
const $timer = $(document.getElementsByClassName('timer'))
const $message = $(document.createElement('h3')).addClass('resultMsg')
const $points = $(document.getElementsByClassName('pointsDiv'))
const $startDiv = $(document.getElementsByClassName('start'))
const $startBtn = $(document.getElementsByClassName('startBtn'))

function newBoggle() {


    //create set to track words used
    let entries = new Set() 
    let plays = 0

    //start timer on start btn click
    $startBtn.on('click', function (e) {
        e.preventDefault()
        $startBtn.toggle()
        $answerInput.toggle()
        countdownTimer()
    })

    //countdown 60 secs of guessing, reset afterwards
    function countdownTimer() {
        var counter = 5;
        var countdown = setInterval(function () {
            $timer.text(counter)
            counter--
            if (counter === -1) {
                clearInterval(countdown);
                $answerInput.toggle()
                $timer.text("Game over!")
                $message.toggle()
                plays++
                const scores = registerScore(entries.size, plays)
                scores
                // postScore(scores)
            }
        }, 1000);
    }

    //send score to json
    async function registerScore(score, plays) {

        let input = {
            "score": score,
            "plays": plays
        }

        const res = await axios.post("/score_board", input)
        console.log(res.data)
        return res.data
    } 


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
        
        //add point for every new guess
        if (msg == "is a word! Great job") {
            entries.add(word)
            $points.text(`Current points: ${entries.size}`)
        }

    }


    
}







newBoggle()