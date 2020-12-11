//handle form data and response request 
$('form').on('submit', async function (e) {
    e.preventDefault()

    //save input value
    let $answer = $('input').val()
    console.log($answer)

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
       return "...umm, not a word buddy. Try again"
    }
    }
    let msg = results()

    //removes any current result message
    let $resContainer = $(document.getElementsByClassName('results'))
    let $message = $(document.createElement('h3')).addClass('resultMsg')
    $('.resultMsg').empty()

    //append response data to page
    $message.text(`"${word}" ${msg}`)
    $resContainer.append($message)

    //clear input after submitting 
    $('input').val('') 

})

