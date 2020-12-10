$('form').on('submit', async function (e) {
    e.preventDefault()
    $answer = $('input').val()
    console.log($answer)
    
    let input = {submitted: $answer}
    
    //send form input value to server using ajax
    $.ajax({
        type: "POST",
        url: "/answers",
        data: input,
        success: "Input data sent successfully",
        dataType: 'json'
    })

    $('input').val('') 
})

