const $resContainer = $(document.getElementsByClassName('results'))
const $message = $(document.createElement('h3')).addClass('resultMsg')
const $points = $(document.getElementsByClassName('pointsDiv'))
count = 0

//handle form data and response request
$('form').on('submit', async function (e) {
    e.preventDefault()

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
    if (result == 'ok'){
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

    keepScore(word,msg)
})

function keepScore(word, msg) {
    
    //create set to track words used
    let entries = new Set() 
    //add point with every new guess
    if (msg == "is a word! Great job") {
        count++
        entries.add(word)
        $points.text(`Current points: ${count}`)
    }
    else {
        $points.text(`Current points: ${count}`)
    }

}

