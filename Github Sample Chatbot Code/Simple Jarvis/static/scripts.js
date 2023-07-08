$(document).ready(function() {
    $('#send-message').on('click', function() {
        sendMessage();
    });

    $('#user-input').on('keypress', function(e) {
        if (e.which === 13) {
            sendMessage();
        }
    });

    $('#new-conversation').on('click', function() {
        $('#conversation-history').html('');
    });

    function sendMessage() {
        var userMessage = $('#user-input').val();
        if (userMessage.trim() !== '') {
            $('#conversation-history').append('<div class="message user">User: ' + userMessage + '</div>');
            $('#user-input').val('');

            $.ajax({
                url: '/message',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({message: userMessage}),
                success: function(data) {
                    var chatbotResponse = data.response;
                    $('#conversation-history').append('<div class="message assistant">JARVIS: ' + chatbotResponse + '</div>');
                    $('#conversation-history').scrollTop($('#conversation-history')[0].scrollHeight);
                }
            });
        }
    }
});

